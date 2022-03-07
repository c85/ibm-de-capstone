# import the libraries
from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

#defining DAG arguments
default_args = {
    'owner': 'Christopher Martin',
    'start_date': days_ago(0),
    'email': ['ccmartin@gmail.com']
}

# defining the DAG
dag = DAG(
    'process_web_log',
    default_args=default_args,
    description='Process Web Log',
    schedule_interval=timedelta(days=1),
)

# define the tasks

# define extract_data
extract_data = BashOperator(
    task_id='extract_data',
    bash_command='grep -o ' + '\'[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\'' + ' /home/project/airflow/dags/capstone/accesslog.txt > /home/project/airflow/dags/capstone/extracted-data.txt',
    dag=dag,
)

# define transform_data
transform_data = BashOperator(
    task_id='transform_data',
    bash_command='grep -v ' + '\'^198\.46\.149\.143\'' + ' /home/project/airflow/dags/capstone/extracted-data.txt > /home/project/airflow/dags/capstone/transformed-data.csv',
    dag=dag,
)

# define load_data
load_data = BashOperator(
    task_id='load_data',
    bash_command='tar -czvf /home/project/airflow/dags/capstone/weblog.tar.gz /home/project/airflow/dags/capstone/transformed-data.csv' ,
    dag=dag,
)

# task pipeline
extract_data >> transform_data >> load_data