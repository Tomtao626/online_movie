#!/usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:tom_tao626
@license: Apache Licence
@contact: tp320670258@gmail.com
@software: PyCharm
"""

from app import app
import sys
import os
from flask_script import Manager, Server

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, os.path.join(BASE_DIR, 'movie_project\\app'))
# sys.path.insert(0, os.path.join(BASE_DIR, 'movie_project\\app\\admin'))
# sys.path.insert(0, os.path.join(BASE_DIR, 'movie_project\\app\\home'))

manage = Manager(app)
manage.add_command("runserver", Server(host="0.0.0.0", use_debugger=True))

if __name__ == "__main__":
    manage.run()
