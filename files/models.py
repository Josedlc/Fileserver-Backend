from django.db import models
from users.models import User

class Department(models.Model):
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name


class File(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    file_save = models.FileField(upload_to='files/')

