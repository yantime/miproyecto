from django.db import models

# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    contenido = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.titulo