# db-diagram

[![test](https://github.com/enorganic/db-diagram/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/enorganic/db-diagram/actions/workflows/test.yml)
[![PyPI version](https://badge.fury.io/py/db-diagram.svg?icon=si%3Apython)](https://badge.fury.io/py/db-diagram)

This package provides a CLI and library for generating
[Mermaid Entity Relationship Diagrams
](https://mermaid.js.org/syntax/entityRelationshipDiagram.html)
based on an existing database [connection URL
](https://docs.sqlalchemy.org/en/20/core/engines.html#database-urls) and/or
[SQLAlchemy metadata.
](https://docs.sqlalchemy.org/en/20/core/metadata.html)

```mermaid
erDiagram
    ab_group_role {
        INTEGER id PK
        INTEGER group_id FK
        INTEGER role_id FK
    }
    ab_group_role }o--|| ab_group : "group_id:id"
    ab_group_role }o--|| ab_role : "role_id:id"
    ab_group {
        INTEGER id PK
        VARCHAR name
        VARCHAR label
        VARCHAR description
    }
    ab_user_group {
        INTEGER id PK
        INTEGER user_id FK
        INTEGER group_id FK
    }
    ab_user_group }o--|| ab_group : "group_id:id"
    ab_role {
        INTEGER id PK
        VARCHAR name
    }
    ab_permission_view_role {
        INTEGER id PK
        INTEGER permission_view_id FK
        INTEGER role_id FK
    }
    ab_permission_view_role }o--|| ab_role : "role_id:id"
    ab_user_role {
        INTEGER id PK
        INTEGER user_id FK
        INTEGER role_id FK
    }
    ab_user_role }o--|| ab_role : "role_id:id"
```

## Installation

You can install `db-diagram` with pip:

```shell
pip3 install db-diagram
```

## Usage

You can utilize `db-diagram` as a
[CLI](https://db-diagram.enorganic.or/cli/) (from a shell or command prompt),
or as a [python library](https://db-diagram.enorganic.or/api/)
(`from db_diagram import write_markdown`).
The CLI will be more convenient under most circumstances, however
if you want to generate diagrams from [SQLAlchemy metadata
](https://docs.sqlalchemy.org/en/20/core/metadata.html) rather than
a connection URL, such as you might for a
[SQLAlchemy ORM](https://docs.sqlalchemy.org/en/latest/orm/),
you will want to use `db_diagram` as a python library.
Pease refer to [these examples](https://db-diagram.enorganic.or/examples/)
for reference concerning output.

