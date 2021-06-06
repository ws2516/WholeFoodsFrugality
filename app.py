import flask
import gunicorn
import model
import gspread
import tabulate
import email_sign_up
import os
import data_pipeline

from flask import Flask, request, render_template, session, redirect
from flask import send_from_directory

app = flask.Flask(__name__, template_folder='templates', static_folder = 'assets')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':

        return(flask.render_template('index.html'))
        
    if flask.request.method == 'POST':
    	
    	zip_code = flask.request.form['ZIP']
    	
    	store_name = flask.request.form['store_name']

    	messaged = data_pipeline.go(zip_code, store_name)
    	
    	return render_template('index.html', waiting = messaged)


@app.route('/FutureProjects')
def further_suggestions():
	return flask.render_template('FutureProjects.html')
    	 
@app.route('/About')
def contact_page():
    return flask.render_template('About.html')

@app.route('/SignUp', methods=['GET', 'POST'])
def sign_up_sheet():

    if flask.request.method == 'GET':

        return(flask.render_template('SignUp.html'))

    if flask.request.method == 'POST':
    	
    	email = flask.request.form['Email']
    	
    	waiting_number = email_sign_up.write_to_sheet(email)
    	
    	return render_template('SignUpThankYou.html', waiting = waiting_number)

@app.errorhandler(500)
def pageNotFound(error):
    return flask.render_template('505.html')
    
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'assets'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run()
    
