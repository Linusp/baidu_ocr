# -*- coding: utf-8 -*-

from __future__ import absolute_import
from operator import itemgetter
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

        if not res or len(res) == 0:
            return u'Error: No text result'
        else:
            return res

    def get_result_regions(self):
        """获取识别结果中的区域信息"""
        if self.result:
            return [region for _, region in self.result]
        else:
            return []


class SingleCharResult(Result):
    """service type 为 SingleCharRecognize 时的结果"""

    def __init__(self, response):
        """初始化，将 result 转换成更易处理的格式"""
        super(SingleCharResult, self).__init__(response)
        self.result = [
            (row.get(u'word'), float(row.get(u'prob')))
            for row in self.result
        ] if self.result else []
        self.result = sorted(self.result, key=itemgetter(1), reverse=True)
        self.threshold = 0.50

    def get_threshold(self):
        """获取当前的拒绝阈值，识别结果中置信度低于该阈值的结果将会被忽视"""
        return self.threshold

    def set_threshold(self, threshold):
        """设定拒绝阈值"""
        self.threshold = threshold

    def get_char(self):
        """获取识别结果中置信度最大的字符，这里会通过拒绝阈值来进行过滤"""
        char = None
        if self.result:
            char, prob = self.result[0]
            if prob < self.threshold:
                char = None

        return char if char else 'Error: No character result'
