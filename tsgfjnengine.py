import pygame,sys
import math
import random
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
class Lightsource:
 def __init__(self,origin,intensity,baser,baseg,baseb):
  self.origin = origin
  self.intensity = intensity# 0-1
  self.baser = baser#0-1
  self.baseg = baseg#0-1
  self.baseb = baseb#0-1
 def calculation(self,start,end,line):
  origin = self.origin
  relativeintensity = 100*self.intensity/((origin.distance(start)+origin.distance(end)/2)*(origin.distance(start)+origin.distance(end)/2))
  returnr = relativeintensity*line.colourr*self.baser
  returng = relativeintensity*line.colourg*self.baseg
  returnb = relativeintensity*line.colourb*self.baseb
  print(returng)
  return (returnr,returng,returnb)

class Cube:
 def __init__(self,size,origin):
  self.size = size
  self.origin = origin
  self.cubelines = []
 def activate(self):
  global alllines
  origin = self.origin
  size = self.size
  self.cubelines = []
  self.cubelines.append(Line3d(Vector3(origin.x-(size/2),origin.y-(size/2),origin.z-(size/2)),Vector3(origin.x-(size/2),origin.y-(size/2),origin.z+(size/2)))) 
  #
  self.cubelines.append(Line3d(Vector3(origin.x-(size/2),origin.y-(size/2),origin.z-(size/2)),Vector3(origin.x-(size/2),origin.y+(size/2),origin.z-(size/2)))) 
  #
  self.cubelines.append(Line3d(Vector3(origin.x-(size/2),origin.y-(size/2),origin.z-(size/2)),Vector3(origin.x+(size/2),origin.y-(size/2),origin.z-(size/2)))) 
  #
  self.cubelines.append(Line3d(Vector3(origin.x-(size/2),origin.y-(size/2),origin.z+(size/2)),Vector3(origin.x+(size/2),origin.y-(size/2),origin.z+(size/2)))) 
  #
  #self.cubelines.append(Line3d(Vector3(origin.x-(size/2),origin.y-(size/2),origin.z+(size/2)),Vector3(origin.x+(size/2),origin.y+(size/2),origin.z-(size/2)))) 
  #
  self.cubelines.append(Line3d(Vector3(origin.x-(size/2),origin.y-(size/2),origin.z+(size/2)),Vector3(origin.x-(size/2),origin.y+(size/2),origin.z+(size/2))))
  #
  self.cubelines.append(Line3d(Vector3(origin.x+(size/2),origin.y-(size/2),origin.z-(size/2)),Vector3(origin.x+(size/2),origin.y-(size/2),origin.z+(size/2))))
  #
  self.cubelines.append(Line3d(Vector3(origin.x+(size/2),origin.y-(size/2),origin.z-(size/2)),Vector3(origin.x+(size/2),origin.y+(size/2),origin.z-(size/2))))  
  #
  self.cubelines.append(Line3d(Vector3(origin.x+(size/2),origin.y+(size/2),origin.z-(size/2)),Vector3(origin.x+(size/2),origin.y+(size/2),origin.z+(size/2))))  
  #
  self.cubelines.append(Line3d(Vector3(origin.x-(size/2),origin.y+(size/2),origin.z-(size/2)),Vector3(origin.x-(size/2),origin.y+(size/2),origin.z+(size/2)))) 
  #
  self.cubelines.append(Line3d(Vector3(origin.x-(size/2),origin.y+(size/2),origin.z-(size/2)),Vector3(origin.x+(size/2),origin.y+(size/2),origin.z-(size/2))))
  #
  self.cubelines.append(Line3d(Vector3(origin.x-(size/2),origin.y-(size/2),origin.z+(size/2)),Vector3(origin.x+(size/2),origin.y-(size/2),origin.z+(size/2))))  
  #
  self.cubelines.append(Line3d(Vector3(origin.x-(size/2),origin.y-(size/2),origin.z+(size/2)),Vector3(origin.x-(size/2),origin.y+(size/2),origin.z+(size/2))))  
  #
  self.cubelines.append(Line3d(Vector3(origin.x-(size/2),origin.y+(size/2),origin.z+(size/2)),Vector3(origin.x+(size/2),origin.y+(size/2),origin.z+(size/2))))
  #
  self.cubelines.append(Line3d(Vector3(origin.x+(size/2),origin.y+(size/2),origin.z-(size/2)),Vector3(origin.x+(size/2),origin.y+(size/2),origin.z+(size/2))))    
  #
  self.cubelines.append(Line3d(Vector3(origin.x+(size/2),origin.y-(size/2),origin.z+(size/2)),Vector3(origin.x+(size/2),origin.y+(size/2),origin.z+(size/2))))  
  for line in self.cubelines:
   alllines.append(line)

