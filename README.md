
#flasky#

这是使用flask的blueprint(蓝本)进行模块化的一个示例.

其中有两个蓝本:
home 和 blog

home接管站点根目录下的视图,
blog接管/blog这一级目录下的视图. 

直接运行run.py, 然后打开浏览器即可看到结果.


目录结构:
.  
├── flasky  
│   ├── blog  
│   │   ├── __init__.py  
│   │   ├── static  
│   │   │   └── css  
│   │   │       └── style.css  
│   │   ├── templates  
│   │   │   ├── blog_about.html  
│   │   │   └── blog_index.html  
│   │   └── views.py  
│   ├── home  
│   │   ├── __init__.py  
│   │   ├── static  
│   │   │   └── css  
│   │   │       └── style.css  
│   │   ├── templates  
│   │   │   ├── 404.html  
│   │   │   ├── home_index.html  
│   │   │   └── home_project.html  
│   │   └── views.py  
│   └── __init__.py  
├── README.md  
├── requirements.txt  
└── run.py  

