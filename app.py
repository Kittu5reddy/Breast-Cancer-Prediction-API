
import main
from flask import Flask, render_template, request


app = Flask(__name__)

app.config['SECRET_KEY'] = "secretkey"

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        inp = request.form['in']
        
        return render_template('predict.html', out = main.predict(inp))
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)