"""This file should have our melon-type classes in it."""

class Melon(object):
    def get_base_price(self):
        return 5.00

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        if self.species == 'Casaba' or self.species == 'Ogen':
            cost = (self.get_base_price() + 1) * qty
        else:
            cost = self.get_base_price() * qty
        if self.imported:
            cost = cost * 1.5 
        if self.shape == 'square':
            cost = cost * 2
        if self.species  == 'Watermelon' and qty > 2:
            cost = cost * 0.75
        if self.species == 'Cantaloupe' and qty > 4:
            cost = cost * 0.5
        return cost

class Watermelon(Melon):
    species = 'Watermelon'
    color = 'green'
    imported = False 
    shape = 'natural'
    seasons = ['Fall', 'Summer']
    
class Cantaloupe(Melon):
    species = 'Cantaloupe'
    color = 'tan'
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

class Casaba(Melon):
    species = 'Casaba'
    color = 'green'
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']

class Sharlyn(Melon):
    species = 'Sharlyn'
    color = 'tan'
    imported = True
    shape = 'natural'
    seasons = ['Summer']

class SantaClaus(Melon):
    species = 'Santa Claus'
    color = 'green'
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

class Christmas(Melon):
    species = 'Christmas'
    color = 'green'
    imported = False
    shape = 'natural'
    seasons = ['Winter']

class HornedMelon(Melon):
    species = 'Horned Melon'
    color = 'yellow'
    imported = True
    shape = 'natural'
    seasons = ['Summer']

class Xigua(Melon):
    species = 'Xigua'
    color = 'black'
    imported = True
    shape = 'square'
    seasons = ['Summer']

class Ogen(Melon):
    species = 'Ogen'
    color = 'tan'
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']