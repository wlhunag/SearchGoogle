#-*- coding: utf-8-*-
__author__ = 'Aaron'

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
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
        websettings = self.webView_2.settings()
        websettings.setAttribute(QWebSettings.PluginsEnabled, True)
        self.browser_content = mechanize.Browser()
        self.browser_content.set_handle_robots(False)
        #還是會被Google 抓到耶，怎麼辦？
        self.browser_content.addheaders = [('User-agent', 'Mozilla')]
        self.updateresults()
        self.createconnection()

    def createconnection(self):
        self.pushButton_search.clicked.connect(lambda: self.analyse())
        self.tabWidget.currentChanged.connect(lambda: self.updateresults())
        self.treeWidget.itemClicked.connect(lambda: self.showhtml())
        self.pushButton_clear.clicked.connect(lambda: self.clearDB())

    def analyse(self):
        #以後還要改良這邊的演算法，現在是毫無演算法可言啦~
        text = unicode(self.QuestionText.toPlainText()).encode('utf-8')
        print(text)
        for subject in text.lstrip('\n').rstrip('\n').replace("   ", " ").replace("  ", " ").split('\n'):
            self.search(subject)

    def clearDB(self):
        os.remove(os.path.join(os.getcwdu(),"storage.db"))
        # con = sqlite3.connect('storage.db')
        # with con:
        #     cur = con.cursor()
        #     cur.execute('CREATE TABLE Questions(Qa TEXT, Results TEXT)')
        #     #這好像不是真正把資料去掉？？
        self.updateresults()

    def search(self, term):

        term = term.replace(" ", "+")
        query = 'http://www.google.com.tw/search?num=10&q=' + term
        self.htmltext = self.browser_content.open(query).read()
        #不知為何這邊編碼一定要mbcs，不然就會變亂碼？？
        #原本以為已經弄懂編碼了，結果又混亂了
        self.htmltext = re.subn(r"(?si)/url\?q=(.*?)&amp[^>]*", r'\1"', self.htmltext.decode('mbcs').replace("<b>","<b class=p>"))

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
        #這樣按 backspace 好像沒辦法回上一頁？
        self.webView_2.setHtml(self.post_content, baseurl)




app = QApplication(sys.argv)
dictionary = Dictionary()
dictionary.show()

app.exec_()