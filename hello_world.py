#Using More Routes
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello ():
  return 'Open a new tab and enter /Welcome/name for URL'

@app.route('/Welcome/<name>')
def Welcome_name(name):
  return 'Welcome ' + name + '!'

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)