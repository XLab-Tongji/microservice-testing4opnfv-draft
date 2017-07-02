import yagmail
from nameko.rpc import rpc, RpcProxy

class benchmark_storperf(object):
    name = "benchmark_storperf"

    @rpc
    def verify(self):
        return "Run storperf benchmarking successfully"