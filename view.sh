#!/bin/bash
# View the register locally
# Extra volumes (e.g. local URL mappings; see build.sh) are mounted here too, so the
# viewer can serve them
if [ -f '.volumes' ]; then
  VOLUMES=$(while read -r line; do
    if [[ "${line}" != /* ]]; then
      echo -n "-v ${PWD}/${line} "
    else
      echo -n "-v $line "
    fi
  done < .volumes)
fi
docker run --rm --pull=always -v "$(pwd):/register" ${VOLUMES} -p 9090:9090 ghcr.io/ogcincubator/bblocks-viewer
