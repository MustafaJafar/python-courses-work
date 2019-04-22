from flask import Flask , render_template as rt

app = Flask (__name__)

@app.route('/') #/ == home page
def home ():
    return rt("home.html")

@app.route('/about/') 
def about ():
    return rt("about.html")

if __name__ == "__main__" :
    app.run(debug = True)