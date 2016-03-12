#!/usr/bin/python
#coding: utf8

from flask import Flask, render_template
from .blog.views import blog
from .home.views import home

app = Flask(__name__,
        # template_folder = 'template',
        # static_folder = 'static',
        )


# 注册蓝本, 不使用前缀
# 即站点的根目录的视图由"home"这个蓝本处理
app.register_blueprint(home)

# /blog下的视图由blog这个蓝本处理
app.register_blueprint(blog, url_prefix = '/blog')


# 自定义404页面
@app.errorhandler(404)
def error_404(e):
    return render_template('404.html'), 404

