from django.db import models

# Create your models here.


class Producto(models.Model):
	titulo = models.CharField(max_length=30)
	descripcion = models.TextField(blank=True, null=True)
	precio = models.DecimalField(max_digits=30, decimal_places=2, default=9.99)
	precio_rebajas = models.DecimalField(max_digits=100,
		decimal_places=2, default=6.99, null=True, blank=True)


	def __unicode__(self):
		return self.titulo