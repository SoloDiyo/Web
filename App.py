from flask import Flask,render_template

app = Flask('app',template_folder='Templates')

@app.route('/')
def hello():
    return render_template('Home.html')
@app.route('/start')
def GetStarted():
    return render_template('GetStarted.html')
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)
