"""This file should have our melon-type classes in it."""

class Melon(object):
    def get_base_price(self):
        return 6.00


class Watermelon(Melon):
    species = 'Watermelon'
    color = 'green'
    imported = False 
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        cost = self.get_base_price() * qty
        if self.imported:
            cost = cost * 1.5 
        if self.shape == 'square':
            cost = cost * 2
        if qty > 2:
            cost = cost * 0.75
        return cost
    
class Cantaloupe(Melon):
    species = 'Cantaloupe'
    color = 'tan'
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        cost = self.get_base_price() * qty
        if self.imported:
            cost = cost * 1.5 
        if self.shape == 'square':
            cost = cost * 2
        if qty > 4:
            cost = cost * .5
        return cost


class Casaba(Melon):
    species = 'Casaba'
    color = 'green'
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        cost = (self.get_base_price() + 1) * qty
        if self.imported:
            cost = cost * 1.5 
        if self.shape == 'square':
            cost = cost * 2
        return cost

class Sharlyn(Melon):
    species = 'Sharlyn'
    color = 'tan'
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        cost = self.get_base_price() * qty
        if self.imported:
            cost = cost * 1.5 
        if self.shape == 'square':
            cost = cost * 2
        return cost

class SantaClaus(Melon):
    species = 'Santa Claus'
    color = 'green'
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        cost = self.get_base_price() * qty
        if self.imported:
            cost = cost * 1.5 
        if self.shape == 'square':
            cost = cost * 2
        return cost

class Christmas(Melon):
    species = 'Christmas'
    color = 'green'
    imported = False
    shape = 'natural'
    seasons = ['Winter']

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        cost = self.get_base_price() * qty
        if self.imported:
            cost = cost * 1.5 
        if self.shape == 'square':
            cost = cost * 2
        return cost

class HornedMelon(Melon):
    species = 'Horned Melon'
    color = 'yellow'
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        cost = self.get_base_price() * qty
        if self.imported:
            cost = cost * 1.5 
        if self.shape == 'square':
            cost = cost * 2
        return cost

class Xigua(Melon):
    species = 'Xigua'
    color = 'black'
    imported = True
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        cost = self.get_base_price() * qty
        if self.imported:
            cost = cost * 1.5 
        if self.shape == 'square':
            cost = cost * 2
        return cost

class Ogen(Melon):
    species = 'Ogen'
    color = 'tan'
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        cost = (self.get_base_price() + 1) * qty
        if self.imported:
            cost = cost * 1.5 
        if self.shape == 'square':
            cost = cost * 2
        return cost