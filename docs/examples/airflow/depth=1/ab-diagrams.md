# Airflow ab_* PostgreSQL Database Diagrams

## ab_group

```mermaid
erDiagram
    ab_group {
        INTEGER id PK
        VARCHAR name
        VARCHAR label
        VARCHAR description
    }
    ab_group_role {
        INTEGER id PK
        INTEGER group_id FK
        INTEGER role_id FK
    }
    ab_group_role }o--|| ab_group : "group_id:id"
    ab_user_group {
        INTEGER id PK
        INTEGER user_id FK
        INTEGER group_id FK
    }
    ab_user_group }o--|| ab_group : "group_id:id"
```

## ab_group_role

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
    ab_role {
        INTEGER id PK
        VARCHAR name
    }
```

## ab_permission

```mermaid
erDiagram
    ab_permission {
        INTEGER id PK
        VARCHAR name
    }
    ab_permission_view {
        INTEGER id PK
        INTEGER permission_id FK
        INTEGER view_menu_id FK
    }
    ab_permission_view }o--|| ab_permission : "permission_id:id"
```

## ab_permission_view

```mermaid
erDiagram
    ab_permission_view {
        INTEGER id PK
        INTEGER permission_id FK
        INTEGER view_menu_id FK
    }
    ab_permission_view }o--|| ab_permission : "permission_id:id"
    ab_permission_view }o--|| ab_view_menu : "view_menu_id:id"
    ab_permission {
        INTEGER id PK
        VARCHAR name
    }
    ab_permission_view_role {
        INTEGER id PK
        INTEGER permission_view_id FK
        INTEGER role_id FK
    }
    ab_permission_view_role }o--|| ab_permission_view : "permission_view_id:id"
    ab_view_menu {
        INTEGER id PK
        VARCHAR name
    }
```

## ab_permission_view_role

```mermaid
erDiagram
    ab_permission_view_role {
        INTEGER id PK
        INTEGER permission_view_id FK
        INTEGER role_id FK
    }
    ab_permission_view_role }o--|| ab_permission_view : "permission_view_id:id"
    ab_permission_view_role }o--|| ab_role : "role_id:id"
    ab_permission_view {
        INTEGER id PK
        INTEGER permission_id FK
        INTEGER view_menu_id FK
    }
    ab_role {
        INTEGER id PK
        VARCHAR name
    }
```

## ab_register_user

```mermaid
erDiagram
    ab_register_user {
        INTEGER id PK
        VARCHAR first_name
        VARCHAR last_name
        VARCHAR username
        VARCHAR password
        VARCHAR email
        TIMESTAMP registration_date
        VARCHAR registration_hash
    }
```

## ab_role

```mermaid
erDiagram
    ab_role {
        INTEGER id PK
        VARCHAR name
    }
    ab_group_role {
        INTEGER id PK
        INTEGER group_id FK
        INTEGER role_id FK
    }
    ab_group_role }o--|| ab_role : "role_id:id"
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

## ab_user

```mermaid
erDiagram
    ab_user {
        INTEGER id PK
        VARCHAR first_name
        VARCHAR last_name
        VARCHAR username
        VARCHAR password
        BOOLEAN active
        VARCHAR email
        TIMESTAMP last_login
        INTEGER login_count
        INTEGER fail_login_count
        TIMESTAMP created_on
        TIMESTAMP changed_on
        INTEGER created_by_fk FK
        INTEGER changed_by_fk FK
    }
    ab_user }o--|| ab_user : "changed_by_fk:id"
    ab_user }o--|| ab_user : "created_by_fk:id"
    ab_user_group {
        INTEGER id PK
        INTEGER user_id FK
        INTEGER group_id FK
    }
    ab_user_group }o--|| ab_user : "user_id:id"
    ab_user_role {
        INTEGER id PK
        INTEGER user_id FK
        INTEGER role_id FK
    }
    ab_user_role }o--|| ab_user : "user_id:id"
```

## ab_user_group

```mermaid
erDiagram
    ab_user_group {
        INTEGER id PK
        INTEGER user_id FK
        INTEGER group_id FK
    }
    ab_user_group }o--|| ab_group : "group_id:id"
    ab_user_group }o--|| ab_user : "user_id:id"
    ab_group {
        INTEGER id PK
        VARCHAR name
        VARCHAR label
        VARCHAR description
    }
    ab_user {
        INTEGER id PK
        VARCHAR first_name
        VARCHAR last_name
        VARCHAR username
        VARCHAR password
        BOOLEAN active
        VARCHAR email
        TIMESTAMP last_login
        INTEGER login_count
        INTEGER fail_login_count
        TIMESTAMP created_on
        TIMESTAMP changed_on
        INTEGER created_by_fk FK
        INTEGER changed_by_fk FK
    }
    ab_user }o--|| ab_user : "changed_by_fk:id"
    ab_user }o--|| ab_user : "created_by_fk:id"
```

## ab_user_role

```mermaid
erDiagram
    ab_user_role {
        INTEGER id PK
        INTEGER user_id FK
        INTEGER role_id FK
    }
    ab_user_role }o--|| ab_role : "role_id:id"
    ab_user_role }o--|| ab_user : "user_id:id"
    ab_role {
        INTEGER id PK
        VARCHAR name
    }
    ab_user {
        INTEGER id PK
        VARCHAR first_name
        VARCHAR last_name
        VARCHAR username
        VARCHAR password
        BOOLEAN active
        VARCHAR email
        TIMESTAMP last_login
        INTEGER login_count
        INTEGER fail_login_count
        TIMESTAMP created_on
        TIMESTAMP changed_on
        INTEGER created_by_fk FK
        INTEGER changed_by_fk FK
    }
    ab_user }o--|| ab_user : "changed_by_fk:id"
    ab_user }o--|| ab_user : "created_by_fk:id"
```

## ab_view_menu

```mermaid
erDiagram
    ab_view_menu {
        INTEGER id PK
        VARCHAR name
    }
    ab_permission_view {
        INTEGER id PK
        INTEGER permission_id FK
        INTEGER view_menu_id FK
    }
    ab_permission_view }o--|| ab_view_menu : "view_menu_id:id"
```
