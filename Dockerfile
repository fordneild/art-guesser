FROM postgres:12 as db
WORKDIR /app
# Copy over the data
COPY ./opendata/data /app/data
# Copy over the table defintions
COPY ./opendata/sql_tables/ /app/sql_tables
# Copy over tables sql script
COPY opendata/scripts/postgres_seed.sql /app/scripts/postgres_seed.sql
# Copy over the init script
COPY ./scripts/db/init.sh /docker-entrypoint-initdb.d
