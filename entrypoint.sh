#!/bin/sh

alembic upgrade head

server_start --host 0.0.0.0 --port 8000
