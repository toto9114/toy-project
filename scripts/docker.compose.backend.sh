#!/usr/bin/env bash
set -e
PROJECT_NAME=food-map-api/backend
COMPOSE_FILE=$(pwd)/docker/compose/compose.backend.yml

export ENV_FILE_PATH=$(pwd)/.env

exec docker-compose \
  --file ${COMPOSE_FILE} \
  --project-name food-map-api \
  "$@"
