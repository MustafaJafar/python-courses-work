from flask import Flask

app = Flask (__name__)

@app.route('/') #/ == home page
def home ():
    return "Home Page!"

@app.route('/about/') 
def about ():
    return "about Page!"

if __name__ == "__main__" :
    app.run(debug = True)