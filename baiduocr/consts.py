# coding: utf8

# 限制类错误
ERROR_REQUEST_EXPIRED = 300101       # User's request is expired
ERROR_USER_DAY_OVERRUN = 300102      # User call overrun per day
ERROR_SERVICE_SECOND_OVERRUN= 300103 # Service call overrun per second
ERROR_SERVICE_DAY_OVERRUN = 300104   # Service call overrun per day

# 调用类错误
ERROR_URL_UNRESOLVED = 300201   # URL cannot be resolved
ERROR_APIKEY_MISSING = 300202   # Missing apikey
ERROR_APKKEY_EMPTY = 300203     # Apikey or secretkey is NULL
ERROR_APIKEY_INVALID = 300204   # Apikey does not exist
ERROR_API_INVALID = 300205      # Api does not exist
ERROR_API_ CLOSED = 300206      # Api out of service

# 代理平台错误：
ERROR_INTERNAL = 300301         # Internal error
ERROR_SYSTEM_BUSY = 300302      # The system is busy
