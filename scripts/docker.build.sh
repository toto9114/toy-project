#!/usr/bin/env bash
PROJECT_NAME=food-map-api/backend

docker build --network host -t ${PROJECT_NAME} .
