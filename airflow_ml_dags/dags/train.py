from airflow.providers.docker.operators.docker import DockerOperator
from airflow import DAG
from datetime import datetime
from docker.types import Mount

default_args = {
    "owner": "vladimir",
    "email": "v.bykov.02@bk.ru",
    "retries": 1
}


with DAG(
    "train",
    default_args=default_args,
    schedule_interval="@daily",
    start_date=datetime(2022, 12, 1)
) as dag:

    process = DockerOperator(
        image="airflow-process",
        command="--input-path ./data/raw/{{ ds }} --output-path ./data/processed/{{ ds }}",
        task_id = "process",
        do_xcom_push=False,
        auto_remove=True,
        network_mode="bridge",
        mounts=[Mount(source="/home/vladimir/PycharmProjects/airflow_ml_dags/data", target='/data', type='bind')]

    )
    
    split = DockerOperator(
        image="airflow-split",
        command="--input-path ./data/processed/{{ ds }} --output-path ./data/train-val/{{ ds }}",
        task_id = "split",
        do_xcom_push=False,
        auto_remove=True,
        network_mode="bridge",
        mounts=[Mount(source="/home/vladimir/PycharmProjects/airflow_ml_dags/data", target='/data', type='bind')]

    )

    train = DockerOperator(
        image="airflow-train",
        command="--input-path ./data/train-val/{{ ds }} --output-path ./data/models/{{ ds }}",
        task_id = "train",
        do_xcom_push=False,
        auto_remove=True,
        network_mode="bridge",
        mounts=[Mount(source="/home/vladimir/PycharmProjects/airflow_ml_dags/data", target='/data', type='bind')]
    )

    validate = DockerOperator(
        image="airflow-validate",
        command="--input-path ./data/train-val/{{ ds }} --model-path ./data/models/{{ ds }} --output-path ./data/metrics/{{ ds }}",
        task_id = "validate",
        do_xcom_push=False,
        auto_remove=True,
        network_mode="bridge",
        mounts=[Mount(source="/home/vladimir/PycharmProjects/airflow_ml_dags/data", target='/data', type='bind')]
    )

    process >> split >> train >> validate
