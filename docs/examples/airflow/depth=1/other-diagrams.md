# Airflow (other) PostgreSQL Database Diagrams

## alembic_version

```mermaid
erDiagram
    alembic_version {
        VARCHAR version_num PK
    }
```

## alembic_version_fab

```mermaid
erDiagram
    alembic_version_fab {
        VARCHAR version_num PK
    }
```

## asset

```mermaid
erDiagram
    asset {
        INTEGER id PK
        VARCHAR name
        VARCHAR uri
        VARCHAR group
        JSON extra
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }
    asset_active {
        VARCHAR name PK, FK
        VARCHAR uri PK, FK
    }
    asset_active }o--|| asset : "name, uri"
    asset_alias_asset {
        INTEGER alias_id PK, FK
        INTEGER asset_id PK, FK
    }
    asset_alias_asset }o--|| asset : "asset_id:id"
    asset_dag_run_queue {
        INTEGER asset_id PK, FK
        VARCHAR target_dag_id PK, FK
        TIMESTAMP created_at
    }
    asset_dag_run_queue }o--|| asset : "asset_id:id"
    asset_trigger {
        INTEGER asset_id PK, FK
        INTEGER trigger_id PK, FK
    }
    asset_trigger }o--|| asset : "asset_id:id"
    dag_schedule_asset_reference {
        INTEGER asset_id PK, FK
        VARCHAR dag_id PK, FK
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }
    dag_schedule_asset_reference }o--|| asset : "asset_id:id"
    task_outlet_asset_reference {
        INTEGER asset_id PK, FK
        VARCHAR dag_id PK, FK
        VARCHAR task_id PK
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }
    task_outlet_asset_reference }o--|| asset : "asset_id:id"
```

## backfill

```mermaid
erDiagram
    backfill {
        INTEGER id PK
        VARCHAR dag_id
        TIMESTAMP from_date
        TIMESTAMP to_date
        JSON dag_run_conf
        BOOLEAN is_paused
        VARCHAR reprocess_behavior
        INTEGER max_active_runs
        TIMESTAMP created_at
        TIMESTAMP completed_at
        TIMESTAMP updated_at
    }
    backfill_dag_run {
        INTEGER id PK
        INTEGER backfill_id FK
        INTEGER dag_run_id FK
        VARCHAR exception_reason
        TIMESTAMP logical_date
        INTEGER sort_ordinal
    }
    backfill_dag_run }o--|| backfill : "backfill_id:id"
    backfill_dag_run }o--|| dag_run : "dag_run_id:id"
    dag_run {
        INTEGER id PK
        VARCHAR dag_id
        TIMESTAMP queued_at
        TIMESTAMP logical_date
        TIMESTAMP start_date
        TIMESTAMP end_date
        VARCHAR state
        VARCHAR run_id
        INTEGER creating_job_id
        VARCHAR run_type
        VARCHAR triggered_by
        JSONB conf
        TIMESTAMP data_interval_start
        TIMESTAMP data_interval_end
        TIMESTAMP run_after
        TIMESTAMP last_scheduling_decision
        INTEGER log_template_id FK
        TIMESTAMP updated_at
        INTEGER clear_number
        INTEGER backfill_id FK
        VARCHAR bundle_version
        INTEGER scheduled_by_job_id
        JSONB context_carrier
        VARCHAR span_status
        UUID created_dag_version_id FK
    }
    dag_run }o--|| backfill : "backfill_id:id"
```

## backfill_dag_run

