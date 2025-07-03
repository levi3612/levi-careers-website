from flask import Flask

appp = Flask(__name__)

@appp.route('/')
def hello_world():
  return 'Hello, World!'

if __name__ == '__main__':
  appp.run(debug=True, host='0.0.0.0')