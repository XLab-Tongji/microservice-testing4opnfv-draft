TAG ?= dev
# docker

run-wheel-builder:
	docker run --rm \
		-v "$$(pwd)":/application -v "$$(pwd)"/wheelhouse:/wheelhouse \
		microservice-benchmarker-builder;

build-image:
	docker build -t chunchill/benchmarker-vsperf:$(TAG) .;

push-image:
	docker push chunchill/benchmarker-vsperf:$(TAG)
