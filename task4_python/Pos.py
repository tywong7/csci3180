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

class Pos():
    
    def __init__(self,x,y):
        self._x=x
        self._y=y
    
    @property
    def X(self):
        return self._x
    @property
    def Y(self):
        return self._y
    
    def set_Pos(self,x,y):
        self._x = x
        self._y = y 