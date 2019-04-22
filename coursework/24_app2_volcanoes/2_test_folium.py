import folium 
#create Map 
#map = folium.Map(location = [80,-100])#laitude : -90 to 90 , longitude : -180 to 180) 

#add marker
#map.add_child(folium.Marker(location = [80 , -100] , popup = "Hi I am a Marker" , icon = folium.Icon(color = "green")))

#save map
#map.save("Map1.html") 

map = folium.Map(location = [38.58,-99.09] , zoom_start = 6 , tiles = "Mapbox Bright")

#add Marker 
map.add_child(folium.Marker(location = [38.2 , -99.1] , popup = "Hi I am a Marker" , icon = folium.Icon(color = "green")))
#another method using a feature group
fg = folium.FeatureGroup(name="My Map")
for coordinates , colors in zip([[37,-99],[37,-97]] , ["orange","red"]) :
    fg.add_child(folium.Marker(location = coordinates , popup = "Hi I am another Marker" , icon = folium.Icon(color = colors)))

map.add_child(fg)

map.save("Map1.html") 

