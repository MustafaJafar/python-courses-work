import folium 
import pandas

def get_color(num):
    if (num >= 0 and num < 1000):
        return "green"
    elif(num >= 1000 and num < 3000):
        return "orange"
    elif(num >= 3000):
        return "red"


data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elve = list(data["ELEV"])
name = list(data["NAME"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target = "_blank">%s</a><br> 
Height : %s m
"""

map = folium.Map(location = [38.58,-99.09] , zoom_start = 6 , tiles = "Mapbox Bright")

v_fg = folium.FeatureGroup(name="Volcanoes")
#green : el < 1000 , orange = 1000 : 3000 , red > 3000
for lt , ln  , el , name in zip(lat,lon , elve , name) : #volcanoes points layer
    color = get_color(el)
    iframe = folium.IFrame(html = html % (name + " volcano" , name + " volcano" , el ) , width=200 , height = 100)
    v_fg.add_child(folium.CircleMarker(location = [lt,ln] , radius = 6 , popup =folium.Popup(iframe), fill_color = color , color = 'grey' , fill_opacity = 0.7))

p_fg = folium.FeatureGroup(name="Population")
p_fg.add_child(folium.GeoJson(data = open("world.json" , "r" , encoding ="utf-8-sig").read() , 
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else "orange" if 10000000 <= x['properties']['POP2005'] < 20000000 else "red"} )) #polygone layers


map.add_child(v_fg)
map.add_child(p_fg)
map.add_child(folium.LayerControl())

map.save("Map2.html") 
#popups with quotes(')
#popup = folium.Popup(str(el) , parse_html=True)

#3layers :polygone , population  , volcanoes' points