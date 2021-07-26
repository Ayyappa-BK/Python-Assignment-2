# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 18:11:27 2021

@author: Gagan Ayyappa
"""

class Dog:
    species = 'Canis familiaris'
    def __init__(self,name,age):
        self.name = name
        self.age = age
buddy = Dog('Buddy',9)
miles = Dog('Miles', 4)


class Dog:
    species = 'Canis familiaris'
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self,sound):
        return f"{self.name} says {sound}"
 
    
class Dog:
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
class Dog:
    species = 'Canis familiaris'
    
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed 
        
class Dog:
    species = 'Canis familiaris'
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self,sound):
        return f"{self.name} says {sound}"
    
class JackRussell(Dog):
    pass
class Dachshund(Dog):
    pass
class Bulldog(Dog):
    pass


class JackRussell(Dog):
    def speak(self,sound='Arf'):
        return f"{self.name] says {sound}"
    
class JackRussell(Dog):
    def speak(self,sound='Arf'):
        return super().speak(sound)
