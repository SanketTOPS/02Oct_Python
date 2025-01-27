from django.db import models

# Create your models here.


class product(models.Model):  # Parent Table
    pname = models.CharField(max_length=100)

    def __str__(self):
        return self.pname


class subcategory(models.Model):  # Child Table
    pname = models.ForeignKey(product, on_delete=models.CASCADE)
    modelname = models.CharField(max_length=50)
    price = models.IntegerField()
