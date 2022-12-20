from django.db import models

# Create your models here.

opc_consulta = [
    [0, 'Consulta'],
    [1, 'Sugerencia'],
    [2, 'Otros']
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opc_consulta)
    mensaje = models.TextField()

    def __str__(self):
        return f'{self.nombre } | {self.mensaje}'