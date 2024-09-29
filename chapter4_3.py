from treelib import Tree,Node
import numpy as np
import math
from collections import Counter

#the colour of watermelon , 1 for green , 2 for black, 3 for white
Data_Colour = [1,2,2,1,3,1,2,2,2,1,3,3,1,3,2,3,1]
#the root of watermelon, 1 for curled up, 2 for little curled up, 3 for hard
Data_Root = [1,1,1,1,1,2,2,2,2,3,3,1,2,2,2,1,1]
#the sound of watermelon,1 for voiced, 2 for dull, 3 for crisp
Data_Sound = [1,2,1,2,1,1,1,1,2,3,3,1,1,2,1,1,2]
#the texture of watermelon,1 for clear, 2 for little clear, 3 for blur 
Data_Texture = [1,1,1,1,1,1,2,1,2,1,3,3,2,2,1,3,2]

Data_Umbilicus = [1,1,1,1,1,2,2,2,2,3,3,3,1,1,2,3,2]

Data_Touch = [1,1,1,1,1,2,2,1,1,2,1,2,1,1,2,1,1]

Data_Density = [0.697,0.774,0.634,0.608,0.556,0.403,0.481,0.437,0.666,0.243,0.245,0.343,0.639,0.657,0.360,0.593,0.719]

Data_Sugar = [0.460,0.376,0.264,0.318,0.215,0.237,0.149,0.211,0.091,0.267,0.057,0.099,0.161,0.198,0.370,0.042,0.103]

Data_GoodOrBad = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0]

class Watermelon :
    def __init__(self) -> None:
        self.Colour = None
        self.Root = None
        self.Sound = None
        self.Texture = None
        self.Umbilicus = None
        self.Touch = None
        self.Density = None
        self.Sugar = None
        self.GorB = None
        self.Num = None
    
    def Set_Data_Colour(self,a):
        self.Colour = a
    def Set_Data_Root(self,a):
        self.Root = a
    def Set_Data_Sound(self,a):
        self.Sound = a 
    def Set_Data_Texture(self,a):
        self.Texture = a
    def Set_Data_Umbilicus(self,a):
        self.Umbilicus = a
    def Set_Data_Touch(self,a):
        self.Touch = a
    def Set_Data_Density(self,a):
        self.Density = a
    









p1 = Counter(Data_GoodOrBad)[1]/17
p2 = Counter(Data_GoodOrBad)[0]/17
Ent_D = -(p1*math.log2(p1)+p2*math.log2(p2))
#print(Ent_D)
Gain_1 = []
def Cal_Gain(a):
    if a[0] != 1.0 and a[0] != 0.0:
        a_t = []
        b = a 
        a = sorted(a)
        print(a)
        print(b)
        Gain_t = []
        for i in range(len(a)-1):
            a_t.append((a[i] + a[i+1])/2)
        print(a_t)
        for i in range(len(a_t)):
            p1 = 0
            p2 = 0
            p1_p = 0
            p1_n = 0
            p2_p = 0
            p2_n = 0
            Ent_Dr1 = 0
            Ent_Dr2 = 0
            for j in range(len(b)):
                if b[j] > a_t[i] :
                    p1 = p1 + 1
                    if Data_GoodOrBad[j] == 1:
                        p1_p = p1_p + 1
                    else:
                        p1_n = p1_n + 1
                        
                else :
                    p2 = p2 + 1
                    if Data_GoodOrBad[j] == 1:
                        p2_p = p2_p + 1
                    else:
                        p2_n = p2_n + 1
            print(p1_p,p1_n,p2_p,p2_n)           
            p1_p = p1_p/p1
            p1_n = p1_n/p1
            p2_p = p2_p/p2
            p2_n = p2_n/p2
            p1 = p1/len(a)
            p2 = p2/len(a)
            
            print(p1_p,p1_n,p2_p,p2_n)
            
            if p1_p != 0 and p1_n != 0:
                Ent_Dr1 = -(p1_p*math.log2(p1_p) + p1_n*math.log2(p1_n))
            print(Ent_Dr1)
            if p2_p != 0 and p2_n != 0:
                Ent_Dr2 = -(p2_p*math.log2(p2_p) + p2_n*math.log2(p2_n))
            print(Ent_Dr2)
            Gain_t.append(Ent_D - p1*Ent_Dr1 - p2*Ent_Dr2)
        print(Gain_t)
        Gain = max(Gain_t)
            
            
        
    else: 
        p1 = Counter(a)[1]/17
        p2 = Counter(a)[2]/17
        p3 = Counter(a)[3]/17
        a_1 = []
        a_2 = []
        a_3 = []
        Ent_D3 = 0
        for i in range(len(a)):
            if a[i] == 1:
                a_1.append(i)
            elif a[i] == 2:
                a_2.append(i)
            elif a[i] == 3:
                a_3.append(i)

        p1_p = 0
        p1_n = 0
        for i in range(len(a_1)):
            if Data_GoodOrBad[a_1[i]] == 1:
                p1_p = p1_p + 1
            else :
                p1_n = p1_n + 1
        p1_p = p1_p/len(a_1)
        p1_n = p1_n/len(a_1)
        if p1_p == 0 or p1_n == 0:
            Ent_D1 = 0
        else:
            Ent_D1 = -(p1_p*math.log2(p1_p) + p1_n*math.log2(p1_n))
#   print(Ent_D1)
        p2_p = 0
        p2_n = 0
        for i in range(len(a_2)):
            if Data_GoodOrBad[a_2[i]] == 1:
                p2_p = p2_p + 1
            else :
                p2_n = p2_n + 1    
        p2_p = p2_p/len(a_2)
        p2_n = p2_n/len(a_2)
        if p2_p == 0 or p2_n == 0:
            Ent_D2 = 0
        else:
            Ent_D2 = -(p2_p*math.log2(p2_p)+p2_n*math.log2(p2_n))
#    print(Ent_D2)
        if len(a_3) != 0:
            p3_p = 0
            p3_n = 0
            for i in range(len(a_3)):
                if Data_GoodOrBad[a_3[i]] == 1:
                    p3_p = p3_p + 1
                else :
                    p3_n = p3_n + 1    
            p3_p = p3_p/len(a_3)
            p3_n = p3_n/len(a_3)
            if p3_p == 0 or p3_n == 0:
                Ent_D3 = 0
            else:
                Ent_D3 = -(p3_p*math.log2(p3_p)+p3_n*math.log2(p3_n))
#    print(Ent_D3)
        Gain = Ent_D - p1*Ent_D1 - p2* Ent_D2 - p3*Ent_D3         
    print(Gain)
    return Gain
Data = [Data_Colour,Data_Root,Data_Sound,Data_Texture,Data_Umbilicus,Data_Touch,Data_Density]
G = []


tree = Tree()
Data_Num = range(17)
while len(Data_Num) != 0:
    for  i in range(len(Data)):
        G.append (Cal_Gain(Data[i]))
    j = sum(G)
    tree.create_node("node[i]","ss")
    
    

