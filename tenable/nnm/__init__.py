from tenable.platform import TenablePlatform


class NessusNetworkMonitor(TenablePlatform):
    _base_path = '/api'
    _port = 8835
    _env_base = 'NNM'
