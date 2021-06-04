import flask
import gunicorn
import model
import gspread
import tabulate
from model import combination_file

from flask import Flask, request, render_template, session, redirect

app = flask.Flask(__name__, template_folder='templates', static_folder = 'assets')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':

        return(flask.render_template('index.html'))
        
    if flask.request.method == 'POST':
    	
    	zip_code = flask.request.form['ZIP']

    	messaged = combination_file.go(zip_code)
    	
    	return render_template('index.html', waiting = messaged)


@app.route('/FutureProjects')
def further_suggestions():
	return flask.render_template('FutureProjects.html')
    	 
@app.route('/About')
def contact_page():
    return flask.render_template('About.html')


if __name__ == '__main__':
    app.run()
    
