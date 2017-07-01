import yagmail
from nameko.rpc import rpc, RpcProxy


class benchmark_networking(object):
    name = "benchmark_networking"

    @rpc
    def verify(self):
        return "Run yardstick-networking benchmarking"