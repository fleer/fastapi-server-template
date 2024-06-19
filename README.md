# fastapi-server-template

Template Repository for FastAPI Service incl. SQLAlchemy

## Tools

### Pre-Commit

Install [pre-commit](https://pre-commit.com) and initialize the tool via `pre-commit install`.
All hooks can be manually executed via `pre-commit run --all-files`.

### Docker

```bash
docker run --rm -it -v $(pwd)/config:/app/config -p 8000:8000 test
```

#### Docker Compose
