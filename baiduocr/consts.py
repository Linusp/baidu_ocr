# coding: utf8

ERROR_NO_RESULT = -1            # 服务未返回结果

# 限制类错误
ERROR_REQUEST_EXPIRED = 300101        # 用户请求过期
ERROR_USER_DAY_OVERRUN = 300102       # 用户日调用量超限
ERROR_SERVICE_SECOND_OVERRUN = 300103 # 服务每秒调用量超限
ERROR_SERVICE_DAY_OVERRUN = 300104    # 服务日调用量超限

# 调用类错误
ERROR_URL_UNRESOLVED = 300201    # URL 无法解析
ERROR_APIKEY_MISSING = 300202    # 请求缺少 API Key
ERROR_APKKEY_EMPTY = 300203      # 服务没有取到 API Key 或 secretkey
ERROR_APIKEY_INVALID = 300204    # API key 不存在
ERROR_API_INVALID = 300205       # API 不存在
ERROR_API_CLOSED = 300206        # API 已关闭服务
ERROR_SERVICE_OVERDUE = 300207   # 余额不足
ERROR_USER_NOT_VERIFIED = 300208 # 用户未通过实名认证
ERROR_RESPONSE_STATUS = 300209   # 服务响应 status 非 200

# 代理平台错误：
ERROR_INTERNAL = 300301         # 内部错误
ERROR_SYSTEM_BUSY = 300302      # 系统繁忙

# 付费版调用方法错误
ERROR_WRONG_PARAMETER = -20001    # 参数错误
ERROR_WRONG_SERVICE_TYPE = -20002 # 没有找到对应的服务类型
ERROR_PACKAGE_ERROR = -20003      # package error
ERROR_SEND_ERROR = -20005         # send error
ERROR_SYSTEM_TIMEOUT = -20006     # receive or parse error
