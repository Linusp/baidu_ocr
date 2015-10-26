from sys import version_info

if version_info[0] == 3:
    from .core import BaiduOcr
else:
    from core import BaiduOcr
