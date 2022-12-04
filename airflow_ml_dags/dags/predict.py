from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime
from docker.types import Mount
from airflow.models import Variable

PATH_TO_MODEL = Variable.get("path_to_model")

default_args = {
    "owner": "vladimir",
    "email": "v.bykov.02@bk.ru",
    "retries": 1
}


with DAG(
    "predict",
    default_args=default_args,
    schedule_interval="@daily",
    start_date=datetime(2022, 12, 1)
) as dag:

    predict = DockerOperator(
            image="airflow-predict",
            command="--input-path ./data/processed/{{ ds }} --model-path " + PATH_TO_MODEL + " --output-path ./data/predictions/{{ ds }}",
            task_id = "predict",
            do_xcom_push=False,
            auto_remove=True,
            network_mode="bridge",
            mounts=[Mount(source="/home/vladimir/PycharmProjects/airflow_ml_dags/data", target='/data', type='bind')]
    )

    predict

