FROM microservice-benchmarker-base

ADD . /code
WORKDIR /code


RUN pip install virtualenv
RUN virtualenv /appenv
RUN . /appenv/bin/activate; pip install -U pip

ADD wheelhouse /var/microservice/wheelhouse
COPY config.yml /var/microservice/config.yml
COPY run.sh /var/microservice/run.sh

RUN chmod +x /var/microservice/run.sh

RUN . /appenv/bin/activate; \
    pip install --no-index -f wheelhouse benchmarker_bottleneck

EXPOSE 8000

CMD . /appenv/bin/activate; \
    /var/microservice/run.sh;