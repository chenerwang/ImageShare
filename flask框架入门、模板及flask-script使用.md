### 一、.flask安装和框架
#### flask官网：http://flask.pocoo.org/
#### flask中文文档：http://dormousehole.readthedocs.io/en/latest/
#### 安装：`pip install flask`

- **最简单的flask应用**
    ```python
    from flask import Flask
    
    app = Flask(__name__)
    
    
    @app.route('/')
    def index():
        return 'hello'
    
    
    if __name__ == '__main__':
        app.run(debug=True)
    
    
    ```
    注:
    1. Ctrl+Alt+B：跳转到实现
    2. [装饰器](http://python.jobbole.com/85056/)：外部函数是装饰器的名字，返回一个装饰版的函数；内部函数是装饰器要实现的功能


- **路径映射**

    多映射：
    ```python
    @app.route('/index/')
    @app.route('/')
    def index():
        return 'hello'
    ```
    参数变量：< >
    ```python
    @app.route('/profile/<int:uid>/')
    def profile(uid):
        return 'profile:' + str(uid)
    ```

- **HTTP Method**

    - GET：获取接口信息
    - POST：提交数据到服务器
    - HEAD：紧急查看接口HTTP的头
    - PUT：支持[幂等性](http://www.cnblogs.com/weidagang2046/archive/2011/06/04/2063696.html)的POST
    - DELETE：删除服务器上的资源
    - OPTIONS：查看支持的方法
    

### 二、静态和模板文件
- 静态

    - 默认目录：statics/templates
    - 文件：css/js/images

- 动态
    - 目录：templates
    - 文件：html/htm

- jinja2模板语法

    - 文档：[中文版](http://docs.jinkan.org/docs/jinja2/) [英文版](http://jinja.pocoo.org/docs/dev/templates/)
    - {{变量/表达式}}
    - {% 语法 %}
    - {# 注释 #}
    - \# :行语法表达
    - filters
    - 模板继承：include, extends
    - call/macro

- request和response

    - request：参数解析、cookie读取、http请求子段、文件上传
    - response：页面内容返回、cookie下发、http字段设置，headers
    
- 重定向和Error

    - 重定向：301永久转移；302临时转移

- Flash message:

    - 发送：获取接口消息 flash(msg)
    - 获取：get_flashed_messages()
    - 属性：通过session传递消息

- Log：

### 三、flask-script

- [官网](http://flask-script.readthedocs.io/en/latest/)
- 安装：`pip install Flask-Script`
- 使用：

### 四、课后作业

- Flask库练习
- Jinja2模板语言练习
- 装饰器和HTTP协议复习
- Flask-Script安装使用