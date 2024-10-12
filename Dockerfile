FROM python:3.11-slim-bookworm

RUN apt-get update && apt-get install -y \
    libpq-dev gcc python3 python3-pip

RUN pip3 install --upgrade pip

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN rm -rf /tmp/requirements.txt 

COPY app/ /app

ENTRYPOINT [ "sh", "run.sh" ]
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
