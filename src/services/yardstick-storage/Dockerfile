FROM python:2.7
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
ARG AMQP_URL

CMD ["nameko run service","--broker", "$AMQP_URL"]