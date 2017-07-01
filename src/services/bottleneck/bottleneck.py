import yagmail
from nameko.rpc import rpc, RpcProxy

class benchmark_bottleneck(object):
    name = "benchmark_bottleneck"

    @rpc
    def verify(self):
        return "Run bottleneck benchmarking"