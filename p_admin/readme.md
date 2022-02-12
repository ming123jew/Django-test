###学习笔记

创建项目
django-admin startproject mysite

最外层的:file: mysite/ 根目录只是你项目的容器， Django 不关心它的名字，你可以将它重命名为任何你喜欢的名字。
manage.py: 一个让你用各种方式管理 Django 项目的命令行工具。你可以阅读 django-admin and manage.py 获取所有 manage.py 的细节。
里面一层的 mysite/ 目录包含你的项目，它是一个纯 Python 包。它的名字就是当你引用它内部任何东西时需要用到的 Python 包名。 (比如 mysite.urls).
mysite/__init__.py：一个空文件，告诉 Python 这个目录应该被认为是一个 Python 包。如果你是 Python 初学者，阅读官方文档中的 更多关于包的知识。
mysite/settings.py：Django 项目的配置文件。如果你想知道这个文件是如何工作的，请查看 Django settings 了解细节。
mysite/urls.py：Django 项目的 URL 声明，就像你网站的“目录”。阅读 URL调度器 文档来获取更多关于 URL 的内容。
mysite/wsgi.py：作为你的项目的运行在 WSGI 兼容的Web服务器上的入口。阅读 如何使用 WSGI 进行部署 了解更多细节。

启用一个http服务器，不能用于开发环境，挂到nginx上面
python manage.py runserver

创建投票应用
 python manage.py startapp polls


https://docs.djangoproject.com/zh-hans/2.0/intro/tutorial02/

改变模型需要这三步：

编辑 models.py 文件，改变模型。
运行 python manage.py makemigrations 为模型的改变生成迁移文件。
运行 python manage.py migrate 来应用数据库迁移。
( python manage.py sqlmigrate polls 0001 查看sql)



最后在StackOverflow上找到此问题，回答说原因是django3.1之后的版本均有发现此问题，我使用的版本为3.0同样会出现此问题。
最终解决方式将settings中的

防止报错，修改
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}


Django 测试工具之 Client (测试视图)
python manage.py shell
from django.test.utils import setup_test_environment
setup_test_environment()
from django.test import Client
client = Client()
response = client.get('/')
response.status_code

from django.urls import reverse
response = client.get(reverse('polls:index'))
response.status_code
response.content

Django - LiveServerTestCase (Selenium 测试)
python3 -m pip install selenium


题外话
class A(object):
    a = 'a'
    @staticmethod
    def foo1(name):
        print 'hello', name
    def foo2(self, name):
        print 'hello', name
    @classmethod
    def foo3(cls, name):
        print 'hello', name
既然@staticmethod和@classmethod都可以直接类名.方法名()来调用，那他们有什么区别呢
从它们的使用上来看,
@staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。
@classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数。
如果在@staticmethod中要调用到这个类的一些属性方法，只能直接类名.属性名或类名.方法名。
而@classmethod因为持有cls参数，可以来调用类的属性，类的方法，实例化对象等，避免硬编码。