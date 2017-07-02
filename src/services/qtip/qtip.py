import yagmail
from nameko.rpc import rpc, RpcProxy

class benchmark_qtip(object):
    name = "benchmark_qtip"

    @rpc
    def verify(self):
        return "Run qtip benchmarking successfully"