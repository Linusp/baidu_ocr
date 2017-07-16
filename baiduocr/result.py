# -*- coding: utf-8 -*-

from __future__ import absolute_import
from baiduocr.consts import (
    ERROR_NO_RESULT,
)


class Rect(object):
    """矩形区域"""

    def __init__(self, top=0, left=0, width=0, height=0):
        self.top = int(top)
        self.left = int(left)
        self.width = int(width)
        self.height = int(height)


class Result(object):
    """百度 OCR 返回结果类"""

    def __init__(self, response):
        """初始化方法"""
        if response:
            self.status = int(response.get(u'errNum'))
            self.message = response.get(u'errMsg')
            self.sign = response.get(u'querySign')
            self.result = response.get(u'retData')
        else:
            self.status = ERROR_NO_RESULT
            self.message = u'No result received'
            self.sign = None
            self.result = None


class LocateRecognizeResult(Result):
    """service type 为 Recognize, Locate, LocateRecognize 时的结果"""

    def __init__(self, response):
        """初始化，将 result 转换成更易处理的格式"""
        super(LocateRecognizeResult, self).__init__(response)
        self.result = [
            (row.get(u'word', u''), Rect(**row.get(u'rect')))
            for row in self.result
        ] if self.result else []

    def get_result_text(self):
        """获取识别文本"""
        res = None
        if self.result:
            res = u'\n'.join([text for text, _ in self.result]).strip()

        if not res:
            return u'Error: No text result'

        return res

    def get_result_regions(self):
        """获取识别结果中的区域信息"""
        if self.result:
            return [region for _, region in self.result]

        return []
