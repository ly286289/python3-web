#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Cleanse'

from app.frame import get
from app.frame.halper import Page, set_valid_value
from app.models import Blog


# 测试
@get('/about')
async def about():
    return {
        '__template__': 'about.html'
    }


# 首页
@get('/')
async def index(*, tag='', page='1', size='10'):
    num = await Blog.countRows(where="position(? in `summary`)", args=[tag])
    page = Page(num, set_valid_value(page), set_valid_value(size, 10))
    if num == 0:
        blogs = []
    else:
        blogs = await Blog.findAll("position(? in `summary`)", [tag], orderBy='created_at desc', limit=(page.offset, page.limit))
    return {
        '__template__': 'uk-blogs.html',
        'blogs': blogs,
        'page': page,
        'tag': tag
    }


# 注册页面
@get('/register')
def register():
    return {
        '__template__': 'uk-register.html'
    }


# 登陆页面
@get('/signin')
def signin():
    return {
        '__template__': 'uk-signin.html'
    }


# 博客页面
@get('/blog/{id}')
async def get_bolg(id):
    blog = await Blog.find(id)
    return {
        '__template__': 'uk-blog.html',
        'blog': blog
    }


# 管理页面
@get('/manage')
def manage():
    return 'redirect:/manage/blogs'


# 管理用户、博客、评论
@get('/manage/{table}')
def manage_table(table):
    return {
        '__template__': 'uk-manage.html',
        'table': table
    }


# 创建博客
@get('/manage/blogs/create')
def manage_create_blog():
    return {
        '__template__': 'uk-blog_edit.html'
    }


# 修改博客
@get('/manage/blogs/edit')
def manage_edit_blog():
    return {
        '__template__': 'uk-blog_edit.html'
    }


# 谷歌验证
@get('/google8d8dd87f7b70fbc7.html')
def google_auth():
    return {
        '__template__': 'google8d8dd87f7b70fbc7.html'
    }
