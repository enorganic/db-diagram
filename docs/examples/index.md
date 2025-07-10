# Examples

The examples provided are all generated from the PostgreSQL database
for an instance of [Apache Airflow](https://airflow.apache.org), run
locally with `docker compose` as described [here
](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html).

The command to generate the first three "All" examples looked as follows,
substituting `-d 1` with the depth used in each example:

```bash
db-diagram \
    -d 1 \
    -t 'Airflow PostgreSQL Database Diagrams' \
    -md docs/examples/airflow/depth=1/diagrams.md \
    postgresql+psycopg://airflow:airflow@127.0.0.1:5432/airflow
```

The command to generate the filtered subset examples looked as follows,
substituting `-d 1` with the depth used in each example, and substituting
`-i 'ab_*'` for the appropriate inclusion or exclusion filter(s):

```bash
db-diagram \
    -i 'ab_*' \
    -d 1 \
    -t 'Airflow PostgreSQL Database Diagrams' \
    -md docs/examples/airflow/depth=1/diagrams.md \
    postgresql+psycopg://airflow:airflow@127.0.0.1:5432/airflow
```

...the "other" examples' commands looked as follows (they just had several `-e`
options to filter out all other subsets):

```bash

```bash
db-diagram \
    -e 'ab_*' \
    -e 'asset_*' \
    -e 'dag_*' \
    -e 'task_*' \
    -d 1 \
    -t 'Airflow PostgreSQL Database Diagrams' \
    -md docs/examples/airflow/depth=1/diagrams.md \
    postgresql+psycopg://airflow:airflow@127.0.0.1:5432/airflow
```

The command to generate the second three examples, for which images
are pre-rendered as SVG (scalable vector graphics), looked as
follows—substituting `-d 1` with the depth used in each example:

```bash
db-diagram \
    -d 1 \
    -t 'Airflow PostgreSQL Database Diagrams' \
    -svg docs/examples/airflow/depth=1/svg \
    -t dark \
    -md docs/examples/airflow/depth=1/diagrams-svg.md \
    postgresql+psycopg://airflow:airflow@127.0.0.1:5432/airflow
```

As you can see above, in the second set of examples, we specify an SVG
image directory. This causes `db-diagram` to render each diagram
as an SVG image, using the specified theme (such as `-t dark`). Optionally,
a CSS background color can be provided (by default this is `-bg transparent`),
or for greater control a JSON [mermaid config file
](https://mermaid.js.org/config/schema-docs/config.html) can be specified
using the `-cf` option.

Hopefully these examples will provide you with insight concerning the
effect of `db-diagram` options, particularly concerning depth, image
rendering, and include/exclude filtering.

-   **Depth**: Note that, when you specify a depth greater than one—you start
    to generate diagrams which may be difficult to read. Usually,
    the default depth (1) is optimal, but it will only show all relationships
    for a single table in each diagram.
-   **Pre-Rendering Images**: When you pre-render images—your pages load more
    quickly, but diagrams are not uniformly sized throughout the document.
    When you don't pre-render images, for databases with many tables—there
    will be a noticeable delay before diagrams are rendered.
-   **Filtering**: Usually your best option, if possible, is to break down
    your documentation into subsets of the tables in your database, thereby
    getting fairly responsive page load times, but with uniform sizing of
    elements in your diagrams.