class Line3d:
 def __init__(self, start,end):
  self.start = start
  self.end = end
  self.colourr = 255
  self.colourg = 255
  self.colourb = 255
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
  self.xdraw = []
  self.ydraw = []
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
   #pygame.draw.line(screen,colour,[pxone,pyone],[pxtwo,pytwo],1)  
   self.drawline(screen,colour,pxone,pyone,pxtwo,pytwo,line)
   #print(str(pxone)+","+str(pyone))
 def drawline(self,screen,colour,pxone,pyone,pxtwo,pytwo,line):
  i = 0
  res = 4
  wdif = pxone-pxtwo
  hdif = pyone-pytwo
  worldspacexcoords = []
  worldspaceycoords = []
  worldspacezcoords = []     
  worldspacexcoords , worldspaceycoords , worldspacezcoords  = self.divide3d(line)
  xcoords = []
  ycoords = [] 
  i = 0
  xcoords,ycoords = self.divide(pxone,pyone,pxtwo,pytwo)
  
  #pygame.draw.line(screen,colour,[pxone,pyone],[math.floor((pxone+pxtwo)/2),math.floor((pyone+pytwo)/2)],1)

  
  #pygame.draw.line(screen,(100,0,200),[math.floor((pxone+pxtwo)/4),math.floor((pyone+pytwo)/4)],[math.floor((pxone+pxtwo)/2),math.floor((pyone+pytwo)/2)],1)
  
  #pygame.draw.line(screen,(0,0,200),[math.floor((pxone+pxtwo)/2),math.floor((pyone+pytwo)/2)],[pxtwo,pytwo],1)


    

  #for a in range(1,res):
   #xcoords.append(a*((pxone+pxtwo)/res))
  # ycoords.append(a*((pyone+pytwo)/res))
  #pygame.draw.line(screen,colour,[pxone,pyone],[xcoords[0],ycoords[0]],1)
  for b in range(0,len(xcoords) -1):
   pygame.draw.line(screen,light.calculation(Vector3(worldspacexcoords[b],worldspaceycoords[b],worldspacezcoords[b]),Vector3(worldspacexcoords[b+1],worldspaceycoords[b+1],worldspacezcoords[b+1]),line),[xcoords[b],ycoords[b]],[xcoords[b+1],ycoords[b+1]],1)     
  
  
 def divide(self,pxone,pyone,pxtwo,pytwo,res=2):
  pass
  xcoords = []
  ycoords = []
  
  x = pxone
  y = pytwo
  fx = pxtwo
  fy = pytwo
  i = 4
  deltax = pxtwo-pxone
  deltay = pytwo - pyone
  for i in range(0,100):
    ycoords.append(deltay*(i/100)+ pyone) 
    xcoords.append(deltax*(i/100)+pxone)
  return xcoords,ycoords
  if(res > 0):
   pass
  else:
   pass
  
 def divide3d(self,line):
  startx = line.start.x
  starty = line.start.y
  startz = line.start.z
  endx = line.end.x
  endy = line.end.y
  endz = line.end.z
  deltax = endx - startx
  deltay = endy - starty
  deltaz = endz - startz
  returnx = []
  returny = []
  returnz = []
  for i in range(0,100):
   returnx.append(deltax*(i/100)+startx)
   returny.append(deltay*(i/100)+starty)
   returnz.append(deltaz*(i/100)+startz)
  return returnx,returny,returnz



  







 def screendistance(self,pxone,pyone,pxtwo,pytwo):
  return int(math.ceil(math.sqrt(((pxone-pxtwo)*(pxone-pxtwo))+((pyone-pytwo)*(pyone-pytwo))))) 
  

light = Lightsource(Vector3(30,30,30),1,0.4,1,1)
cam = Camera(camerapos)
cube = Cube(20,Vector3(30,30,30))
cube.activate()
cube2 = Cube(10,Vector3(140,140,140))
cube2.activate()
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
 print (len(alllines))



 


 

 pygame.display.flip()
