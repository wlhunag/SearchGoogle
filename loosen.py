#-*- coding: utf-8-*-
__author__ = 'Aaron'

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
from manipulation import TextTwist
from PyQt4.QtWebKit import *
import mechanize
import sqlite3
import os
import re
from bs4 import BeautifulSoup
from qtui.MainWindow import Ui_MainWindow

class Dictionary(QMainWindow,Ui_MainWindow):

    def __init__(self, parent=None):
        super(Dictionary, self).__init__(parent)
        self.setupUi(self)
        self.browser_content = mechanize.Browser()
        self.browser_content.set_handle_robots(False)
        self.browser_content.addheaders = [('User-agent', 'Mozilla')]
        self.webset()
        self.updateresults()
        self.createconnection()

    def webset(self):
        websettings = self.webView_2.settings()
        websettings.setAttribute(QWebSettings.PluginsEnabled, True)
        websettings.setAttribute(QWebSettings.WebGLEnabled, True)
        websettings.setAttribute(QWebSettings.AutoLoadImages, True)
        websettings.setAttribute(QWebSettings.LocalStorageEnabled, True)
        websettings.setAttribute(QWebSettings.LocalContentCanAccessFileUrls, True)
        websettings.setAttribute(QWebSettings.LocalContentCanAccessRemoteUrls, True)
        websettings.setAttribute(QWebSettings.DeveloperExtrasEnabled, True)

    def createconnection(self):
        self.pushButton_search.clicked.connect(lambda: self.analyse())
        self.tabWidget.currentChanged.connect(lambda: self.updateresults())
        self.treeWidget.itemClicked.connect(lambda: self.showhtml())
        self.pushButton_clear.clicked.connect(lambda: self.clearDB())

    def analyse(self):
        text = unicode(self.QuestionText.toPlainText()).encode('utf-8')
        print(text)
        for subject in re.sub('[ ]+',' ',text.strip().replace("   ", " ").replace("  ", " ")).split('\n'):
            self.search(subject)

    def clearDB(self):
        os.remove(os.path.join(os.getcwdu(),"storage.db"))
        self.updateresults()

    def search(self, term):
        #TODO以後還要改良這邊的演算法，現在是毫無演算法可言啦~
        row = term.replace(" ", "+")
        #TODO 送 Google 查詢前，需要先處理，應該要用一個Class 來處理，見manipulation.py
        query = 'http://www.google.com.tw/search?num=10&q=' + row
        self.htmltext = self.browser_content.open(query).read()
        #不知為何這邊編碼一定要mbcs，不然就會變亂碼？？        #原本以為已經弄懂編碼了，結果又混亂了
        self.htmltext = re.subn(r"(?si)/url\?q=(.*?)&amp[^>]*", r'\1"', self.htmltext.decode('mbcs').replace("<b>","<b class=p>").replace("%3F", "?").replace("%3D", "=").replace("%25", "%"))#.replace('href="/', 'href="http://www.google.com.tw/'))
        #TODO 最後兩個Replace 是應付php 網站的，和Google 圖片的但似乎也不是很好的解法，很多可能性要考慮，是否要一個一個取代？？

        soup = BeautifulSoup(self.htmltext[0])
        for div in soup.findAll('div', 'am-dwn-arw-container'):
            div.extract()
        content = unicode(soup.find(id="ires"))
        QA = (
            (term.decode('utf-8'), content),
        )
        con = sqlite3.connect('storage.db')
        with con:
            cur = con.cursor()
            cur.executemany('INSERT INTO Questions VALUES(?,?)', QA)

    def updateresults(self):
        if os.path.isfile(os.path.join(os.getcwdu(),"storage.db")):
            pass

        else:
            con = sqlite3.connect('storage.db')
            with con:
                cur = con.cursor()
                cur.execute('CREATE TABLE Questions(Qa TEXT, Results TEXT)')

        con = sqlite3.connect('storage.db')
        with con:
            cur = con.cursor()
            cur.execute('SELECT Qa FROM Questions')
            rows = cur.fetchall()
            self.treeWidget.clear()

            for row in rows:
                self.treeWidget.addTopLevelItem(QTreeWidgetItem(row))

    def showhtml(self):
        for item in self.treeWidget.selectedItems():
            term = unicode(item.text(0))
        self.tabWidget_2.setTabText(0, term)
        print repr(term)
        con = sqlite3.connect('storage.db')
        with con:
            cur = con.cursor()
            cur.execute("SELECT Results from Questions WHERE Qa=?", (term,))
            con.commit()
            row = cur.fetchone()
        from resources.html_dec import html_end, html_head
        self.post_content = html_head % term + row[0] + html_end

        src_location = os.getcwdu()
        baseurl = QUrl.fromLocalFile(os.path.join(src_location, "resources/"))
        self.webView_2.setHtml(self.post_content, baseurl)




app = QApplication(sys.argv)
dictionary = Dictionary()
dictionary.show()

app.exec_()