```mermaid
erDiagram
    backfill_dag_run {
        INTEGER id PK
        INTEGER backfill_id FK
        INTEGER dag_run_id FK
        VARCHAR exception_reason
        TIMESTAMP logical_date
        INTEGER sort_ordinal
    }
    backfill_dag_run }o--|| backfill : "backfill_id:id"
    backfill_dag_run }o--|| dag_run : "dag_run_id:id"
    backfill {
        INTEGER id PK
        VARCHAR dag_id
        TIMESTAMP from_date
        TIMESTAMP to_date
        JSON dag_run_conf
        BOOLEAN is_paused
        VARCHAR reprocess_behavior
        INTEGER max_active_runs
        TIMESTAMP created_at
        TIMESTAMP completed_at
        TIMESTAMP updated_at
    }
    dag_run {
        INTEGER id PK
        VARCHAR dag_id
        TIMESTAMP queued_at
        TIMESTAMP logical_date
        TIMESTAMP start_date
        TIMESTAMP end_date
        VARCHAR state
        VARCHAR run_id
        INTEGER creating_job_id
        VARCHAR run_type
        VARCHAR triggered_by
        JSONB conf
        TIMESTAMP data_interval_start
        TIMESTAMP data_interval_end
        TIMESTAMP run_after
        TIMESTAMP last_scheduling_decision
        INTEGER log_template_id FK
        TIMESTAMP updated_at
        INTEGER clear_number
        INTEGER backfill_id FK
        VARCHAR bundle_version
        INTEGER scheduled_by_job_id
        JSONB context_carrier
        VARCHAR span_status
        UUID created_dag_version_id FK
    }
    dag_run }o--|| backfill : "backfill_id:id"
```

## callback_request

```mermaid
erDiagram
    callback_request {
        INTEGER id PK
        TIMESTAMP created_at
        INTEGER priority_weight
        JSONB callback_data
        VARCHAR callback_type
    }
```

## celery_taskmeta

```mermaid
erDiagram
    celery_taskmeta {
        INTEGER id PK
        VARCHAR task_id
        VARCHAR status
        BYTEA result
        TIMESTAMP date_done
        TEXT traceback
        VARCHAR name
        BYTEA args
        BYTEA kwargs
        VARCHAR worker
        INTEGER retries
        VARCHAR queue
    }
```

## celery_tasksetmeta

```mermaid
erDiagram
    celery_tasksetmeta {
        INTEGER id PK
        VARCHAR taskset_id
        BYTEA result
        TIMESTAMP date_done
    }
```

## connection

```mermaid
erDiagram
    connection {
        INTEGER id PK
        VARCHAR conn_id
        VARCHAR conn_type
        TEXT description
        VARCHAR host
        VARCHAR schema
        TEXT login
        TEXT password
        INTEGER port
        BOOLEAN is_encrypted
        BOOLEAN is_extra_encrypted
        TEXT extra
    }
```

## dagrun_asset_event

```mermaid
erDiagram
    dagrun_asset_event {
        INTEGER dag_run_id PK, FK
        INTEGER event_id PK, FK
    }
    dagrun_asset_event }o--|| asset_event : "event_id:id"
    dagrun_asset_event }o--|| dag_run : "dag_run_id:id"
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
    dag_run {
        INTEGER id PK
        VARCHAR dag_id
        TIMESTAMP queued_at
        TIMESTAMP logical_date
        TIMESTAMP start_date
        TIMESTAMP end_date
        VARCHAR state
        VARCHAR run_id
        INTEGER creating_job_id
        VARCHAR run_type
        VARCHAR triggered_by
        JSONB conf
        TIMESTAMP data_interval_start
        TIMESTAMP data_interval_end
        TIMESTAMP run_after
        TIMESTAMP last_scheduling_decision
        INTEGER log_template_id FK
        TIMESTAMP updated_at
        INTEGER clear_number
        INTEGER backfill_id FK
        VARCHAR bundle_version
        INTEGER scheduled_by_job_id
        JSONB context_carrier
        VARCHAR span_status
        UUID created_dag_version_id FK
    }
```

## deadline

```mermaid
erDiagram
    deadline {
        UUID id PK
        VARCHAR dag_id FK
        INTEGER dagrun_id FK
        TIMESTAMP deadline
        VARCHAR callback
        JSON callback_kwargs
    }
    deadline }o--|| dag : "dag_id"
    deadline }o--|| dag_run : "dagrun_id:id"
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
    dag_run {
        INTEGER id PK
        VARCHAR dag_id
        TIMESTAMP queued_at
        TIMESTAMP logical_date
        TIMESTAMP start_date
        TIMESTAMP end_date
        VARCHAR state
        VARCHAR run_id
        INTEGER creating_job_id
        VARCHAR run_type
        VARCHAR triggered_by
        JSONB conf
        TIMESTAMP data_interval_start
        TIMESTAMP data_interval_end
        TIMESTAMP run_after
        TIMESTAMP last_scheduling_decision
        INTEGER log_template_id FK
        TIMESTAMP updated_at
        INTEGER clear_number
        INTEGER backfill_id FK
        VARCHAR bundle_version
        INTEGER scheduled_by_job_id
        JSONB context_carrier
        VARCHAR span_status
        UUID created_dag_version_id FK
    }
```

