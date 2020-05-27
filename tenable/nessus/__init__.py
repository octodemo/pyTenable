from tenable.base.platform import APIPlatform


class NessusScanner(APIPlatform):
    _base_path = '/api'
    _port = 8834
    _env_base = 'NESSUS'
