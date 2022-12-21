# HOMEWORK 3

Run:
~~~
#insert your date to PATH_TO_MODEL
export PATH_TO_MODEL=./data/models/2022-12-04
export FERNET_KEY=$(python3 -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")
docker compose up --build
~~~
