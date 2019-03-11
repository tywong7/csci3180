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

class NPC(object):
    
    def __init__(self,pos_x,pos_y,index,Map):
        self.Map=Map;
        self._pos=Pos(pos_x, pos_y)
        self._index=index
        self._name=None
        self._power=None
        
		
    def talk(self,content):
        print(self._name+ ": " + content)
	
    def action_On_Warrior(self,warrior):
        return False
    
    @property
    def Pos(self):
        return self._pos
    
    @Pos.setter
    def Pos(self, pos):
        self._pos = pos
        
    @property
    def Name(self):
        return self._name
    @Name.setter
    def Name(self, name):
        self._name=name
    
    @property
    def Power(self):
        return self._power
    @Power.setter
    def Power(self, power):
        self._power=power
    
    
    