from django.db import models


class Profile(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(primary_key=True)
    phone_number = models.IntegerField(models.UniqueConstraint)

    def __str__(self):
        return f"This is {self.first_name} {self.last_name}"


class TodoList(models.Model):

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    deadline = models.DateField()
    email = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
