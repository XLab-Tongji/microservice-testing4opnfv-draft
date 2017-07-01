from nameko.rpc import rpc, RpcProxy

class benchmark_ha(object):
    name = "benchmark_ha"

    @rpc
    def verify(self):
        return "Run HA benchmarking"