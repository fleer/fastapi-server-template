#!/bin/bash

envsubst <./config/config.prod.yaml >./config/config.yaml

exec "$@"
