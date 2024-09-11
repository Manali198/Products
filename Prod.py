from django.db import models

class Prod{models.Model):
    name = models.Charfield(max_length=200)
    description = models.Textfields()
    price = models.DecimalField(max_dights=10,decimal_places=2)
    
    def __str__(self):
        return self.name
