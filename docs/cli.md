# Command Line Interface

```console
$ db-diagram -h
db-diagram -h
usage: db-diagram [-h] [-mmd MERMAID_MARKDOWN]
                  [-svg SCALABLE_VECTOR_GRAPHICS]
                  [-png PORTABLE_NETWORK_GRAPHICS] [-md MARKDOWN]
                  [-cf CONFIG_FILE] [-bc BACKGROUND_COLOR] [-t THEME]
                  [-i INCLUDE] [-e EXCLUDE] [-d DEPTH]
                  url

Write a markdown document with mermaid diagrams describing tables and
relationships for the specified database URL

positional arguments:
  url                   A [SQLAlchemy database URL](https://docs.sqla
                        lchemy.org/en/20/core/engines.html#database-
                        urls)

optional arguments:
  -h, --help            show this help message and exit
  -mmd MERMAID_MARKDOWN, --mermaid-markdown MERMAID_MARKDOWN
                        A directory in which to write mermaid
                        markdown (.mmd) documents. These documents
                        will be named using the format
                        `{TABLE_NAME}.mmd`.
  -svg SCALABLE_VECTOR_GRAPHICS, --scalable-vector-graphics SCALABLE_VECTOR_GRAPHICS
                        A directory in which to write SVG images. If
                        this option is provided in concert with the
                        --markdown / -md option, the markdown
                        document will utilize the SVG images in lieu
                        of embedding the mermaid diagrams. The SVG
                        files will be named using the format
                        `{TABLE_NAME}.mmd.svg`.
  -png PORTABLE_NETWORK_GRAPHICS, --portable-network-graphics PORTABLE_NETWORK_GRAPHICS
                        A directory in which to write PNG images. If
                        this option is provided in concert with the
                        --markdown / -md option, the markdown
                        document will utilize the PNG images in lieu
                        of embedding the mermaid diagrams. The PNG
                        files will be named using the format
                        `{TABLE_NAME}.mmd.png`.
  -md MARKDOWN, --markdown MARKDOWN
                        The file path to which to write a markdown
                        document
  -cf CONFIG_FILE, --config-file CONFIG_FILE
                        The path to a mermaid config file
  -bc BACKGROUND_COLOR, --background-color BACKGROUND_COLOR
                        A CSS background color for SVG diagrams
  -t THEME, --theme THEME
                        default | neutral | dark | forest | base
                        (only applicable for SVG/PNG images)
  -i INCLUDE, --include INCLUDE
                        Include only tables and views matching the
                        specified pattern(s) (for example:
                        "PREFIX_*")
  -e EXCLUDE, --exclude EXCLUDE
                        Exclude tables and views matching the
                        specified pattern(s) (for example:
                        "PREFIX_*")
  -d DEPTH, --depth DEPTH
                        Recursively traverse foreign key
                        relationships up to this number of times
```