## import_error

```mermaid
erDiagram
    import_error {
        INTEGER id PK
        TIMESTAMP timestamp
        VARCHAR filename
        VARCHAR bundle_name
        TEXT stacktrace
    }
```

## job

```mermaid
erDiagram
    job {
        INTEGER id PK
        VARCHAR dag_id
        VARCHAR state
        VARCHAR job_type
        TIMESTAMP start_date
        TIMESTAMP end_date
        TIMESTAMP latest_heartbeat
        VARCHAR executor_class
        VARCHAR hostname
        VARCHAR unixname
    }
```

## log

```mermaid
erDiagram
    log {
        INTEGER id PK
        TIMESTAMP dttm
        VARCHAR dag_id
        VARCHAR task_id
        INTEGER map_index
        VARCHAR event
        TIMESTAMP logical_date
        VARCHAR run_id
        VARCHAR owner
        VARCHAR owner_display_name
        TEXT extra
        INTEGER try_number
    }
```

## log_template

```mermaid
erDiagram
    log_template {
        INTEGER id PK
        TEXT filename
        TEXT elasticsearch_id
        TIMESTAMP created_at
    }
    dag_run {
        INTEGER id PK
        VARCHAR dag_id
        TIMESTAMP queued_at
        TIMESTAMP logical_date
        TIMESTAMP start_date
        TIMESTAMP end_date
        VARCHAR state
        VARCHAR run_id
        INTEGER creating_job_id
        VARCHAR run_type
        VARCHAR triggered_by
        JSONB conf
        TIMESTAMP data_interval_start
        TIMESTAMP data_interval_end
        TIMESTAMP run_after
        TIMESTAMP last_scheduling_decision
        INTEGER log_template_id FK
        TIMESTAMP updated_at
        INTEGER clear_number
        INTEGER backfill_id FK
        VARCHAR bundle_version
        INTEGER scheduled_by_job_id
        JSONB context_carrier
        VARCHAR span_status
        UUID created_dag_version_id FK
    }
    dag_run }o--|| log_template : "log_template_id:id"
```

## rendered_task_instance_fields

```mermaid
erDiagram
    rendered_task_instance_fields {
        VARCHAR dag_id PK, FK
        VARCHAR task_id PK, FK
        VARCHAR run_id PK, FK
        INTEGER map_index PK, FK
        JSON rendered_fields
        JSON k8s_pod_yaml
    }
    rendered_task_instance_fields }o--|| task_instance : "dag_id, task_id, run_id, map_index"
    task_instance {
        UUID id PK
        VARCHAR task_id
        VARCHAR dag_id FK
        VARCHAR run_id FK
        INTEGER map_index
        TIMESTAMP start_date
        TIMESTAMP end_date
        DOUBLE_PRECISION duration
        VARCHAR state
        INTEGER try_number
        INTEGER max_tries
        VARCHAR hostname
        VARCHAR unixname
        VARCHAR pool
        INTEGER pool_slots
        VARCHAR queue
        INTEGER priority_weight
        VARCHAR operator
        VARCHAR custom_operator_name
        TIMESTAMP queued_dttm
        TIMESTAMP scheduled_dttm
        INTEGER queued_by_job_id
        TIMESTAMP last_heartbeat_at
        INTEGER pid
        VARCHAR executor
        BYTEA executor_config
        TIMESTAMP updated_at
        VARCHAR rendered_map_index
        JSONB context_carrier
        VARCHAR span_status
        VARCHAR external_executor_id
        INTEGER trigger_id FK
        TIMESTAMP trigger_timeout
        VARCHAR next_method
        JSONB next_kwargs
        VARCHAR task_display_name
        UUID dag_version_id FK
    }
```

## serialized_dag

