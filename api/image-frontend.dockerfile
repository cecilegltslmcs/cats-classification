FROM python:3.11.6-slim@sha256:eb7a9f47cd21f68c04356a841389326a9cefccdd2dbf53ed788b133641af5aa4

EXPOSE 8501

WORKDIR /code

COPY ["requirements-frontend.txt", "frontend.py", "./"]

RUN apt-get update \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements-frontend.txt

ENTRYPOINT ["streamlit", "run", "frontend.py", "--server.port=8501", "--server.address=0.0.0.0"]
