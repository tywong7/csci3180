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
class Potion(object):
    _HEAL_CAP = 40
    def __init__(self,pos_x,pos_y,index,Map):
        self._map_=Map
        self._pos=Pos(pos_x,pos_y)
        self._index=index;
        self._name="P"+str(index)
        self._heal=random.randint(1,self._HEAL_CAP)
    
    def action_On_Warrior(self,warrior):
        final_Heal=warrior.Health+self.Heal;
        
        if (final_Heal>self._HEAL_CAP):
            final_Heal=self._HEAL_CAP
        
        warrior.increase_Health(final_Heal)
        warrior.talk("Very good, I got additional healing potion "+self.Name+".")
        self._map_.decrease_Num_Of_Potions()
        self._map_.delete_Teleportable_Obj(self)
        return True
    
    def teleport(self):
        self._map_.set_Land(self._pos,None)        
        self.set_Pos=self._map_.get_Un_Occupied_Position()
        self._map_.set_Land(self._pos,self)
    
    
    @property
    def Heal(self):
        return self._heal
    
    @property
    def Name(self):
        return self._name
    
    @property
    def Pos(self):
        return self._pos
    
    @Pos.setter
    def set_Pos(self,pos):
        self._pos=pos
    
    
        
        
        