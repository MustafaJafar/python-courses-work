#from motion_detector import df
import pandas
from bokeh.plotting import figure , show , output_file
from bokeh.models import HoverTool , ColumnDataSource

df = pandas.read_csv("Times.csv", parse_dates = ["Start" , "End"])

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

p = figure(x_axis_type = 'datetime' , height = 100 , width = 500 , title = "Motion Graph")
p.xaxis.minor_tick_line_color=None
p.ygrid[0].ticker.desired_num_ticks = 1 #remove the grid 

hover = HoverTool(tooltips = [("Start","@Start_string") , ("End","@End_string")])
p.add_tools(hover)

q = p.quad(left = "Start" ,right ="End" , bottom = 0 , top = 1 , color = 'green' , source = cds )

output_file('6_motion_graph.html')
show(p)