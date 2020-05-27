from tenable.base.platform import APIPlatform


class NessusNetworkMonitor(APIPlatform):
    _base_path = '/api'
    _port = 8835
    _env_base = 'NNM'
