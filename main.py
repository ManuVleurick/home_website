from flask import Flask,render_template
import os
import sys

app = Flask(__name__)
host = '127.0.0.1'if len(sys.argv) == 1 else sys.argv[1] 
if os.getenv('FLASK_SECRET_KEY'):
    app.secret_key = os.getenv('FLASK_SECRET_KEY')
else:
    print('In development mode, no flask secret key as env var')
    app.secret_key = b'yoinkerbedoinkers'


@app.route('/')
def home():
    return render_template('home.html')


if __name__=='__main__':
    app.run(host=host,debug=True)