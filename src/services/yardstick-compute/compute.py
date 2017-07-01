from nameko.rpc import rpc, RpcProxy

class benchmark_compute(object):
    name = "benchmark_compute"

    @rpc
    def verify(self):
        return "Run yardstick-compute benchmarking"