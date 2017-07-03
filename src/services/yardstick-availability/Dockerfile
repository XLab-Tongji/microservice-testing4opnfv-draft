FROM microservice-benchmarker-base

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt

CMD ["nameko run","--config", "config.yml","availability"]