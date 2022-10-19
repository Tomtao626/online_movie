#!/usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:tom_tao626
@license: Apache Licence
@contact: tp320670258@gmail.com
@software: PyCharm
"""

from flask import Blueprint

admin = Blueprint("admin",__name__)

import app.admin.views