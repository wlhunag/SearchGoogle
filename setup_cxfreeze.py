#-*- coding: utf-8-*-
__author__ = 'Aaron'
from cx_Freeze import setup, Executable
import sys
#base = None
if sys.platform == "win32":
    base = "Win32GUI"

#因為已經包含下列檔案了，所以就comment掉了
includefiles= ['qtui', 'resources','imageformats']

includes = ['sip','PyQt4.QtNetwork']


setup(
        name = u"Loosen",
        version = "0.1",
        description = u"查資料程式",
        options = {'build_exe': {'include_files':includefiles}},
        executables = [Executable("loosen.py" ,base = base, icon = "resources/rock.ico")])