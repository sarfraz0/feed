#!/usr/bin/python
# -*- coding: utf-8 -*-
#@(#)----------------------------------------------------------------------
#@(#) OBJET            : Flask QT wrapper
#@(#)----------------------------------------------------------------------
#@(#) AUTEUR           : Sarfraz Kapasi
#@(#) DATE DE CREATION : 05.06.2015
#@(#) LICENSE          : GPL-3
#@(#)----------------------------------------------------------------------

#==========================================================================
#
# WARNINGS
# NONE
#
#==========================================================================

#==========================================================================
# Imports
#==========================================================================

# standard
import sys
import os
import time
import json
import logging
import urllib
# installed
import keyring
from PySide.QtGui import *
from PySide.QtWebKit import *
from PySide.QtCore import *
# custom
from net.shksystem.common.utils import init_logger
from net.shksystem.web.feed.routes import app as application

#==========================================================================
# Environment/Parameters/Static variables
#==========================================================================

# SCRIPT CONFIG
cnf = {}
with open(os.path.abspath('../etc/config.json')) as f:
    cnf = json.load(f)
# LOGGER
logger = init_logger(os.path.abspath(cnf['LOGFILE']), logging.INFO)
# FLASK CONFIG
application.config['APP_NAME'] = cnf['APP_NAME']
application.config['WTF_CSRF_ENABLED'] = True
application.config['SECRET_KEY'] = cnf['SECRET']
application.config['SQLALCHEMY_DATABASE_URI'] = cnf['DATABASE_URI']

#==========================================================================
# Classes/Functions
#==========================================================================

class WebApp(QThread):
    def setApplication(self, app, setup_callback):
        self.application = app
        self.setup_callback = setup_callback

    def run(self):
        self.setup_callback()
        self.application.run(port=cnf['APP_PORT']))

def main():
    global web, env

    # Init Flask server
    webappThread = WebApp()
    def setup_callback():
        # Do something specific here before app start
        pass
    webappThread.setApplication(application, setup_callback)
    webappThread.start()

    # Init QT app
    app = QApplication(sys.argv)

    # Setup WebView (WebKit)
    web = QWebView()
    web.resize(cnf['QT']['HORIZONTAL_RES'], cnf['QT']['VERTICAL_RES'])
    web.setWindowTitle(cnf['APP_NAME'])
    web.setWindowIcon(QIcon(os.path.abspath(cnf['FAVFILE'])))
    qr = web.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    web.move(qr.topLeft())

    web.setUrl('http://localhost:{0}'.format(cnf['APP_PORT'],))

    # Bind shut down
    def shutdown():
        webappThread.quit()
    app.aboutToQuit.connect(shutdown)

    # Start up
    web.show()
    sys.exit(app.exec_())

#==========================================================================
# Main
#==========================================================================

if __name__ == '__main__':
    main()

#==========================================================================
# End sequence
#==========================================================================
#0
