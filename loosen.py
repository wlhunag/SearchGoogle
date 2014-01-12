#-*- coding: utf-8-*-
__author__ = 'Aaron'

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
import mechanize
import urllib
import sqlite3
import os
import re
from bs4 import BeautifulSoup
from MainWindow import Ui_MainWindow

class Dictionary(QMainWindow,Ui_MainWindow):

    def __init__(self, term, parent = None):
        super(Dictionary, self).__init__( parent)
        self.setupUi(self)

        browser_content = mechanize.Browser()
        browser_content.set_handle_robots(False)
        #還是會被Google 抓到耶，怎麼辦？
        browser_content.addheaders = [('User-agent','Mozilla')]

        #如何設定傳入的關鍵字？
        # term = r'福音 教義'
        term = term.replace(" ","+")
        # term = urllib.quote(term)
        query = 'http://www.google.com/search?num=10&q=' + term

        self.htmltext = browser_content.open(query).read().decode('mbcs').replace("<b>","<b class=p>")
        #把奇怪的字串弄成可以連結的正常URL
        self.htmltext = re.subn(r"(?si)/url\?q=(.*?)&amp[^>]*", r'\1"', self.htmltext)

        soup = BeautifulSoup(self.htmltext[0])
        self.content = unicode(soup.find(id="ires"))
        #將self.content 存起來
        QA = (
            (1,term, self.content),
        )
        con = sqlite3.connect('test.db')
        with con:
            cur = con.cursor()
            cur.execute('DROP TABLE IF EXISTS Questions')
            cur.execute('CREATE TABLE Questions(Id INT, Qa TEXT, Results TEXT)')
            cur.executemany('INSERT INTO Questions VALUES(?,?,?)', QA)


    # def search(self):
    #     fn = os.path.join(os.getcwdu(),"test.html")
        src_location = os.path.abspath(os.path.dirname(__file__))
        baseUrl = QUrl.fromLocalFile(os.path.join(src_location,"resources/"))
    #     self.webView.load(QUrl.fromLocalFile(fn))
        websettings = self.webView.settings()
        websettings.setAttribute(QWebSettings.PluginsEnabled,True)

        con = sqlite3.connect('test.db')
        with con:
            cur = con.cursor()
            cur.execute("SELECT Results from Questions WHERE Qa=?", (term,))
            con.commit()
            row = cur.fetchone()
        from resources.html_dec import html_end, html_head
        # self.post_content = html_head.format(term).decode('utf-8') + \
        #                   unicode(self.content) + html_end.decode('utf-8')
        self.post_content = html_head.format(term) + row[0] + html_end
        #這樣按 backspace 好像沒辦法回上一頁？
        self.webView.setHtml(self.post_content, baseUrl)




app = QApplication(sys.argv)
query = 'Queen'
#應該要兩個query ，一個加括號，一個不加
dictionary = Dictionary(query)
dictionary.show()

app.exec_()