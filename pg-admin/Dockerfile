# Use the official Python image as a base
FROM python:3.9-slim

# Install PostgreSQL and other dependencies
RUN apt-get update && apt-get install -y \
    postgresql postgresql-contrib libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies (psycopg2 for PostgreSQL)
RUN pip install psycopg2-binary

# Expose PostgreSQL port
EXPOSE 5432

# Set the default command to run PostgreSQL and Python script
CMD service postgresql start && \
    psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" && \
    createdb -O docker docker && \
    python /app/db_script.py
