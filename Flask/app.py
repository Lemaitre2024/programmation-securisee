import flask
from flask import request, render_template

app = flask.Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')    #Allow to be connected with the index.html pages

@app.route('/avis/', methods=['GET', 'POST']) # define the 2 methods get and post for the https request
def avis():
    if request.method == 'POST':        # if the post method is required, avis.html will be logged with the avis lauch in the formulaire.html
        avis = request.form['avis']
        return render_template('avis.html', avis=avis)
    return render_template('formulaire.html')       # 

if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug=True)

