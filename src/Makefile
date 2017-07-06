IMAGES := services/bottleneck services/qtip services/storperf services/vsperf services/yardstick-availability \
services/yardstick-compute services/yardstick-feature services/yardstick-networking services/yardstick-storage \
api-gateway

build-microservice-base:
	docker build -t microservice-benchmarker-base -f docker/docker.base .;

build-wheel-builder: build-microservice-base
	docker build -t microservice-benchmarker-builder -f docker/docker.build .;

run-wheel-builder: build-wheel-builder
	for image in $(IMAGES) ; do make -C $$image run-wheel-builder; done

build-images: run-wheel-builder
	for image in $(IMAGES) ; do make -C $$image build-image; done

build: build-images

docker-login:
	docker login --email=$(DOCKER_EMAIL) --password=$(DOCKER_PASSWORD) --username=$(DOCKER_USERNAME)

push-images: build
	for image in $(IMAGES) ; do make -C $$image push-image; done