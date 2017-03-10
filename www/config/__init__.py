#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Cleanse'

# 数据库默认设置
db_config = {
    'user': 'root',
    'password': 'root',
    'db': 'mblog'
}

# jinja2默认设置
jinja2_config = dict()

# cookie默认设置
COOKIE_NAME = 'aweSession'
COOKIE_KEY = 'MBlog'

__all__ = ['db_config', 'jinja2_config', 'COOKIE_NAME', 'COOKIE_KEY']
