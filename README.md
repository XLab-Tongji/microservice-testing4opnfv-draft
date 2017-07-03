# microservice-testing4opnfv-draft

![](project-icon.png)

> A microservice project for opnfv testing framework with python full stack technology

## Architechture

![OPNFV testing framework microservice](arch.png)

## Features

According to the [OPNFV](https://www.opnfv.org/) guide:
"[A Guide to Understanding OPNFV & NFV](https://www.opnfv.org/resources/download-understanding-opnfv-ebook)",
there are at least 5 projects which are related to testing, they are:

- [Bottleneck](https://wiki.opnfv.org/display/bottlenecks)
- [QTIP](https://wiki.opnfv.org/display/qtip)
- [Storeperf](https://wiki.opnfv.org/display/storperf)
- [VSPerf](https://wiki.opnfv.org/display/vsperf)
- [yardstick](https://wiki.opnfv.org/display/yardstick)
    - availability
    - compute
    - networking
    - storage
    - feature

We try to design a microservice testing framework with [Domain Driven Design](https://martinfowler.com/tags/domain%20driven%20design.html) philosophy,it will cover the above services.
    The granularity and the context boundary of the micro-services are still topics worthy of dicussion.

    Currently,this project is still in its draft and proposal stage.
## Technology Dependency

- Python 2.7,3.0
- [Nameko](https://github.com/nameko/nameko)
- [JinJia2](http://jinja.pocoo.org/)
- [Flask](http://flask.pocoo.org/)
- [RabbitMQ as a Service](https://www.cloudamqp.com/#/),for convenience,we just use a public FREE RabbitMQ service instead of
    installing a private rabbitMQ.
    the account of the public service is :`{username:xthidnmx,password:naMqLqyPbJlrtYBkm-ZTYcdiIpZcwJsC}`.
    if you want to use a private RabbitMQ service,you could also refer to the project [docker_nameko](https://github.com/chunchill/docker-nameko).
- [Docker](https://www.docker.com/),the services are hosted with docker container
- [Docker Compose](https://docs.docker.com/compose/)/[Kubernetes](https://kubernetes.io/),the services could be orchestrated with kubenetes or Docker compose

## Debugging the Project Manually

You could replace the following `AMPQ_URL` with `amqp://xthidnmx:naMqLqyPbJlrtYBkm-ZTYcdiIpZcwJsC@fish.rmq.cloudamqp.com/xthidnmx`,which is the public RabbitMQ Service

* run the microservice bottleneck

    ```
    $ cd src/services/bottleneck/
    $ nameko run bottleneck --broker AMPQ_URL
    ```

* run the microservice QTIP

    `cd src/services/qtip/`

    `nameko run qtip --broker AMPQ_URL`

* run the microservice storperf

    `cd src/services/storperf/`

    `nameko run storperf --broker AMPQ_URL`

* run the microservice vsperf

    `cd src/services/vsperf/`

    `nameko run bottleneck --broker AMPQ_URL`

* run the microservice yardstick-availability

    `cd src/services/yardstick-availability/`

    `nameko run availability --broker AMPQ_URL`

* run the microservice yardstick-compute

    `cd src/services/yardstick-compute/`

    `nameko run compute --broker AMPQ_URL`

* run the microservice yardstick-feature

    `cd src/services/yardstick-feature/`

    `nameko run feature --broker AMPQ_URL`

* run the microservice yardstick-networking

    `cd src/services/yardstick-networking/`

    `nameko run availability --broker AMPQ_URL`

* run the microservice yardstick-storage

    `cd src/services/yardstick-storage/`

    `nameko run storage --broker AMPQ_URL`

* run the service-gateway

    `cd src/api-gateway/`

    `python api.py`

## Support

For help,comments or question, please contact [Juan Qiu](mailto:juan_qiu@tongji.edu.cn)

## Contribute

- Fork the repository
- Raise an issue or make a feature request

## License

This project is an open-source project licensed under Apache 2.0.
