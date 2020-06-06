# DataSet: Body temperature , Gender ,Heart rate
from itertools import combinations
import math
import random

def FindPointrect(x1, y1, x2,
              y2, x, y) :
    if (x >= x1 and x <= x2 and
        y >= y1 and y <= y2) :
        return True
    else :
        return False

def FindPointCircle(circle_x, circle_y, rad, x, y):

	# Compare radius of circle
	# with distance of its center
	# from given point
	if ((x - circle_x) * (x - circle_x) +
		(y - circle_y) * (y - circle_y) <= rad * rad):
		return True;
	else:
		return False;

def circle(point65) :
    List= list(combinations(point65,2))
    circle=[]
    mini,count1,count2 = float('inf'),float('inf'),float('inf')

    for i in range(len(List)):
        x1 , y1 , x2 , y2 = float(List[i][0][0]),float(List[i][0][2]),float(List[i][1][0]),float(List[i][1][2])
        rad = math.sqrt((x1-x2)**2+(y1-y2)**2)
        if mini>min(count1,count2):
            mini=min(count1,count2)
            circle=x1, y1, x2, y2
        #print (i,circle,count1,count2,mini)
        count1=0
        count2=0
        for j in range(len(point65)):
            x , y=float(point65[j][0]),float(point65[j][2])
            if FindPointCircle(x1, y1, rad, x, y) and float(point65[j][1])==2:
                count1+=1
            elif not FindPointCircle(x1, y1, rad, x, y) and float(point65[j][1])==1:
                count1+=1
        for j in range(len(point65)):
            x , y=float(point65[j][0]),float(point65[j][2])
            if FindPointCircle(x1, y1, rad, x, y) and float(point65[j][1])==1:
                count2+=1
            elif not FindPointCircle(x1, y1, rad, x, y) and float(point65[j][1])==2:
                count2+=1
    print ("min circle:",circle,mini)
    return circle,mini;

def rectangle(point65) :
    List= list(combinations(point65,2))
    rectangle=[]
    mini,count1,count2 = float('inf'),float('inf'),float('inf')

    for i in range(len(List)):
        x1 , y1 , x2 , y2 = float(List[i][0][0]),float(List[i][0][2]),float(List[i][1][0]),float(List[i][1][2])

        if mini>min(count1,count2):
            mini=min(count1,count2)
            rectangle=x1, y1, x2, y2
        #print (i,rectangle,count1,count2,mini)
        count1=0
        count2=0
        for j in range(len(point65)):
            x , y=float(point65[j][0]),float(point65[j][2])
            if FindPointrect(x1, y1, x2, y2, x, y) and float(point65[j][1])==2:
                count1+=1
            elif not FindPointrect(x1, y1, x2, y2, x, y) and float(point65[j][1])==1:
                count1+=1
        for j in range(len(point65)):
            x , y=float(point65[j][0]),float(point65[j][2])
            if FindPointrect(x1, y1, x2, y2, x, y) and float(point65[j][1])==1:
                count2+=1
            elif not FindPointrect(x1, y1, x2, y2, x, y) and float(point65[j][1])==2:
                count2+=1
    print ("min rectangle:",rectangle,mini)
    return rectangle,mini;

def adaboost(point65) :
    D0=[1/float(len(point65))]*len(point65)
    # for r in range(8) :
    #     for r in range(100) :
    # #         #print r

def main():
    f = open("HC_Body_Temperature", "r")
    List = []
    for i in f:
        List+=[i.split()]
    List_random=random.sample(List,130)
    traning=[]
    testing=[]
    for i in range(0,65):
        traning+=[List_random[i]]
    for i in range(65,130):
        testing+=[List_random[i]]
    #print(rectangle(traning))
    temp = rectangle(traning)
    print ( "testingggggggggg",temp[0],temp[1])
    print(circle(traning))
    adaboost(traning)
if __name__== "__main__":
  main()
 