```mermaid
erDiagram
    serialized_dag {
        UUID id PK
        VARCHAR dag_id
        JSON data
        BYTEA data_compressed
        TIMESTAMP created_at
        TIMESTAMP last_updated
        VARCHAR dag_hash
        UUID dag_version_id FK
    }
    serialized_dag }o--|| dag_version : "dag_version_id:id"
    dag_version {
        UUID id PK
        INTEGER version_number
        VARCHAR dag_id FK
        VARCHAR bundle_name
        VARCHAR bundle_version
        TIMESTAMP created_at
        TIMESTAMP last_updated
    }
```

## session

```mermaid
erDiagram
    session {
        INTEGER id PK
        VARCHAR session_id
        BYTEA data
        TIMESTAMP expiry
    }
```

## slot_pool

```mermaid
erDiagram
    slot_pool {
        INTEGER id PK
        VARCHAR pool
        INTEGER slots
        TEXT description
        BOOLEAN include_deferred
    }
```

## trigger

```mermaid
erDiagram
    trigger {
        INTEGER id PK
        VARCHAR classpath
        TEXT kwargs
        TIMESTAMP created_date
        INTEGER triggerer_id
    }
    asset_trigger {
        INTEGER asset_id PK, FK
        INTEGER trigger_id PK, FK
    }
    asset_trigger }o--|| trigger : "trigger_id:id"
    task_instance {
        UUID id PK
        VARCHAR task_id
        VARCHAR dag_id FK
        VARCHAR run_id FK
        INTEGER map_index
        TIMESTAMP start_date
        TIMESTAMP end_date
        DOUBLE_PRECISION duration
        VARCHAR state
        INTEGER try_number
        INTEGER max_tries
        VARCHAR hostname
        VARCHAR unixname
        VARCHAR pool
        INTEGER pool_slots
        VARCHAR queue
        INTEGER priority_weight
        VARCHAR operator
        VARCHAR custom_operator_name
        TIMESTAMP queued_dttm
        TIMESTAMP scheduled_dttm
        INTEGER queued_by_job_id
        TIMESTAMP last_heartbeat_at
        INTEGER pid
        VARCHAR executor
        BYTEA executor_config
        TIMESTAMP updated_at
        VARCHAR rendered_map_index
        JSONB context_carrier
        VARCHAR span_status
        VARCHAR external_executor_id
        INTEGER trigger_id FK
        TIMESTAMP trigger_timeout
        VARCHAR next_method
        JSONB next_kwargs
        VARCHAR task_display_name
        UUID dag_version_id FK
    }
    task_instance }o--|| trigger : "trigger_id:id"
```

## variable

```mermaid
erDiagram
    variable {
        INTEGER id PK
        VARCHAR key
        TEXT val
        TEXT description
        BOOLEAN is_encrypted
    }
```

## xcom

```mermaid
erDiagram
    xcom {
        INTEGER dag_run_id PK
        VARCHAR task_id PK, FK
        INTEGER map_index PK, FK
        VARCHAR key PK
        VARCHAR dag_id FK
        VARCHAR run_id FK
        JSONB value
        TIMESTAMP timestamp
    }
    xcom }o--|| task_instance : "dag_id, task_id, run_id, map_index"
    task_instance {
        UUID id PK
        VARCHAR task_id
        VARCHAR dag_id FK
        VARCHAR run_id FK
        INTEGER map_index
        TIMESTAMP start_date
        TIMESTAMP end_date
        DOUBLE_PRECISION duration
        VARCHAR state
        INTEGER try_number
        INTEGER max_tries
        VARCHAR hostname
        VARCHAR unixname
        VARCHAR pool
        INTEGER pool_slots
        VARCHAR queue
        INTEGER priority_weight
        VARCHAR operator
        VARCHAR custom_operator_name
        TIMESTAMP queued_dttm
        TIMESTAMP scheduled_dttm
        INTEGER queued_by_job_id
        TIMESTAMP last_heartbeat_at
        INTEGER pid
        VARCHAR executor
        BYTEA executor_config
        TIMESTAMP updated_at
        VARCHAR rendered_map_index
        JSONB context_carrier
        VARCHAR span_status
        VARCHAR external_executor_id
        INTEGER trigger_id FK
        TIMESTAMP trigger_timeout
        VARCHAR next_method
        JSONB next_kwargs
        VARCHAR task_display_name
        UUID dag_version_id FK
    }
```
