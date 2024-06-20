# fastapi-server-template

For information about the API see **Swagger Documentation**
The Documentation about the project can be found here:

## Development

### Package and Build Management via Poetry

Poetry is a tool for Python project and dependency management. It helps you declare the libraries your project depends on and it will manage (install/update) them for you.

Here's how you can install and use Poetry:

1. **Installation**

   You can install Poetry through `curl` or `pip`. Here's the `curl` method:

   ```bash
   curl -sSL https://install.python-poetry.org | python -
   ```

   This command downloads a script and executes it. The script then checks your Python installation and downloads the appropriate version of Poetry.

2. **Usage**

   To install all dependencies of the project, navigate to the project's directory (which contains `pyproject.toml` and `poetry.lock` files) and run:

   ```bash
   poetry install --with dev,docs
   ```

   This command reads the `pyproject.toml` file to identify the dependencies and then installs them.

3. **Build**

   To build the project run

   ```bash
   poetry build

   ```

After installing the dependencies, the service can be started via

```bash
uvicorn src.service.api:app --reload --port 8000
```

If the code changes, the service is reloaded automatically.

For information about the API see the Swagger Documentation at [http://localhost:8000/docs](http://localhost:8000/docs).

```bash
poetry run service.app:

```

The access to a PostgreSQL database is expected in order to run the webservice. For development the database can be set up easily by either uncommenting the `app` service in the `docker-compose.yaml` or be manually starting the database server via

```bash
docker run --name some-postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -d postgres

```

## Configuration

The service can be configured via the `config/config.yaml` file. Currently only
the connection information for the database are mandatory.

```yaml
database:
  db_schema: public
  # host: localhost -> For local dev and testing
  host: postgres # -> For execution via docker compose
  db_name: postgres
  port: 5432
  user: postgres
  password: postgres
```

## Build

The _package version_ is automatically determined via the current git tag.

### Locally

After installing the package vie `poetry install` or building and then
installing the `*.wheel` via

```bash
poetry build

pip install dist/*.wheel
```

it is possible to start the service via

```bash
poetry shell # If not installed globally via pip
server_start --host 0.0.0.0 --port 8000
```

### Docker

The docker image can be build via

```bash
docker build . -t test

```

Run the created image via

```bash
docker run --rm -it -v $(pwd)/config:/app/config -p 8000:8000 test
```

Please note that the application expects a configuration `config/config.yaml`
which is not included in the image. It has to be _manually created and then mounted_ during
the container start-up.

### Docker compose

Start the service and the corresponding database via

```bash
docker compose up --remove-orphans --build
```

## Tools

### Pre-Commit

Install [pre-commit](https://pre-commit.com) and initialize the tool via `pre-commit install`.
All hooks can be manually executed via `pre-commit run --all-files`.
