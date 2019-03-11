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

from Map import Map

class TheJourney:
        
    def __init__(self):
        self._map_=Map()
        
    def gameStart(self):
        self._map_.initialize_All()
        num_Of_Alive_Monsters = self._map_.Num_Of_Alive_Monsters
        num_Of_Alive_Warriors = self._map_.Num_Of_Alive_Warriors
        
        while (num_Of_Alive_Monsters>0 and num_Of_Alive_Warriors>0):
            self._map_.print_Board()
            self._map_.teleport_All()
            
            num_Of_Alive_Monsters = self._map_.Num_Of_Alive_Monsters
            num_Of_Alive_Warriors = self._map_.Num_Of_Alive_Warriors
        
        if num_Of_Alive_Monsters==0:
            print("Congratulations, all the monsters have been killed.")
        else:
            print("Unfortunately, the mission failed and all the warriors died.")
            
if __name__ == "__main__":
    journey = TheJourney()
    journey.gameStart()