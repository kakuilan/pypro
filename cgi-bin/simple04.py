#!/usr/bin/python3
# coding: utf-8
# 使用HTML表单的CGI脚本

import cgi

form = cgi.FieldStorage()
name = form.getvalue('name', 'world')
print("""Content-type: text/html

<html>
  <head>
    <title>Greeting Page</title>
  </head>
  <body>
    <h1>Hello, {}!</h1>
    <form action=''>
    Change name <input type='text' name='name' />
    <input type='submit' />
    </form>
  </body>
</html>
""".format(name))
