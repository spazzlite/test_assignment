from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Creation time')
    modified = models.DateTimeField(auto_now=True, editable=False, verbose_name='Update time')

    class Meta:
        abstract = True


class Department(BaseModel):
    name = models.CharField(max_length=100, null=False)


class Employee(BaseModel):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    age = models.IntegerField()
    position = models.CharField(max_length=100)
    salary = models.IntegerField()
    photo = models.ImageField()
    department = models.ForeignKey(to=Department, related_name='employees', on_delete=models.CASCADE)
