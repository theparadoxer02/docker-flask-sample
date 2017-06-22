from flask import Flask
import requests

# the all-important app variable:
app = Flask(__name__)

@app.route("/")
def hello():
    return "Oh, Hello World <br><a href='/git'>view latest git author</a>"

@app.route("/git")
def git_author():
    url = 'https://api.github.com/events?per_page=200'
    headers = {'user-agent':'githubarchive.org'}
    r = requests.get(url, headers=headers)
    return r.json()[0]['actor']['login']

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)