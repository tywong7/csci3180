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

from NPC import NPC
import random
class Monster(NPC):
    
    _DAMAGE_CAP = 20
    def __init__(self,pos_x,pos_y,index,Map):       
        super().__init__(pos_x,pos_y,index,Map)
        self.Name='M'+str(index)
        self.Power=random.randint(0,Monster._DAMAGE_CAP-6)+5

    
    def action_On_Warrior(self,warrior):
        super().talk("I am the monster %s.  Here is my territory. My damage power is %d."%(self.Name,self.Power))
        super().talk("Your health is is %d."%warrior.Health)
        super().talk("Do you really want to challenge me?")
        super().talk("You now have following options: ")
        print("1. Yes")
        print("2. No")
        a=input()
        if a=='1':
            if (warrior.Health>self.Power):
                warrior.decrease_Health(self.Power)
                warrior.increase_Crystal(random.randint(0,4)+5)
                warrior.talk("Nice, I have killed the monster %s."%self.Name)
                self.Map.decrease_Num_Of_Alive_Monsters()
                return True
            warrior.decrease_Health(self.Power);
        return False
    