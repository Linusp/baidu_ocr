# -*- coding: utf-8 -*-

import requests

IMAGE_FOR_TEST = '/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDABMNDxEPDBMREBEWFRMXHTAfHRsbHTsqLSMwRj5KSUU+RENNV29eTVJpU0NEYYRiaXN3fX59S12Jkoh5kW96fXj/2wBDARUWFh0ZHTkfHzl4UERQeHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHj/wAARCAAfACEDAREAAhEBAxEB/8QAGAABAQEBAQAAAAAAAAAAAAAAAAQDBQb/xAAjEAACAgICAgEFAAAAAAAAAAABAgADBBESIRMxBSIyQXGB/8QAFAEBAAAAAAAAAAAAAAAAAAAAAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/APawEBAQEBAgy8i8ZTVV3UY6V1eU2XoWDDZB19S646Gz39w9fkKsW1r8Wm2yo1PYis1be0JG9H9QNYCAgc35Cl3yuVuJZl0cB41rZQa32dt2y6OuOiOxo61vsLcVblxaVyXD3hFFjL6La7I/sDWAgICAgICB/9k='


class BaiduOcr(object):
    def __init__(self, api_key=''):
        """Initialize a ocr instance with usable api key."""
        self.url = 'http://apis.baidu.com/apistore/idlocr/ocr'
        self.header = {}
        if isinstance(api_key, str):
            self.header['apikey'] = api_key

        if not self.test_api():
            raise Exception("Invalid API KEY: %s" % api_key)


    def recog(self, image, service='Recognize', lang='CHN_ENG'):
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
                image_file = open(image, 'rb').read()
        except Exception:
            return None

        resp = requests.post(self.url, headers=self.header, data=data, files={'image': ('ocr.jpg', image_file)})

        return resp.json()


    def test_api(self):
        data = {}
        data['fromdevice'] = 'pc'
        data['clientip'] = '10.10.10.0'
        data['detecttype'] = 'Recognize'
        data['languagetype'] = 'CHN_ENG'
        data['imagetype'] = '1'
        data['image'] = IMAGE_FOR_TEST
        resp = requests.post(self.url, headers=self.header, data=data)

        if resp is not None and resp.json().get(u'errMsg') == u'success':
            return True
        else:
            return False
