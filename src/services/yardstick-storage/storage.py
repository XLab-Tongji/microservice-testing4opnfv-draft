import yagmail
from nameko.rpc import rpc, RpcProxy

class benchmark_storage(object):
    name = "benchmark_storage"

    @rpc
    def verify(self):
        return "Run yardstick-storage benchmarking successfully"