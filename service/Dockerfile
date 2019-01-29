FROM envoyproxy/envoy-alpine:latest

RUN apk update && apk add python3 bash
COPY requirements.txt .
RUN pip3 install -q --upgrade pip && \
pip3 install --no-cache-dir -r requirements.txt && \
pip3 install gunicorn
ENV FLASK_APP=app.py
RUN mkdir /code
WORKDIR /code
ADD ./start_service.sh /usr/local/bin/start_service.sh
ADD . /code
RUN chmod u+x /usr/local/bin/start_service.sh
ENTRYPOINT /usr/local/bin/start_service.sh
