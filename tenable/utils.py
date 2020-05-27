from box import Box
from restfly.utils import (
    dict_flatten,
    dict_clean,
    dict_merge,
    trunc,
    check as _chk
)

def check(name, obj, expected_type, **kwargs):
    patterns = {
        'suuid': r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12,32}$'
    }
    kwargs['pattern_map'] = dict_merge(patterns, kwargs.get('pattern_map', dict()))
    return _chk(name, obj, expected_type, **kwargs)