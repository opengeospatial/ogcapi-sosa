# OGC Building Block template

This repository can be used as a template to create new collections of
[OGC Building Blocks](https://opengeospatial.github.io/bblocks). 

## Building block structure

- `bblock.json`: Contains the metadata for the building block. Please refer to this
  [JSON schema](https://github.com/avillar/bblocks/blob/master/metadata-schema.yaml) for more information.
- `description.md`: Human-readable, Markdown document with the description of this building block.
- `examples.yaml`: A list of examples for this building block. See [Examples](#examples) below.
- `schema.yaml`: JSON schema for this building block, if any. See [JSON schema](#json-schema) below.
- `assets/`: Documentation assets (e.g. images) directory. See [Assets](#assets) below.

This repository includes a sample building block in the `my-building-block` directory.

Building Block identifiers are automatically generated in the form:

```
<identifier-prefix><bb-path>
```

where:

- `identifier-prefix` is read from `bblocks-config.yaml`. This will initially be a placeholder value,
  but should have an official value eventually (see [How-to](#how-to)).
- `bb-path` is the dot-separated path to the building block inside the repository.
 
For example, given a `r1.branch1.` identifier prefix and a `cat1/cat2/my-bb/bblock.json` metadata file,
the generated identifier would be `r1.branch1.cat1.cat2.my-bb`. This applies to the documentation
subdirectories as well, after removing the first element (e.g., Markdown documentation will be written to 
`generateddocs/markdown/branch1/cat1/cat2/my-bb/index.md`).

### Examples

Each example consists of Markdown `content` and/or a list of `snippets`. `snippets`, in turn,
have a `language` (for highlighting, language tabs in Slate, etc.) and the `code` itself. 

The `examples.yaml` file in `my-building-block` can be used as a template.

### JSON schema

The JSON schema for a building block can be linked to a conceptual model by using a root-level `@modelReference`
property pointing to a JSON-LD context document (relative paths are ok). The Building Blocks Register can 
then annotate every property inside the JSON schemas with their corresponding RDF predicate automatically.

If a `schema.yaml` file is found, it is not necessary to add the `schema` property to `bblock.json`; it will
be done automatically on the OGC Building Blocks Register. `ldContext` however, is not auto-generated. 

### Assets

Assets (e.g., images) can be placed in the `assets/` directory for later use in documentation pages,
by using references to `@@assets@@/filename.ext`.

For example, a `sample.png` image in that directory can be included in the description
Markdown code of a building block like this:

```markdown
![This is a sample image](@@assets@@/sample.png)
```

## How-to

1. Fork (or click on "Use this template" on GitHub) this repository.
2. For each new building block, replace or create a copy of the `my-building-block`.
   Note: **the name of the new directory will be part of the building block identifier**.
3. Update the building [block's files](#building-block-structure).
4. Replace this README.md file with documentation about the new building block(s).
5. Contact OGC and request that your new building block(s) be added to the official Register.
6. Set the `identifier-prefix` provided by OGC in `bblocks-config.yaml`.

Note: building blocks subdirectories can be grouped inside other directories, like so:

```
type1/
  bb1-1/
    bblock.json
  bb1-2/
    bblock.json
type2/
  subtype2-1/
    bb2-1-1/
        bblock.json
[...]
```

In that case, `type1`, `type2` and `subtype2-1` will also be part of the building block identifiers.

## Postprocessing overview

This repository comes with a GitHub workflow that detects, validates and processes its building blocks,
so that their outputs can be tested before inclusion in the main OGC Register:

![OGC Building Blocks processing](https://raw.githubusercontent.com/avillar/bblocks-postprocess/master/process.png)

### Output testing

The outputs can be generated locally by running the following (*Note: Docker must be installed locally*):

```shell
# Process building blocks
docker run --rm --workdir /workspace -v $(pwd):/workspace
# Optional - build Slate docs
docker run --rm -v "$(pwd)/generateddocs/slate:/srv/slate/source" \
  -v "$(pwd)/generateddocs/slate-build:/srv/slate/build" slatedocs/slate build
```