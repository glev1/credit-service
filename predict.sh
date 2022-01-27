#!/usr/bin/env bash

PORT=8080
echo "Port: $PORT"

# POST method predict
curl -d '{
    "inc": 9000,
    "age": 30,
    "rev": 0.7,
    "debt": 0.8,
    "dep": 2,
    "cred": 5,
    "estate": 2,
    "lowdue": 2,
    "middue": 0,
    "highdue": 0
}'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/predict