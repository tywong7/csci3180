# CSCI3180 Principles of Programming Languages
#
# --- _Declaration ---
#
# I declare that the assignment here submitted is original except for source
# material explicitly acknowledged. I also acknowledge that I am aware of
# University policy and regulations on honesty in academic work, and of the
# disciplinary guidelines and procedures applicable to breaches of such policy
# and regulations, as contained in the website
# http://www.cuhk.edu.hk/policy/academichonesty/
#
# Assignment 2
# Name : Wong Tsz Yin
# Student I_D : 1155093245
# Email Addr : 1155093245@link.cuhk.edu.hk

from Land import Land
from Monster import Monster
from Elf import Elf
from Warrior import Warrior
from Pos import Pos

import random
class Map(object):
    _D = 10
    
    
    def __init__(self):
        self._teleportable_obj=[]
        self._lands= [[Land() for j in range(self._D)] for i in range(self._D)]
        self._e=random.randint(0,1)+2
        self._m=random.randint(0,1)+2
        self._w=1
        self._total_Num=self._m+self._e+self._w
        self._num_Of_Alive_Monsters=self._m
        self._num_Of_Alive_Warriors=self._w
    
    def initialize_All(self):
        print("Welcome to Kafustrok. Light blesses you. ")
        for i in range (self._D):
            for j in range (self._D):
                self._lands[i][j]=Land()
        for i in range (self._total_Num):
            pos=self.get_Un_Occupied_Position()
            if i<self._m:
                self._lands[pos.X][pos.Y].Occupied_obj=Monster(pos.X,pos.Y,i,self)
            elif i<self._m+self._e:
                self._lands[pos.X][pos.Y].Occupied_obj=Elf(pos.X,pos.Y,i-self._m,self)
            else:   
                self._lands[pos.X][pos.Y].Occupied_obj=Warrior(pos.X,pos.Y,i-self._m-self._e,self)
                self._teleportable_obj.append(self._lands[pos.X][pos.Y].Occupied_obj)
                
    def teleport_All(self):
        for obj in self._teleportable_obj:
            obj.teleport()

    def coming(self,pos_x,pos_y,warrior):
        return self._lands[pos_x][pos_y].coming(warrior)
    
    def set_Land(self,_pos, occupied_obj):
        self._lands[_pos.X][_pos.Y].Occupied_obj=occupied_obj
                    
    def delete_Teleportable_Obj(self,obj):
        self._teleportable_obj.remove(obj)
    
    def get_Un_Occupied_Position(self):
        randx=random.randint(0,self._D-1)
        randy=random.randint(0,self._D-1)
        while (self._lands[randx][randy].Occupied_obj !=None):
            randx=random.randint(0,self._D-1)
            randy=random.randint(0,self._D-1)
        return Pos(randx,randy)
    
    def print_Board(self):
        print_Object=[]
        for i in range(self._D):
            print_Object.append([' '] * self._D)
    
        for i in range(self._D):
            for j in range(self._D):
                occupant_Name=self._lands[i][j].Occupant_Name
                if (occupant_Name==None):
                    occupant_Name="  "
                print_Object[i][j]=occupant_Name
        
        print("  ", end='')
        for i in range (self._D):
            print("| %d  "%i, end='')
        print("|")
        
        for i in range (int(self._D*5.5)):
            print("-",end='')
        print("")
        
        for row in range (self._D):
            print(row,end=' ')
            for col in range (self._D):
                print("| %s "%print_Object[row][col],end='')
            print("|")
            
            for i in range (int(self._D*5.5)):
                print("-",end='')
            print("")
            
    def decrease_Num_Of_Alive_Monsters(self):
        self._num_Of_Alive_Monsters-=1
    def decrease_Num_Of_Warriors(self):
        self._num_Of_Alive_Warriors-=1
    
    @property
    def Num_Of_Alive_Monsters(self):
        return self._num_Of_Alive_Monsters
    
    @Num_Of_Alive_Monsters.setter
    def Num_Of_Alive_Monsters(self,num_Of_Alive_Monsters):
        self._num_Of_Alive_Monsters=num_Of_Alive_Monsters
        
    @property
    def Num_Of_Alive_Warriors(self):
        return self._num_Of_Alive_Warriors
    
    @Num_Of_Alive_Warriors.setter
    def Num_Of_Alive_Warriors(self,num_Of_Alive_Warriors):
        self._num_Of_Alive_Warriors=num_Of_Alive_Warriors
        
                
            
                
                
                
                