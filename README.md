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

    When starting the app, it is checked if a `config.dev.yaml` file is present. If
    this is the case, it is loaded instead of `config.yaml`

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

### Alembic

The database is managed via [alembic](https://alembic.sqlalchemy.org/en/latest/index.html). Thus, all changes that have to be made to the
database tables have to be managed via this tool in order to have a consistent
history. While applying changes to the database tables, alembic stores information
in the `alembic_version` table.

### Python Semantic Release

[Python Semantic Release](https://python-semantic-release.readthedocs.io/en/latest/index.html) is utilized to automatically bump the version on each commit based on [semantic versioning](https://semver.org/spec/v2.0.0.html) conventions.
Per default, the git commit guidelines have to be provided in the [angular style](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#-git-commit-guidelines).

#### Commit Message Format

- Header: Includes type, scope (optional), and subject.
- Body: Details about the change.
- Footer: Notes on breaking changes or issue references.

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

#### Commit Types

Commit message types determine the next version of your app. For example, the feat type increases the MINOR version number, while the fix type increases the PATCH number. Here are the standard types:

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code changes without fixing bugs or adding features
- `perf`: Performance improvements
- `test`: Testing changes
- `chore`: Build process or auxiliary tool changes

## Good Practice

### Service-Repository Pattern

#### Repository Pattern

     The Repository pattern abstracts the data access layer by offering a clean interface for
     interacting with the underlying data storage, whether it’s a database, external API,
     or any other data source. It encapsulates the logic for querying, creating, updating,
     and deleting data entities, thereby promoting the separation of concerns and enhancing the
     maintainability and testability of the codebase.

#### Service Layer

     The service layer acts as the intermediary between the API endpoints and the repository layer.
     It’s responsible for implementing business logic, orchestrating interactions between different
     repositories, and performing necessary validations or additional operations.

#### Literature

- [Fast API — Repository Pattern and Service Layer](https://medium.com/@kacperwlodarczyk/fast-api-repository-pattern-and-service-layer-dad43354f07a)
- [Service-Repository Pattern](https://medium.com/@ankitpal181/service-repository-pattern-802540254019)
