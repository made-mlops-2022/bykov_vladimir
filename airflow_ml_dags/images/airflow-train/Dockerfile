FROM python:3.10-slim-bullseye
COPY train.py requirements.txt ./
RUN python3 -m pip install --upgrade pip \
  && pip3 install -r requirements.txt
ENTRYPOINT ["python3", "train.py"]

