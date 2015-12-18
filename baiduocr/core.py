# -*- coding: utf-8 -*-

import requests


API_URL = 'http://apis.baidu.com/idl_baidu/baiduocrpay/idlocrpaid'


class BaiduOcr(object):
    """百度 OCR 客户端"""

    _IMAGE_FOR_TEST = '/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDABMNDxEPDBMREBEWFRMXHTAfHRsbHTsqLSMwRj5KSUU+RENNV29eTVJpU0NEYYRiaXN3fX59S12Jkoh5kW96fXj/2wBDARUWFh0ZHTkfHzl4UERQeHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHj/wAARCAAfACEDAREAAhEBAxEB/8QAGAABAQEBAQAAAAAAAAAAAAAAAAQDBQb/xAAjEAACAgICAgEFAAAAAAAAAAABAgADBBESIRMxBSIyQXGB/8QAFAEBAAAAAAAAAAAAAAAAAAAAAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/APawEBAQEBAgy8i8ZTVV3UY6V1eU2XoWDDZB19S646Gz39w9fkKsW1r8Wm2yo1PYis1be0JG9H9QNYCAgc35Cl3yuVuJZl0cB41rZQa32dt2y6OuOiOxo61vsLcVblxaVyXD3hFFjL6La7I/sDWAgICAgICB/9k='
    _IMAGE_MAX_SIZE = 307200    # 300K

    _SERVICE_LIST = set(['LocateRecognize', 'Locate', 'Recognize', 'SingleCharRecognize'])
    _LANG_LIST = set(['CHN_ENG', 'ENG', 'JAP', 'KOR'])

    def __init__(self, url=API_URL, key=''):
        """初始化客户端

        :type api_key: str
        :param api_key: API 服务授权代码

        :type environment: str
        :param environment: API 服务类型，设定为 'online' 时使用企业版 API；
                            否则使用个人免费版 API(默认)
        """
        self.api_key = key
        self.url = url

    def ping(self):
        """使用 API Store 提供的示例测试服务是否可用

        当 API 测试正常时，将会输出 'pong'。同时 API 返回的结果将会被返回，方便
        出错时进行调试
        """
        header = {'apikey': self.api_key}
        data = {}
        data['fromdevice'] = 'pc'
        data['clientip'] = '10.10.10.0'
        data['detecttype'] = 'Recognize'
        data['languagetype'] = 'CHN_ENG'
        data['imagetype'] = '1'
        data['image'] = self._IMAGE_FOR_TEST

        resp = requests.post(self.url, headers=header, data=data)
        res = resp.json() if resp is not None else {}

        if res.get(u'errNum', -1) == u'0' and res.get(u'errMsg', '') == u'success':
            print('pong')

        return res

    def recog(self, image, service='Recognize', lang='CHN_ENG'):
        """调用百度 OCR API 进行图片文字识别

        :type image: str
        :param image: 待识别文字的图像，可为本地文件或网络文件链接，若该
                      图像大小超过 300K ，将会抛出异常

        :type service: str
        :param service: 请求的服务类型，可用的服务类型即说明如下
                        + LocateRecognize: 整图文字检测、识别，以行为单位
                        + Locate: 整图文字行定位
                        + Recognize: 整图文字识别(默认)
                        + SingleCharRecognize: 单字图像识别

        :type lang: str
        :param lang: 指定要检测的文字类型，目前仅支持以下类型
                     + CHN_ENG: 中英文
                     + ENG: 英文
                     + JAP: 日文
                     + KOR: 韩文

        返回结果是一个 dict 类型的值，包含以下几个字段
        + errNum: 结果状态，类型为 unicode, 为 0 时表示有结果且正常；否则表示出错
        + errMsg: 错误消息，类型为 unicode
        + querySign: 本次请求的唯一性标识(无用)
        + retData: 实际结果，类型为 list
        """
        header = {'apikey': self.api_key}
        data = {}
        data['fromdevice'] = 'pc'
        data['clientip'] = '10.10.10.0'
        data['detecttype'] = service
        data['languagetype'] = lang
        data['imagetype'] = '2'

        image_file = None
        try:
            if image.startswith('http://') or image.startswith('https://'):
                r = requests.get(image)
                image_file = r.content
            else:
                image_file = open(image, 'rb')
        except Exception:
            return {}

        resp = requests.post(self.url, headers=header, data=data, files={'image': ('ocr.jpg', image_file)})

        return {} if not resp else resp.json()
