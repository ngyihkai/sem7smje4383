FROM python:3.9

WORKDIR /fastapi-app

COPY requirement.txt .

RUN pip install -r requirement.txt

COPY ./app ./app

CMD ["python", "./app/main.py"]