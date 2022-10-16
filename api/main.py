from flask import Flask, flash, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/upload')
def uploadFile():
    return redirect(request.url)


if __name__ == '__main__':
    app.run()