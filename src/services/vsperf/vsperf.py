import yagmail
from nameko.rpc import rpc, RpcProxy

class benchmark_vsperf(object):
    name = "benchmark_vsperf"

    @rpc
    def verify(self):
        return "Run vsperf benchmarking"