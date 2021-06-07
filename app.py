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
    	
    	ingredient = flask.request.form['ingredient']

    	choices = data_pipeline.go(zip_code, store_name)
    	
    	chosen = data_pipeline.filter_function(choices, ingredient)
    	
    	if len(chosen) == 0:
    		
    		messaged = "No products fit your description unfortunately! Come back another time!"
    	
    	else:
    	
    		messaged = data_pipeline.webify(chosen)
    	
    	return render_template('index.html', waiting = messaged, viewing = store_name)


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

if __name__ == '__main__':
    app.run()
    
