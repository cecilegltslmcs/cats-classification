FROM python:3.12-slim@sha256:c127a8c4aca8a5d3ac3a333cbab4c082c7ddbd0891441cc4e30d88dc351f1ce5

EXPOSE 8501

WORKDIR /code

COPY ["requirements-frontend.txt", "frontend.py", "./"]

RUN apt-get update \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements-frontend.txt

ENTRYPOINT ["streamlit", "run", "frontend.py", "--server.port=8501", "--server.address=0.0.0.0"]
