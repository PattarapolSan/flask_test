from flask import Flask, Blueprint
from controller.calculatorApi import caluclator_api


app = Flask(__name__)


app.register_blueprint(caluclator_api)

@app.route('/hello-world')
def hello():
    return "Hello, World!"


if __name__ == '__main__':
    app.run()