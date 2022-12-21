FROM python:3.10-slim-bullseye
COPY predict.py requirements.txt ./
RUN python3 -m pip install --upgrade pip \
  && pip3 install -r requirements.txt
ENTRYPOINT ["python3", "predict.py"]

