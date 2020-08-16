from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'
app.add_url_rule('/1', 'hello', hello_world)

@app.route('/hello/<name>/')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/add/<float:num1>+<float:num2>/')
def add_num(num1,num2):
   return '%.2f' %(num1 + num2)

if __name__ == '__main__':
    app.debug = True
    app.run(port='5555')