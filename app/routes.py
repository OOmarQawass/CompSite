from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
@app.route('/')
def Parts(): return render_template('Parts Lists.html')

if __name__ == '__main__':
    app.run(debug=True)