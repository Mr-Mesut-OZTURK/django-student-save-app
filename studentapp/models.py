from django.db import models

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField(unique=True)
    email = models.EmailField(max_length=254, unique=True)
    image = models.ImageField(upload_to='students/%Y/%m', default="avatar.png")
    GENDER = (
        ("1", "Female"),
        ("2", "Male"),
    )
    gender = models.CharField(max_length=50, choices=GENDER)


    def __str__(self):
        return str(self.number) + ' ' + self.first_name + " " + self.last_name

    class Meta:
        ordering = ('number',)