FROM python:3.7-alpine

RUN pip install pytest httpx

COPY . /action

ENTRYPOINT ["python", "/action/run_test.py"]