"""
Connection types are specified here:
    https://code.google.com/p/selenium/source/browse/spec-draft.md?repo=mobile#120
    Value (Alias)      | Data | Wifi | Airplane Mode
    -------------------------------------------------
    0 (None)           | 0    | 0    | 0
    1 (Airplane Mode)  | 0    | 0    | 1
    2 (Wifi only)      | 0    | 1    | 0
    4 (Data only)      | 1    | 0    | 0
    6 (All network on) | 1    | 1    | 0
"""
class ConnectionType(object):
    NO_CONNECTION = 0
    AIRPLANE_MODE = 1
    WIFI_ONLY = 2
    DATA_ONLY = 4
    ALL_NETWORK_ON = 6
