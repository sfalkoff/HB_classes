"""This file should have our melon-type classes in it."""


class Watermelon(object):
    species = 'Watermelon'
    color = 'green'
    imported = False 
    shape = 'natural'
    seasons = ['Fall', 'Summer']
    base_price = 5.00

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        cost = self.base_price * qty
        if self.imported:
            cost = cost * 1.5 
        if self.shape != 'natural':
            cost = cost * 2
        if qty > 2:
            cost = cost * 0.75
        return cost
    
class Cantaloupe(object):
    species = 'Cantaloupe'
    color = 'tan'
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']
    base_price = 5.00

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        cost = self.base_price * qty
        if self.imported:
            cost = cost * 1.5 
        if self.shape != 'natural':
            cost = cost * 2
        if qty > 4:
            cost = cost * .5
        return cost


class Casaba(object):
    species = 'Casaba'
    color = 'green'
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    base_price = 6.00

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        cost = self.base_price * qty
        if self.imported:
            cost = cost * 1.5 
        if self.shape != 'natural':
            cost = cost * 2
        return cost

class Sharlyn(object):
    species = 'Sharlyn'
    color = 'tan'
    imported = True
    shape = 'natural'
    seasons = ['Summer']
    base_price = 5.00

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        cost = self.base_price * qty
        if self.imported:
            cost = cost * 1.5 
        if self.shape != 'natural':
            cost = cost * 2
        return cost

class SantaClaus(object):
    species = 'Santa Claus'
    color = 'green'
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']
    base_price = 5.00

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        cost = self.base_price * qty
        if self.imported:
            cost = cost * 1.5 
        if self.shape != 'natural':
            cost = cost * 2
        return cost

class Christmas(object):
    species = 'Christmas'
    color = 'green'
    imported = False
    shape = 'natural'
    seasons = ['Winter']
    base_price = 5.00

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        cost = self.base_price * qty
        if self.imported:
            cost = cost * 1.5 
        if self.shape != 'natural':
            cost = cost * 2
        return cost

class HornedMelon(object):
    species = 'Horned melon'
    color = 'yellow'
    imported = True
    shape = 'natural'
    seasons = ['Summer']
    base_price = 5.00

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        cost = self.base_price * qty
        if self.imported:
            cost = cost * 1.5 
        if self.shape != 'natural':
            cost = cost * 2
        return cost

class Xigua(object):
    species = 'Xigua'
    color = 'black'
    imported = True
    shape = 'square'
    seasons = ['Summer']
    base_price = 5.00

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        cost = self.base_price * qty
        if self.imported:
            cost = cost * 1.5 
        if self.shape != 'natural':
            cost = cost * 2
        return cost

class Ogen(object):
    species = 'Ogen'
    color = 'tan'
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']
    base_price = 6.00

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        cost = self.base_price * qty
        if self.imported:
            cost = cost * 1.5 
        if self.shape != 'natural':
            cost = cost * 2
        return cost