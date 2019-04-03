import pygame,sys
import math
pygame.init()
size = width,height = 1280,720
rotating = False
theta = 0
speed = [2,2]
black = 0,0,0
PI = 3.1416
screen = pygame.display.set_mode(size)
class Vector3:
 def __init__(self,x,y,z):
  self.x = x
  self.y = y
  self.z = z
 def distance(self,othervec):
  return math.sqrt((self.x-othervec.x)*(self.x-othervec.x)+(self.y-othervec.y)*(self.y-othervec.y)+(self.z-othervec.z)*(self.z-othervec.z))

class Line3d:
 def __init__(self, start,end):
  self.start = start
  self.end = end
 
vec1 = Vector3(20,20,30)
vec2 = Vector3(0,10,40)
camerapos = Vector3(height/2,width/2,2)
sampleline = Line3d(vec1,Vector3(height/2,width/2,10))
alllines = []
#alllines.append(sampleline)
vectorsmoved = []
class Model:
 def __init__(self, linelist):
  self.linelist = linelist
    
vec3 = Vector3(10,10,10)
vec4 = Vector3(10,20,10)
line1 = Line3d(vec3,vec4)
alllines.append(line1)
vec5 = Vector3(20,10,10)
line2 = Line3d(vec3,vec5)
alllines.append(line2)
vec6 = Vector3(10,10,20)
line3 = Line3d(vec3,vec6)
alllines.append(line3)
vec7 = Vector3(10,20,20)
vec8 = Vector3(20,20,20)
vec9 = Vector3(20,10,20)
vec10 = Vector3(20,20,10)
line4 = Line3d(vec4,vec7)
alllines.append(line4)
line5 = Line3d(vec6,vec7)
alllines.append(line5)
line6 = Line3d(vec7,vec8)
alllines.append(line6)
line7 = Line3d(vec6,vec9)
alllines.append(line7)
line8 = Line3d(vec8,vec10)
alllines.append(line8)
line9 = Line3d(vec8,vec9)
alllines.append(line9)
line10 = Line3d(vec9,vec5)
alllines.append(line10)
line11 = Line3d(vec4,vec10)
alllines.append(line11)
line12 = Line3d(vec5,vec10)
alllines.append(line12)

class Camera:
 def __init__(self,startpos):
  self.startpos = startpos
 def drawlines(self,linelist,screen,cameraposition,colour):
  global PI
  global height
  global width
  asp = height/width 
  twicetanthetaovertwo = 2*math.tan(((PI/2)/2))
  for line in linelist:
   pxone = (width/2)+(100*(1*(1/(twicetanthetaovertwo/2))*line.start.x)/line.start.z)#1000*(line.start.x)/(camerapos.distance(line.start))#
   pyone = (height/2)+(100*(1*(1/(twicetanthetaovertwo/2))*line.start.y)/line.start.z)#1000*(line.start.y)/(camerapos.distance(line.start))#
   pxtwo = (width/2)+(100*(1*(1/(twicetanthetaovertwo/2))*line.end.x)/line.end.z)#1000*(line.end.x)/(camerapos.distance(line.end))    #
   pytwo = (height/2)+(100*(1*(1/(twicetanthetaovertwo/2))*line.end.y)/line.end.z)#1000*(line.end.y)/(camerapos.distance(line.end))   #
   pygame.draw.line(screen,colour,[pxone,pyone],[pxtwo,pytwo],1)  
   print(str(pxone)+","+str(pyone))
cam = Camera(camerapos)
while 1:
 for event in pygame.event.get():
  if(event.type == pygame.QUIT):
   sys.exit()
  if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            for line in alllines:
              if(line.start not in vectorsmoved):
               line.start.x -= 5
               vectorsmoved.append(line.start)
              if(line.end not in vectorsmoved):
               line.end.x -= 5
               vectorsmoved.append(line.end) 
            screen.fill(((0,0,0)))
            vectorsmoved = []   
        if event.key == pygame.K_RIGHT:
            for line in alllines:
              if(line.start not in vectorsmoved):
               line.start.x += 5
               vectorsmoved.append(line.start)
              if(line.end not in vectorsmoved):
               line.end.x += 5
               vectorsmoved.append(line.end) 
            screen.fill(((0,0,0)))
            vectorsmoved = []   

        if event.key == pygame.K_UP:
            for line in alllines:
              if(line.start not in vectorsmoved):
               line.start.z -= 25
               vectorsmoved.append(line.start)
              if(line.end not in vectorsmoved):
               line.end.z -= 25
               vectorsmoved.append(line.end) 
              if(line.start.distance(line.end) != 10):
               print("deformation")
            screen.fill(((0,0,0)))
            vectorsmoved = [] 
        if event.key == pygame.K_DOWN:
            for line in alllines:
              if(line.start not in vectorsmoved):
               line.start.z += 25
               vectorsmoved.append(line.start)
              if(line.end not in vectorsmoved):
               line.end.z += 25
               vectorsmoved.append(line.end) 
              if(line.start.distance(line.end) != 10):
               print("deformation")
            screen.fill(((0,0,0))) 
            vectorsmoved = []   
        if event.key == pygame.K_a:
         rotating = not rotating
      
 if(rotating):
   for line in alllines:
    if(line.start and line.end not in vectorsmoved):
     line.start.x = line.start.x +math.sin(theta)
     line.end.x =line.end.x + math.sin(theta)
     line.start.z = line.start.z + math.cos(theta)
     line.end.z = line.end.z + math.cos(theta)
     vectorsmoved.append(line.start)
     vectorsmoved.append(line.end)
   theta = theta + 1
   vectorsmoved = []
   screen.fill(((0,0,0))) 
 cam.drawlines(alllines,screen,Vector3(height/2,width/2,0),(255,255,255)) 




 


 

 pygame.display.flip()

