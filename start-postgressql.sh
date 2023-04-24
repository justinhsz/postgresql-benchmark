podman run --name postgre-benchmark-database -p 5432:5432 \
-e POSTGRES_PASSWORD=Test \
-e POSTGRES_USER=test \
-d postgres:13