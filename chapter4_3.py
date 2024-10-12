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

Texture_Name = ['Colour','Root','Sound','Texture','Umbilicus','Touch','Density','Sugar']
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
        self.TextureList = [self.Colour,self.Root,self.Sound,self.Texture,self.Umbilicus,self.Touch,self.Density,self.Sugar]
        self.DataType = [None]*10
    def Set_Data_Colour(self,a):
        self.Colour = a
        if isinstance(a,int):
            self.DataType[0] = 'discrete' 
        else:
            self.DataType[0] = 'continued'
    def Set_Data_Root(self,a):
        self.Root = a
        if isinstance(a,int):
            self.DataType[1] = 'discrete' 
        else:
            self.DataType[1] = 'continued'
    def Set_Data_Sound(self,a):
        self.Sound = a 
        if isinstance(a,int):
            self.DataType[2] = 'discrete' 
        else:
            self.DataType[2] = 'continued'
    def Set_Data_Texture(self,a):
        self.Texture = a
        if isinstance(a,int):
            self.DataType[3] = 'discrete' 
        else:
            self.DataType[3] = 'continued'
    def Set_Data_Umbilicus(self,a):
        self.Umbilicus = a
        if isinstance(a,int):
            self.DataType[4] = 'discrete' 
        else:
            self.DataType[4] = 'continued'
    def Set_Data_Touch(self,a):
        self.Touch = a
        if isinstance(a,int):
            self.DataType[5] = 'discrete' 
        else:
            self.DataType[5] = 'continued'
    def Set_Data_Density(self,a):
        self.Density = a
        if isinstance(a,int):
            self.DataType[6] = 'discrete' 
        else:
            self.DataType[6] = 'continued'
    def Set_Data_Sugar(self,a):
        self.Sugar = a
        if isinstance(a,int):
            self.DataType[7] = 'discrete' 
        else:
            self.DataType[7] = 'continued'
    def Set_Data_GorB(self,a):
        self.GorB = a
    def Set_Data_Num(self,a):
        self.Num = a

Data = []
Data_Num = 17
for i in range(Data_Num):
    Data.append(Watermelon())
    Data[i].Set_Data_Colour(Data_Colour[i])
    Data[i].Set_Data_Root(Data_Root[i])
    Data[i].Set_Data_Sound(Data_Sound[i])
    Data[i].Set_Data_Texture(Data_Texture[i])
    Data[i].Set_Data_Umbilicus(Data_Umbilicus[i])
    Data[i].Set_Data_Touch(Data_Touch[i])
    Data[i].Set_Data_Density(Data_Density[i])
    Data[i].Set_Data_Sugar(Data_Sugar[i])
    Data[i].Set_Data_GorB(Data_GoodOrBad[i])
    Data[i].Set_Data_Num(i)

tree = Tree()

def Cal_Gain_Depth(Data,BestAttribute,DataNum,TextureNum,TextureName,parentid):
    temp = []
    for i in range(len(Data)):
        temp.append(Data[i].GorB)
    Ent_D = -(Counter(temp)[1]/len(temp)*math.log2(Counter(temp)[1]/len(temp)) + Counter(temp)[0]/len(temp)*math.log2(Counter(temp)[0]/len(temp)))
    if Ent_D == 0 and BestAttribute == None:
        print('Wrong Data Set!!')
        return
    elif Ent_D == 0 and BestAttribute != None:
        if temp[0] == 1:    
            tree.create_node(tag='good',parent=parentid,data=BestAttribute)
        else:
            tree.create_node(tag='bad',parent=parentid,data=BestAttribute)
        return
    elif Ent_D > 0:
        Gain = Cal_Gain(Data,Ent_D,TextureNum,DataNum)
        Max_Gain_Num = Gain.index(max(Gain))
        tree.create_node(tag=TextureName[Max_Gain_Num],id=TextureName[Max_Gain_Num],data = TextureName[Max_Gain_Num])
        treeid = TextureName[Max_Gain_Num]        
        for i in range(Data_Num):
            temp[i] = Data[i].TextureList[Max_Gain_Num]
        set1 = set(temp)
        set2 = []
        for every in set1:
            set2.append(every)
        for i in range(len(set2)):
            Data_temp  = []
            for j in range(len(temp)):
                if temp[j] == set2[i]:
                    Data_temp.append(Data[j])
            Cal_Gain_Depth(Data_temp,TextureName[Max_Gain_Num],len(Data_temp),TextureNum,TextureName,treeid)
            
def Cal_Gain(Data,Ent_D,TextureNum,DataNum):
    temp = []
    Gain_t = []
    for i in range(TextureNum):
        Data_Type1 = ''
        Data_Type1  = Data[0].DataType[i]
        for j in range(DataNum):
            temp.append(Data[j].TextureList[i])           
        if Data_Type1 == 'continued':
            temp_t = []
            temp_s = []
            temp_s = temp 
            temp_s = sorted(temp_s)
            for j in range(len(temp_s)-1):
                temp_t.append((temp_s[j] + temp_s[j+1])/2)
            for j in range(len(temp_t)):
                p1 = 0
                p2 = 0
                p1_p = 0
                p1_n = 0
                p2_p = 0
                p2_n = 0
                Ent_Dr1 = 0
                Ent_Dr2 = 0
                for k in range(len(temp)):
                    if temp[k] > temp_t[j] :
                        p1 = p1 + 1
                        if Data[k].GorB == 1:
                            p1_p = p1_p + 1
                        else:
                            p1_n = p1_n + 1
                            
                    else :
                        p2 = p2 + 1
                        if Data[k].GorB == 1:
                            p2_p = p2_p + 1
                        else:
                            p2_n = p2_n + 1          
                p1_p = p1_p/p1
                p1_n = p1_n/p1
                p2_p = p2_p/p2
                p2_n = p2_n/p2
                p1 = p1/len(temp)
                p2 = p2/len(temp)                
                if p1_p != 0 and p1_n != 0:
                    Ent_Dr1 = -(p1_p*math.log2(p1_p) + p1_n*math.log2(p1_n))
                if p2_p != 0 and p2_n != 0:
                    Ent_Dr2 = -(p2_p*math.log2(p2_p) + p2_n*math.log2(p2_n))
                Gain_t.append(Ent_D - p1*Ent_Dr1 - p2*Ent_Dr2)
            print(Gain_t)
        else:
            set1 = set(temp)
            set2 = []
            for every in set1:
                set2.append(every)
            p = []
            Num_t = []
            for i in range(len(set1)):
                Num_t.append(Counter(temp)[set2[i]])
                p.append(Counter(temp)[set2[i]]/DataNum)
            Ent_D_t = []
            for i in range(len(set1)):
                num_p = 0
                num_n = 0
                p1 = 0
                p2 = 0
                for j in range(Data_Num):
                    if temp[j] == set2[i] and Data[j].GorB == 1:
                        num_p = num_p + 1
                    elif temp[j] == set2[i] and Data[j].GorB == 0:
                        num_n = num_n + 1
                p1 = num_p / Num_t[i]
                p2 = num_n / Num_t[i]
                if p1!= 0 and p2!=0:
                    Ent_D_t.append(-(p1*math.log2(p1)+p2*math.log2(p2)))
                else:
                    Ent_D_t.append(0)
            Gain_temp = Ent_D            
            for i in range(len(set1)):
                Gain_temp = Gain_temp -p[i]*Ent_D_t[i]        
            Gain_t.append(Gain_temp)
        return Gain_t

print(Data[0].DataType[2])
Cal_Gain_Depth(Data,None,Data_Num,len(Data[0].TextureList),Texture_Name)



    

