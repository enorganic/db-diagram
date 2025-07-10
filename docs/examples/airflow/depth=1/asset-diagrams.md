# Airflow asset_* PostgreSQL Database Diagrams

## asset_active

```mermaid
erDiagram
    asset_active {
        VARCHAR name PK, FK
        VARCHAR uri PK, FK
    }
    asset_active }o--|| asset : "name, uri"
    asset {
        INTEGER id PK
        VARCHAR name
        VARCHAR uri
        VARCHAR group
        JSON extra
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }
```

## asset_alias

```mermaid
erDiagram
    asset_alias {
        INTEGER id PK
        VARCHAR name
        VARCHAR group
    }
    asset_alias_asset {
        INTEGER alias_id PK, FK
        INTEGER asset_id PK, FK
    }
    asset_alias_asset }o--|| asset_alias : "alias_id:id"
    asset_alias_asset_event {
        INTEGER alias_id PK, FK
        INTEGER event_id PK, FK
    }
    asset_alias_asset_event }o--|| asset_alias : "alias_id:id"
    dag_schedule_asset_alias_reference {
        INTEGER alias_id PK, FK
        VARCHAR dag_id PK, FK
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }
    dag_schedule_asset_alias_reference }o--|| asset_alias : "alias_id:id"
```

## asset_alias_asset

```mermaid
erDiagram
    asset_alias_asset {
        INTEGER alias_id PK, FK
        INTEGER asset_id PK, FK
    }
    asset_alias_asset }o--|| asset : "asset_id:id"
    asset_alias_asset }o--|| asset_alias : "alias_id:id"
    asset {
        INTEGER id PK
        VARCHAR name
        VARCHAR uri
        VARCHAR group
        JSON extra
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }
    asset_alias {
        INTEGER id PK
        VARCHAR name
        VARCHAR group
    }
```

## asset_alias_asset_event

```mermaid
erDiagram
    asset_alias_asset_event {
        INTEGER alias_id PK, FK
        INTEGER event_id PK, FK
    }
    asset_alias_asset_event }o--|| asset_alias : "alias_id:id"
    asset_alias_asset_event }o--|| asset_event : "event_id:id"
    asset_alias {
        INTEGER id PK
        VARCHAR name
        VARCHAR group
    }
    asset_event {
        INTEGER id PK
        INTEGER asset_id
        JSON extra
        VARCHAR source_task_id
        VARCHAR source_dag_id
        VARCHAR source_run_id
        INTEGER source_map_index
        TIMESTAMP timestamp
    }
```

## asset_dag_run_queue

```mermaid
erDiagram
    asset_dag_run_queue {
        INTEGER asset_id PK, FK
        VARCHAR target_dag_id PK, FK
        TIMESTAMP created_at
    }
    asset_dag_run_queue }o--|| asset : "asset_id:id"
    asset_dag_run_queue }o--|| dag : "target_dag_id:dag_id"
    asset {
        INTEGER id PK
        VARCHAR name
        VARCHAR uri
        VARCHAR group
        JSON extra
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }
    dag {
        VARCHAR dag_id PK
        BOOLEAN is_paused
        BOOLEAN is_stale
        TIMESTAMP last_parsed_time
        TIMESTAMP last_expired
        VARCHAR fileloc
        VARCHAR relative_fileloc
        VARCHAR bundle_name FK
        VARCHAR bundle_version
        VARCHAR owners
        VARCHAR dag_display_name
        TEXT description
        TEXT timetable_summary
        VARCHAR timetable_description
        JSON asset_expression
        INTEGER max_active_tasks
        INTEGER max_active_runs
        INTEGER max_consecutive_failed_dag_runs
        BOOLEAN has_task_concurrency_limits
        BOOLEAN has_import_errors
        TIMESTAMP next_dagrun
        TIMESTAMP next_dagrun_data_interval_start
        TIMESTAMP next_dagrun_data_interval_end
        TIMESTAMP next_dagrun_create_after
    }
```

## asset_event

```mermaid
erDiagram
    asset_event {
        INTEGER id PK
        INTEGER asset_id
        JSON extra
        VARCHAR source_task_id
        VARCHAR source_dag_id
        VARCHAR source_run_id
        INTEGER source_map_index
        TIMESTAMP timestamp
    }
    asset_alias_asset_event {
        INTEGER alias_id PK, FK
        INTEGER event_id PK, FK
    }
    asset_alias_asset_event }o--|| asset_event : "event_id:id"
    dagrun_asset_event {
        INTEGER dag_run_id PK, FK
        INTEGER event_id PK, FK
    }
    dagrun_asset_event }o--|| asset_event : "event_id:id"
```

## asset_trigger

```mermaid
erDiagram
    asset_trigger {
        INTEGER asset_id PK, FK
        INTEGER trigger_id PK, FK
    }
    asset_trigger }o--|| asset : "asset_id:id"
    asset_trigger }o--|| trigger : "trigger_id:id"
    asset {
        INTEGER id PK
        VARCHAR name
        VARCHAR uri
        VARCHAR group
        JSON extra
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }
    trigger {
        INTEGER id PK
        VARCHAR classpath
        TEXT kwargs
        TIMESTAMP created_date
        INTEGER triggerer_id
    }
```
