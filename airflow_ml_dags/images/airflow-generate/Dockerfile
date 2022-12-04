FROM python:3.10-slim-bullseye
COPY generate.py requirements.txt ./
RUN python3 -m pip install --upgrade pip \
  && pip3 install -r requirements.txt
WORKDIR ./
ENTRYPOINT ["python3", "generate.py"]


