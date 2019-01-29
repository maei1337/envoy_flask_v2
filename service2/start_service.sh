#!/bin/sh
exec gunicorn -b 0.0.0.0:8080 --name app --reload app:app &
envoy -c /etc/service-envoy.yaml --service-cluster service${SERVICE_NAME}
