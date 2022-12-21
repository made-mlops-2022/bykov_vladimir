FROM python:3.10-slim-bullseye


COPY server.py enities.py model_rf.pkl requirements.txt ./online_inference/
WORKDIR /online_inference
RUN python3 -m pip install --upgrade pip \
  &&  pip3 install -r requirements.txt

ENV PATH_TO_MODEL="./model_rf.pkl"
CMD ["python3", "server.py"]

