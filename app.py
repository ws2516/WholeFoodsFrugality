import flask
import gunicorn
import models
import gspread
import poker_sign_up
import tabulate

from flask import Flask, request, render_template, session, redirect

app = flask.Flask(__name__, template_folder='templates', static_folder = 'assets')

@app.route('/')
def main():
    return flask.render_template('index.html')


@app.route('/POTD', methods=['GET', 'POST'])
def potdTracker():

    if flask.request.method == 'GET':

        return(flask.render_template('format_comment.html'))

    if flask.request.method == 'POST':
    	
    	Record = flask.request.form['Record']
    	
    	ROI = flask.request.form['ROI']
    	
    	Net_units = flask.request.form['Net_Units']
    	
    	Sport = flask.request.form['Sport']
    	
    	League = flask.request.form['League']
    	
    	Time = flask.request.form['Time']
    	
    	Pick = flask.request.form['Pick']
    	
    	Odds = flask.request.form['Odds']
    	
    	Units = flask.request.form['Units']
    	
    	Write_Up = flask.request.form['Write_Up']
    	
    	messaged = POTD.format_correctly(Record, 
        							ROI,
        							Net_units,
        							Sport,
        							League,
        							Time,
        							Pick,
        							Odds,
        							Units,
        							Write_Up)
    	if db.session.query(potdTrack).filter(potdTrack.win == 7).count() == 0:
        	data = potdTrack(3, 2, 1, 'MLM', 32.5, 12.3, 12)
        	db.session.add(data)
        	db.session.commit()
        	return render_template('format_comment_display.html', result = messaged)
        	
    	return render_template('format_comment_display.html', result = messaged)


@app.route('/intelligentpoker', methods=['GET', 'POST'])
def poker_ai():

    if flask.request.method == 'GET':

        return(flask.render_template('intelligentpoker.html'))

    if flask.request.method == 'POST':
    	
    	email = flask.request.form['Email']
    	
    	waiting_number = poker_sign_up.write_to_sheet(email)
    	
    	return render_template('intelligentpokerthankyou.html', waiting = waiting_number)
    	 
@app.route('/contact')
def contact_page():
    return flask.render_template('Contact.html')


if __name__ == '__main__':

    app.run()
    
