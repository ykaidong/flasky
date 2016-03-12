#!/usr/bin/python
#coding: utf8

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

home = Blueprint('home',
        __name__,
        # 绝对路径为 /home/templates , 下同
        template_folder = 'templates',
        static_folder = 'static',
        # static_url_path必须指定
        # 否则如果不指定前缀的话flask将不会到/home/static中寻找静态文件
        static_url_path = '/home/static')

# 最好在将模板名称前加蓝本前缀
# 因为即使在实例化 Blueprint 时指定了模板位置
# 如果一旦有两个templates目录下的模板名称相同
# flask将会渲染一个.
# 比如/home/templates下有一个index.html
# /blog/templates下也有一个index.html
# 访问两个不同的index.html
# flask将会将两个页面全用其中先找到的模板渲染(不确定)
@home.route('/')
def home_index():
    return render_template('home_index.html')


@home.route('/project')
def home_project():
    try:
        return render_template('home_project.html')
    except TemplateNotFound:
        abort(404)


