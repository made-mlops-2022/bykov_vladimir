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
    "generate",
    default_args=default_args,
    schedule_interval="@daily",
    start_date=datetime(2022, 12, 1)
) as dag:
    generate = DockerOperator(
        image="airflow-generate",
        command="--output_path ./data/raw/{{ ds }}",
        task_id = "generate_synthetic_data",
        do_xcom_push=False,
        auto_remove=True,
        network_mode="bridge",
        mounts=[Mount(source="/home/vladimir/PycharmProjects/airflow_ml_dags/data", target='/data', type='bind')]
    )

    generate
