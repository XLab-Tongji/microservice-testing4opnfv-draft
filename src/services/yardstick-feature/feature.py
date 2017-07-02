from nameko.rpc import rpc, RpcProxy

class benchmark_feauture(object):
    name = "benchmark_feature"

    @rpc
    def verify(self):
        return "Run feautre benchmarking successfully"