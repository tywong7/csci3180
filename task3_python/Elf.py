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
import random
from NPC import NPC

class Elf(NPC):
    
    _MAGIC_CAP = 20
    def __init__(self,pos_x,pos_y,index,Map):       
        super().__init__(pos_x,pos_y,index,Map)
        self.Name="E" +str(index)
        self.Power=random.randint(0,Elf._MAGIC_CAP-6)+5
        
    def action_On_Warrior(self,warrior):
        super().talk("My name is %s.  Welcome to my home. My magic power is %d."%(self.Name,self.Power))
        super().talk("Your magic crystal is %d."%warrior.Magic_crystal)
        super().talk("Do you need my help?")
        super().talk("You now have following options: ")
        print("1. Yes")
        print("2. No",end=' ')
        a=input()
        if a=='1':
            value=(random.randint(0,self.Power-3)+2)
            if (warrior.Magic_crystal>value):
                warrior.decrease_Crystal(value)
                warrior.increase_Health(value)
                warrior.talk("Thanks for your help! %s."%self.Name)
            else:
                warrior.talk("Very embarrassing, I don't have enough crystals.")
        return False