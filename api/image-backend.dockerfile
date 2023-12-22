FROM python:3.11.6-slim@sha256:eb7a9f47cd21f68c04356a841389326a9cefccdd2dbf53ed788b133641af5aa4

EXPOSE 8000

WORKDIR /app

COPY ["backend.py", "proto.py", "requirements-backend.txt", "./"]

RUN apt-get update \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements-backend.txt

CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8000"]
