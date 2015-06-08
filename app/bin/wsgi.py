#!/usr/bin/python
# -*- coding: utf-8 -*-
#@(#)----------------------------------------------------------------------
#@(#) OBJET            : WSGI entry point
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

#standard
import os
import logging
import json
#installed
import keyring
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
#custom
from net.shksystem.common.utils import init_logger
from net.shksystem.web.feed.routes import app as application
from net.shksystem.web.feed.models import db as database

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

# -- FLASK ALCHEMY
# -------------------------------------------------------------------------
migrate = Migrate(application, database)
manager = Manager(application)
manager.add_command('db', MigrateCommand)

#==========================================================================
# Main
#==========================================================================

if __name__ == '__main__':
    application.config['DEBUG'] = True
    manager.run()

#==========================================================================
# End sequence
#==========================================================================
#0
