# microservice-yardstick-draft
> a microservice project for opnfv testing framework with python full stack technology

## Architechture

![OPNFV testing framework microservice](arch.png)

## Features

According to the OPNFV guide, there are at list 5 projects which are related to testing, they are:

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


`nameko run SERVICE_NAME --broker amqp://xthidnmx:naMqLqyPbJlrtYBkm-ZTYcdiIpZcwJsC@fish.rmq.cloudamqp.com/xthidnmx`

you could run the following command to testing the RPC service

`nameko shell --broker amqp://xthidnmx:naMqLqyPbJlrtYBkm-ZTYcdiIpZcwJsC@fish.rmq.cloudamqp.com/xthidnmx`

The RabbitMQ service is provided by : `https://fish.rmq.cloudamqp.com/#/`

The services could be deployed with kubernetes:

`http://blog.apcelent.com/scaling-python-microservices-kubernetes.html`


## Support

For help,comments or question, please contact [Juan Qiu](mailto:juan_qiu@tongji.edu.cn)

## Contribute

- Fork the repository
- Raise an issue or make a feature request

## License

This project is an open-source project licensed under Apache 2.0.