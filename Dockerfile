FROM python:3.6

WORKDIR /app/

COPY setup.py requirements.txt /app/

RUN pip install --no-cache-dir -e .

COPY src /app/src