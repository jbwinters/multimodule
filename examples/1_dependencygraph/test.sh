#!/bin/sh

# Run run.sh separately

echo "* v0 (multiapi/v0)"
curl localhost:5000/v0
echo "\n* v1 (multiapi/v1)"
curl localhost:5000/v1
echo "\n* v1.1 (multiapi/v1_1)"
curl localhost:5000/v1.1
echo "\n* v2 (multiapi/v2)"
curl localhost:5000/v2
