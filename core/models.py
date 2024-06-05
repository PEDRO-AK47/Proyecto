from django.db import models

class Producto(models.Model):
 id_producto = models.AutoField(primary_key=True)
 nombre_p = models.CharField(max_length=40)
 precio = models.IntegerField()
 info = models.CharField(max_length=400)

def __str__(self):
    return self.nombre_p + ""+int(self.precio)


