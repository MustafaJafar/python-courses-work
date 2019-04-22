from pandas_datareader import data
from datetime import datetime as dt
from bokeh.plotting import figure , show , output_file
from bokeh.embed import components
from bokeh.resources import CDN #content delivery network
from flask import Flask , render_template as rt

app = Flask (__name__)

@app.route('/plot/')
def plot():
    start = dt(2018,11,1)  #  1/1/2019
    end = dt(2019,3,12)   # 12/3/2019
    df = data.DataReader(name = "AAPL" , data_source = "yahoo" , start = start , end = end )

    def Inc_dec(c,o):
        if c > o : 
            value = "Increase"
        elif c < o :
            value = "Decrease"
        else :
            value = "Equal"
        return value
            
    df["Status"] = [Inc_dec(c,o) for c , o in zip(df.Close , df.Open)]
    df["Middle"] = (df.Open+df.Close)/ 2
    df["Diff"] = abs(df.Open-df.Close)


    p = figure (x_axis_type ='datetime' , width = 1000 , height = 300 ,title = "Apple Stock Analysis nov2018-mar 2019" , sizing_mode = 'scale_width')
    p.yaxis.axis_label= "USD" 
    p.grid.grid_line_alpha = 0.3 

    p.segment(df.index , df.High , df.index ,df.Low , color = "#7c7c7c")

    hours_12 = 12 * 60 * 60 * 1000 #milliseconda  
    
    p.rect(df.index[df.Status == "Increase"] , df.Middle[df.Status == "Increase"] , hours_12 ,df.Diff[df.Status == "Increase"] , fill_color = "#86d88a" , line_color = "#2a442b")
    p.rect(df.index[df.Status == "Decrease"] , df.Middle[df.Status == "Decrease"] , hours_12 ,df.Diff[df.Status == "Decrease"] , fill_color = "#d88686" , line_color = "#442a2a")


    script1 , div1,  = components(p)
    cdn_js = CDN.js_files[0]
    cdn_css = CDN.css_files[0]
    return rt("plot.html" , script1 = script1 , div1 = div1 , cdn_js = cdn_js , cdn_css = cdn_css )



@app.route('/') #/ == home page
def home ():
    return rt("home.html")

@app.route('/about/') 
def about ():
    return rt("about.html")


if __name__ == "__main__" :
    app.run(debug = True)  #runs on local host
    #app.run(host='0.0.0.0') #runs on local network
    