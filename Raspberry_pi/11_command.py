
import os

while 1 : 

	g = "" 
	g = raw_input('type something : \n',  )
	#print g
	#os.system( "clear" )
	if (g == 'esc' ) :
		print 'program ended'
 		break 
	else :
		os.system(g)
	
