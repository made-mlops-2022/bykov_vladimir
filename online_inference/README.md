HOMEWORK 2
Online Inference

Start:
~~~
cd online_inference
~~~
With docker:

~~~
docker build -t online_inference .
docker run -p 8000:8000 ml_project/online_inference
~~~

or
~~~
docker pull bykoff/online_inference:v5
docker run -p 8000:8000 ml_project/online_inference:v5
~~~


With python3:
~~~
python3 server.py
~~~

With uvicorn:
~~~
uvicorn server:app --host 0.0.0.0 --port 8000
~~~
