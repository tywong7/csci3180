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


class Land(object):
    
    def __init__(self):
        self._occupied_obj= None
    
    def coming(self,warrior):
        try:

            return self._occupied_obj.action_On_Warrior(warrior)
        except:

            return True
        
        return True
    @property   
    def Occupied_obj(self):
        return self._occupied_obj
    
    @Occupied_obj.setter
    def Occupied_obj(self,occupied_obj):
        self._occupied_obj=occupied_obj
        
    @property
    def Occupant_Name(self):
        try:
            return self._occupied_obj.Name
        except:
            return None
        return None
    
