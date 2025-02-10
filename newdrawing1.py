from turtle import * 
from random import randint 

bgcolor('black') 
x = 1 
speed(0) 
while x < 400: 
  
 r = randint(0,255) 
 g = randint(0,255)  
 b = randint(0,255) 
  
 colormode(255)  
 pencolor(r,g,b) 

 circle(x)
 rt(60)

 x = x+5
  
exitonclick() 
