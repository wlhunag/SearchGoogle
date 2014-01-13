#-*- coding: utf-8-*-
__author__ = 'Aaron'
import re


class TextTwist:
    def __init__(self,text):
        ''' 字串傳進來以後，如何依序完成所有的文字操作
            請參考 RegexBuddy 或 PowerGrep 的內容'''
        text = self.delete_blankline(text)
        return text

    def delete_blankline(self, text):
        '''刪除空行'''
        return re.sub("(?m)^[ \t]*$\r?\n", "", text)

    def del_whitespace(self, text):
        '''刪除兩個以上的空白'''
        return re.sub("(?m)([ \t]{2,})", " ", text)

    def separate_header(self, text):
        #TODO 把選項 (A)(B)(C)(D) 全部分開
        pass