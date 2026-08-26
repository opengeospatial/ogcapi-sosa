#!/usr/bin/env bash
# Creates a "clean" branch of a Building Blocks register fork, excluding all
# changes in the build/ directory (and fork-only config overrides), so that
# it can be used to open a Pull Request against the upstream register without
# generated-artifact merge conflicts.
#
# See https://opengeospatial.github.io/bblocks-docs/build/contribution for details.

usage() {
  echo "Usage: $0 [-u upstreamRemote] [-f forkRemote] [-b upstreamBranch] [-d buildDirectory] [-t tempBranch] [-P]"
  echo
  echo "Options:"
  echo "  -u    Upstream remote name (default: 'fork-parent')"
  echo "  -f    Fork remote name (default: 'origin')"
  echo "  -b    Upstream branch (default: 'main' or 'master')"
  echo "  -d    Build directory (default: 'build')"
  echo "  -t    Name for the temporary clean branch (default: randomly generated)"
  echo "  -P    Do not push to remote"
  echo "  -h    Show this help message"
  exit 1
}

UPSTREAM_REMOTE=fork-parent
BUILD_DIR=build
FORK_REMOTE=origin
UPSTREAM_BRANCH=
PUSH_TO_REMOTE=1
TMP_BRANCH=

while getopts "u:f:b:d:t:Ph" opt; do
  case $opt in
    u) UPSTREAM_REMOTE="$OPTARG" ;;
    f) FORK_REMOTE="$OPTARG" ;;
    b) UPSTREAM_BRANCH="$OPTARG" ;;
    d) BUILD_DIR="$OPTARG" ;;
    P) PUSH_TO_REMOTE=;;
    t) TMP_BRANCH="$OPTARG";;
    h) usage ;;
    \?) usage ;;
  esac
done

trap_add() {
    local cmd="$1"
    # shellcheck disable=SC2064
    trap "${cmd};$(trap -p EXIT | cut -d"'" -f2)" EXIT
}

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    echo "This script must be run inside a git directory."
    echo "If you are using Docker, check you have mounted the right volumes."
    exit 1
fi

if ! ( git diff --quiet && git diff --cached --quiet ); then
  echo "There are pending changes. Please commit or stash them before continuing."
  exit 1
fi

# Detect git-filter-repo
if [[ -x "./git-filter-repo" ]]; then
    FILTER_REPO_CMD="./git-filter-repo"
elif command -v git-filter-repo >/dev/null 2>&1; then
    FILTER_REPO_CMD="git-filter-repo"
elif git filter-repo --help >/dev/null 2>&1; then
    FILTER_REPO_CMD="git filter-repo"
else
    # Download the latest released version to a temp location
    LATEST_TAG=$(curl -sSfL https://api.github.com/repos/newren/git-filter-repo/releases/latest \
        | sed -n 's/.*"tag_name": *"\([^"]*\)".*/\1/p')
    if [[ -z "$LATEST_TAG" ]]; then
        echo "Could not determine the latest git-filter-repo release." >&2
        exit 1
    fi
    TMP_DIR=$(mktemp -d)
    FILTER_REPO_CMD="$TMP_DIR/git-filter-repo"
    if ! curl -sSfL -o "$FILTER_REPO_CMD" \
        "https://raw.githubusercontent.com/newren/git-filter-repo/${LATEST_TAG}/git-filter-repo"; then
      echo "Failed to download git-filter-repo ${LATEST_TAG}." >&2
      rm -rf "$TMP_DIR"
      exit 1
    fi
    chmod +x "$FILTER_REPO_CMD"
    trap_add "rm -rf \"$TMP_DIR\""
fi
echo "Using git-filter-repo command: $FILTER_REPO_CMD"

CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
trap_add "git checkout \"$CURRENT_BRANCH\" >/dev/null 2>/dev/null"

UPSTREAM_URL=$(git remote get-url "$UPSTREAM_REMOTE" 2>/dev/null)
if [[ $? -ne 0 || -z "$UPSTREAM_URL" ]]; then
  echo "Upstream remote '$UPSTREAM_REMOTE' does not exist. Please add it first by running:"
  echo "  git remote add ${UPSTREAM_REMOTE} git@github.com:username/repo.git"
  exit 1
fi
echo "Using upstream remote: ${UPSTREAM_REMOTE} / ${UPSTREAM_URL}"

FORK_URL=$(git remote get-url "$FORK_REMOTE" 2>/dev/null)
if [[ $? -ne 0 || -z "$FORK_URL" ]]; then
  echo "Fork (local) remote '$FORK_REMOTE' does not exist."
  exit 1
fi
echo "Using fork remote: ${FORK_REMOTE} / ${FORK_URL}"

set -euo pipefail
git fetch "${UPSTREAM_REMOTE}"

if [[ -z "$TMP_BRANCH" ]]; then
  TMP_BRANCH="clean-pr-$(date +%s).$RANDOM"
fi
git checkout -b "$TMP_BRANCH"

if [[ -z "${UPSTREAM_BRANCH}" ]]; then
  if git rev-parse --verify --quiet "${UPSTREAM_REMOTE}"/main >/dev/null; then
    UPSTREAM_BRANCH=main
  else
    UPSTREAM_BRANCH=master
  fi
fi
echo "Using upstream branch: ${UPSTREAM_BRANCH}"

$FILTER_REPO_CMD --path "${BUILD_DIR}" --path .fork --path bblocks-config-override.yml --path bblocks-config-override.yaml --invert-paths --force \
  --refs "${UPSTREAM_REMOTE}/${UPSTREAM_BRANCH}..HEAD"

if [[ -n "$PUSH_TO_REMOTE" ]]; then
  git push "${FORK_REMOTE}" "${TMP_BRANCH}"
  echo "Branch created and changed pushed"

  # Strip a trailing .git suffix, then split "owner/repo" on the last slash/colon.
  UPSTREAM_PATH="${UPSTREAM_URL#git@github.com:}"
  UPSTREAM_PATH="${UPSTREAM_PATH#https://github.com/}"
  UPSTREAM_PATH="${UPSTREAM_PATH%.git}"

  FORK_PATH="${FORK_URL#git@github.com:}"
  FORK_PATH="${FORK_PATH#https://github.com/}"
  FORK_PATH="${FORK_PATH%.git}"

  PR_URL="https://github.com/${UPSTREAM_PATH}/compare/${UPSTREAM_BRANCH}...${FORK_PATH%%/*}:${FORK_PATH#*/}:${TMP_BRANCH}?expand=1"
  echo ""
  echo "========"
  echo "You can use the following URL to create the Pull Request:"
  echo "  ${PR_URL}"
  echo "========"
  echo ""
else
  echo "Branch '${TMP_BRANCH}' created - push disabled"
fi
