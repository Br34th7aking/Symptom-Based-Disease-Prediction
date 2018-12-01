from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.form:
        print(request.form)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
