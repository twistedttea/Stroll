from django.db import models


class User(models.Model):

    name = models.CharField(max_length=50)
    location = ...

    def __str__(self):
        return self.name

    class Meta:
        abstract = true


class Walker(User):
    # This is going to be a subclass under user that defines data access, and what can be stored.
    # Will append on the CRUD methods l8r

    name = models.CharField(max_length=50)

    # return the to the struct
    # This acts as the "name" of the string, not what is stored
    def __str__(self):
        return self.name


class Doggy(User):
    # This is the dog class that defines just name at the moment.
    dog_name = models.CharField(max_length=50)

    # return the name to the struct
    def __str__(self):
        return self.dog_name
