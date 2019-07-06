this project is inspired by : https://github.com/oscarwestberg/Face-Tracking-Maya

But I think that my code is easier to understand, maybe beacuse it is written in PYTHON ! 

any way, I made this project as my graduation project at

    University of Benha Shoubra Faculty Of Engineering
    Computer and electronics department
    


## Goals 

In this project, I tried to break the final goal into smaller goals 

the final goal : simple facial motion capture 

the smaller goals : 

    1.detect one mark
    2.track one mark's motion
    3.detect 12 marks (simulated version)
    4.sort those 12 marks 
    5.track and transfer motion data of the simulated version
    6.track and transfer motion data of a real face 
    
## Algorithm    

the algorithm used to detect marks :
note : marks are white points put on someone's face

    1.apply color segmentation (to select specific range of colors)
    2.apply binary threshold (to more filtration)
    3.apply blob detection (to detect marks' position) 
    4.sort points to follow the refrence image
    5.compare current marks' positions to previous marks' postions 
    6.send data via socket 
    
pieces of that algorithm can be found in the smaller goals 
and the final goal where you can find the full algorithm 

the algorithm is inspired by : https://www.youtube.com/watch?v=2R4iKC4xgOw

## Main Problem

problems I faced : 
    
    problems with camera setup and lighting 
    so, to deal with it I made a marks simulation 
    it simulates the marks on someone's face and thier motion
    the simulation is made in maya software, 
    you can find it in marks_simulation\source
    also you will find the resultant 3d head model motion

## How to run the examples : 

Note : there are 2 source directories 

    1.marks_simulation\source
          where you find : 
                simulation maya scene 
                voldmorts resultant motion of simulation
    2.marks_real_capture\source
          where you find : 
                voldmorts resultant motion of the simple motion capture

the proper way to run my code : 

    1.open maya project folder pick anyone of the two voldmorts mentioned above
    2.open maya scene "found in \scenes"
    3.run TCP server socket "found in \scripts "
    4.run either 7_marks_sim_maya.py or 8_marks_real_capture.py
          it depends on what you want to do 
              7_ : is the simulation version and expects a video of white points
              8_ : is the real facial motion capture and it expects 
                      1.A camera input
                      2.A face with the 12 marks attached 
                     
you can see these steps in this test video :      
https://drive.google.com/open?id=1Ivs5CZLS8JNYfgk1mz5H2kWbkTm3t9jg
    
Note : in the video you will see that script hangs down many times
as the code expects 12 points, and I had some problems with camera setup and lighting. 

### last but not least
  the project is considerd as a simple prototype        
  alot of prarameters needed to be tested     
  alot of math needed to be added       
  and I hope you have enjoyed ^^ 
