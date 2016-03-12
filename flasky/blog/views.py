#coding: utf8

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

# 实例化Blueprint时指定模板目录与静态目录
blog = Blueprint('blog', 
        __name__, 
        template_folder = 'templates',
        static_folder = 'static')

@blog.route('/')
def blog_index():
    try:
        return render_template('blog_index.html')
    except TemplateNotFound:
        abort(404)



@blog.route('/about')
def blog_about():
    try:
        return render_template('blog_about.html')
    except TemplateNotFound:
        abort(404)
