class User(models.Model):
    name = models.CharField(max_length=50)
    location = ...

    def __str__(self):
        return self.name

    class Meta:
        abstract = true


class Walker(User):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
