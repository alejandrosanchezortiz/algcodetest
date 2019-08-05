from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)
    connects = models.ManyToManyField('self',blank=True)

    def __str__(self):
        return self.name
	