from nameko.standalone.rpc import ClusterRpcProxy
CONFIG = {'AMQP_URI': "amqp://xthidnmx:naMqLqyPbJlrtYBkm-ZTYcdiIpZcwJsC@fish.rmq.cloudamqp.com/xthidnmx"}

class ServiceDiscover:
    def invoke(self, service_name):
        with ClusterRpcProxy(CONFIG) as rpc:
            if service_name == "AVAILABILITY":
                return rpc.benchmark_ha.verify()
            elif service_name == "COMPUTE":
                return rpc.benchmark_compute.verify()
            elif service_name == "NETWORKING":
                return rpc.benchmark_networking.verify()
            elif service_name == "STORAGE":
                return rpc.benchmark_storage.verify()
            elif service_name == "FEATURE":
                return rpc.benchmark_feature.verify()
            else:
                raise "the service is not registed"
