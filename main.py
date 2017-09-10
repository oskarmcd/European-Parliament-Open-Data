import csv
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('profile_page.html', country="A", twitter="@A", party="EPP", name="Oskar", photo="https://scontent-vie1-1.xx.fbcdn.net/v/t1.0-9/14716223_1515727901801116_440836942848701398_n.jpg?oh=206913df1d441f05ad8714acee587f71&oe=5A576ABC")

@app.route('/<name>')
def generate_profile(name):
	name = name.split('-')
	with open('mep.csv', 'r', encoding="utf8") as csvfile:
		reader = csv.DictReader(csvfile)
		for lines in reader:
			if all(names.lower() in lines['NAME'].lower() for names in name):
				return render_template('profile_page.html', name=lines['NAME'], country=lines['NATIONALITY'], group=lines['GROUP'], twitter=lines['SCREEN_NAME'], twitter_link=lines['TWITTER_URL'])
		return render_template('404.html'), 404