from flask import Flask 
import uuid 
app = Flask(__name__)

@app.route('/')
def index():
  return '''

  <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width>, initial-scale=1.0">
  <title>Flask - Basic</title>
</head>
<body>
  <h1>Home Page</h1>
</body>
</html>
  '''

  @app.route('/<name>')
  def show_name(name):
    return f'<h1>My name is {name}</h1>'

  @app.route('/hello/<name>')
  def hello(name):
    return f'<h1>Hello, {name}</h1>'

  @app.route('/greeting/<name>/<age>')
  def greeting(name, age):
    return f'<h1>My name is {name}. I am {age} years old.</h1>'

  @app.route('/calculate/addition/<int:a>/<int:b>')
  def subtraction(a, b):
    return f'<h1>{a} + {b} = {a+b}</h1>'

  @app.route('/secrekey/<uuid:sk>')
  def secret_key(sk):
    return f'my secret kay : {sk}'

#  if __name__ == '__main__':
#    app.run(debug=True)index.htmlindex.htmlindex.htmlindex.html








