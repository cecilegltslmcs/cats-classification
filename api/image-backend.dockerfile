FROM python:3.12-slim@sha256:c127a8c4aca8a5d3ac3a333cbab4c082c7ddbd0891441cc4e30d88dc351f1ce5

EXPOSE 8000

WORKDIR /app

COPY ["backend.py", "proto.py", "requirements-backend.txt", "./"]

RUN apt-get update \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements-backend.txt

CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8000"]
