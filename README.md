# park-crawler

![CI](https://github.com/amritpurshotam/park-crawler/actions/workflows/ci.yaml/badge.svg)

## Running a migration

### Create the migration script
```console
$ docker-compose run app alembic revision --autogenerate -m "Add table"
```

### Apply the migration
```console
$ docker-compose run app alembic upgrade head
```