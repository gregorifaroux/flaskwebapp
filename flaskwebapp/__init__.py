from flask import Flask, render_template, request
app = Flask(__name__)

import flaskwebapp.utils as myutils


@app.route('/')
def home() -> 'html':
	return render_template('entry.html', page_title='Play with Functions')

@app.route('/findcommonletters', methods=['POST'])
def findcommonletters() -> 'html':
  results = myutils.find_common_letters(request.form['sentence'], request.form['letters'])
  return render_template('results.html', results_title='Common Letters:', the_results = results)

@app.route('/countvowels', methods=['POST'])
def countvowels() -> 'html':
  results = myutils.count_vowels(request.form['sentence'])
  return render_template('results.html', results_title='Vowels Count:', the_results = results)

app.run()
