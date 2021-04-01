FROM python:3.6

WORKDIR /app/

COPY alembic.ini requirements.txt setup.py /app/

RUN pip install --no-cache-dir -e .

COPY migrations /app/migrations
COPY src /app/src