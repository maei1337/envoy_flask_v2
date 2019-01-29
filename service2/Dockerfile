FROM envoyproxy/envoy-alpine:latest

RUN apk update && apk add python3 bash
COPY requirements.txt .
RUN pip3 install -q --upgrade pip && \
pip3 install --no-cache-dir -r requirements.txt && \
pip3 install gunicorn
ENV FLASK_APP=app.py
RUN mkdir /code
WORKDIR /code
ADD . /code
RUN chmod u+x /code/start_service.sh
ENTRYPOINT /code/start_service.sh
