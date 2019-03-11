# CSCI3180 Principles of Programming Languages
#
# --- Declaration ---
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
# Student ID : 1155093245
# Email Addr : 1155093245@link.cuhk.edu.hk

from Pos import Pos
import random

class Warrior(object):
    _HEALTH_CAP = 40;
    def __init__(self,pos_x,pos_y,index,Map):       
        self._pos= Pos(pos_x,pos_y)
        self._index=index
        self._map_=Map
        self._name="W"+str(index)
        self._health=Warrior._HEALTH_CAP
        self._magic_crystal=10

    def action_On_Warrior(self,warrior):
        self.talk("Hi bro. You can call me "+self._name+". I am very happy to meet you. I have "+str(self._magic_crystal)+" magic crystals.")
        if (self._magic_crystal<=1):
                self.talk("Sorry bro, I am f-up too.")
                return False
        self.talk("The number of your magic crystals is "+str(warrior.Magic_crystal)+".");
        self.talk("Need I share with you some crystal?");
        self.talk("You now have following options:");
        print("1. Yes")
        print("2. No")
        a=input()
        if a=='1':
            value=self.Magic_crystal;
            value=random.randint(0,value)
            warrior.increase_Crystal(value)
            self.decrease_Crystal(value)
            warrior.talk("Thanks for your shared "+str(value)+" magic crystals! "+self.Name+".");
            
        return False;
    
    def teleport(self):
        print("Hi, %s. Your position is (%d,%d) and health is %d."%(self._name,self._pos.X, self._pos.Y, self._health))
        print("Specify your target position (Input 'x y').")
        pos_x, pos_y=input().split(' ')
        pos_x=int(pos_x)
        pos_y=int(pos_y)
        while((pos_x == self._pos.X) and (pos_y == self._pos.Y)):
            print("Specify your target position (Input 'x y'). It should not be the same as the original one.")
            pos_x, pos_y=input().split(' ') 
            pos_x=int(pos_x)
            pos_y=int(pos_y)
        result=self._map_.coming(pos_x,pos_y,self)
        
        if result:
            self._map_.set_Land(self._pos,None)
            self._pos.set_Pos(pos_x,pos_y)
            self._map_.set_Land(self._pos,self)
        
        if self._health<=0:
            print("Very sorry, %s has been killed."%self._name)
            self._map_.set_Land(self._pos,None)
            self._map_.delete_Teleportable_Obj(self)
            self._map_.decrease_Num_Of_Warriors()
        
    def talk(self,content):
        print(self._name+ ": " + content)
    
    def increase_Crystal(self,value):
        self._magic_crystal+=value
    
    def decrease_Crystal(self,value):
        self._magic_crystal-=value
    
    def increase_Health(self,value):
        self._health+=value
        if (self._health>Warrior._HEALTH_CAP):
            self._health=Warrior._HEALTH_CAP
    def decrease_Health(self,value):
        self._health-=value   
    
    @property
    def Pos(self):
        return self._pos
    
    @property
    def Name(self):
        return self._name
    
    @property
    def Health(self):
        return self._health
    
    @Health.setter
    def Health(self,health):
        self._health=health
    
    @property
    def Magic_crystal(self):
        return self._magic_crystal
    
    @Magic_crystal.setter
    def Magic_crystal(self,magic_crystal):
        self._magic_crystal=magic_crystal
            