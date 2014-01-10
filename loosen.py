#-*- coding: utf-8-*-
__author__ = 'Aaron'
'''
目前一切還在構思中，不確定網路上有無現成的原始碼
依照文件類型不同
  1.可以切segment，如果文字完全符合就用綠色，75%符合就用藍色，50%符合就用咖啡色
  2.照paragraph 分，也許可以標示出符合的部分
'''

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import mechanize
import os
import re
from bs4 import BeautifulSoup
from MainWindow import Ui_MainWindow

class Dictionary(QMainWindow,Ui_MainWindow):

    def __init__(self, parent = None):
        super(Dictionary, self).__init__(parent)
        self.setupUi(self)

        #不知如何變成utf-8編碼的網頁，只好手動加入
        html_head = '''<!DOCTYPE html>
<html itemscope="" itemtype="http://schema.org/WebPage">
 <head>
  <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
  <title>
   {0}
  </title>
<link rel="stylesheet" type="text/css" href="style.css"/>
<body>

  '''
        html_end = '</body></html>'



        browser_content = mechanize.Browser()
        browser_content.set_handle_robots(False)
        browser_content.addheaders = [('User-agent','chrome')]
        #如何設定傳入的關鍵字？
        term = 'car good'
        term = term.replace(" ","+") #不換成+會導致錯誤
        query = 'http://www.google.com.tw/search?num=10&q=' + term

        self.htmltext = browser_content.open(query).read().decode('mbcs').replace("<b>","<b class=p>")
        #把奇怪的字串弄成可以連結的正常URL
        self.htmltext = re.subn(r"(?si)/url\?q=(.*?)&amp[^>]*", r'\1"', self.htmltext)

        soup = BeautifulSoup(self.htmltext[0])

        self.post_content = html_head.format(term).decode('utf-8') + \
                            unicode(soup.find(id="ires")) + html_end.decode('utf-8')

        # with open("oo.html",'wb') as fh:
        #     fh.write(self.post_content.encode('utf-8'))

        #思考如何寫入資料庫，而不是用檔案？
        #當然也要想如何從資料庫拿出資料？
        # with open("test.html",'wb') as fh:
        #     fh.write(self.content)

        # self.search()


    # def search(self):
    #     fn = os.path.join(os.getcwdu(),"test.html")
        src_location = os.path.abspath(os.path.dirname(__file__))
        baseUrl = QUrl.fromLocalFile(os.path.join(src_location,"resources/"))
    #     self.webView.load(QUrl.fromLocalFile(fn))
        self.webView.setHtml(self.post_content,baseUrl )




app = QApplication(sys.argv)

dictionary = Dictionary()
dictionary.show()

app.exec_()