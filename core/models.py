from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Venta(models.Model):
   id = models.AutoField(primary_key=True)
   fecha = models.DateTimeField(default=datetime.now())
   cliente = models.ForeignKey(to=User, on_delete=models.CASCADE)
   total = models.IntegerField()

   def __str__(self):
      return str(self.id)+" "+self.cliente.username+" "+str(self.fecha)[0:20]

class Producto(models.Model):
 id_producto = models.CharField(primary_key=True, max_length=5)
 nombre_p = models.CharField(max_length=40) 
 precio = models.IntegerField()
 stock = models.IntegerField(null=True)
 imagen = models.CharField(max_length=200, null=True)
 info = models.CharField(max_length=400)

def __str__(self):
   return self.detalle+ " ("+self.codigo+")"

class Detalle(models.Model):
   id = models.AutoField(primary_key=True)
   venta = models.ForeignKey(to=Venta, on_delete=models.CASCADE)
   producto = models.ForeignKey(to=Producto, on_delete=models.CASCADE)
   cantidad = models.IntegerField()
   precio = models.IntegerField()

   def __str__(self):
      return str(self.id)+" "+self.producto.info[0:12]+" "+str(self.venta.id)