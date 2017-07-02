# microservice-testing4opnfv-draft
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
## Technology Dependency

- Python 2.7,3.0
- [Nameko](https://github.com/nameko/nameko)
- [JinJia2](http://jinja.pocoo.org/)
- [Flask](http://flask.pocoo.org/)
- [RabbitMQ as a Service](https://www.cloudamqp.com/#/) We just use a public rabbitMQ service instead of
// installing a private rabbitMQ
    {username:xthidnmx,password:naMqLqyPbJlrtYBkm-ZTYcdiIpZcwJsC},if you want to use a private rabbitMQ service,
    you could also refer to this project [docker_nameko](https://github.com/chunchill/docker-nameko)
- [Docker](https://www.docker.com/),the services are hosted with docker container
- [Docker Compose/Kubernetes](https://kubernetes.io/),the services could be orchestrated with kubenetes or Docker compose

## Debugging the Project Manually
* run the micorserivce bottleneck

    `cd src/services/bottleneck/`

    `nameko run bottleneck --broker amqp://xthidnmx:naMqLqyPbJlrtYBkm-ZTYcdiIpZcwJsC@fish.rmq.cloudamqp.com/xthidnmx`

* run the micorserivce QTIP

    `cd src/services/qtip/`

    `nameko run qtip --broker amqp://xthidnmx:naMqLqyPbJlrtYBkm-ZTYcdiIpZcwJsC@fish.rmq.cloudamqp.com/xthidnmx`

* run the micorserivce storperf

    `cd src/services/storperf/`

    `nameko run storperf --broker amqp://xthidnmx:naMqLqyPbJlrtYBkm-ZTYcdiIpZcwJsC@fish.rmq.cloudamqp.com/xthidnmx`

* run the micorserivce vsperf

    `cd src/services/vsperf/`

    `nameko run bottleneck --broker amqp://xthidnmx:naMqLqyPbJlrtYBkm-ZTYcdiIpZcwJsC@fish.rmq.cloudamqp.com/xthidnmx`

* run the micorserivce yardstick-availability

    `cd src/services/yardstick-availability/`

    `nameko run availability --broker amqp://xthidnmx:naMqLqyPbJlrtYBkm-ZTYcdiIpZcwJsC@fish.rmq.cloudamqp.com/xthidnmx`

* run the micorserivce yardstick-compute

    `cd src/services/yardstick-compute/`

    `nameko run compute --broker amqp://xthidnmx:naMqLqyPbJlrtYBkm-ZTYcdiIpZcwJsC@fish.rmq.cloudamqp.com/xthidnmx`

* run the micorserivce yardstick-feature

    `cd src/services/yardstick-feature/`

    `nameko run feature --broker amqp://xthidnmx:naMqLqyPbJlrtYBkm-ZTYcdiIpZcwJsC@fish.rmq.cloudamqp.com/xthidnmx`

* run the micorserivce yardstick-networking

    `cd src/services/yardstick-networking/`

    `nameko run availability --broker amqp://xthidnmx:naMqLqyPbJlrtYBkm-ZTYcdiIpZcwJsC@fish.rmq.cloudamqp.com/xthidnmx`

* run the micorserivce yardstick-storage

    `cd src/services/yardstick-storage/`

    `nameko run storage --broker amqp://xthidnmx:naMqLqyPbJlrtYBkm-ZTYcdiIpZcwJsC@fish.rmq.cloudamqp.com/xthidnmx`

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
