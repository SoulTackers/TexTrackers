# from django.db import models
# from django.contrib.auth.models import AbstractUser
#
# class Role(models.Model):
#   '''
#   The Role entries are managed by the system,
#   automatically created via a Django data migration.
#   '''
#   Admin = 1
#   Employee = 2
#   Client = 3
#
#   ROLE_CHOICES = (
#       (Admin, 'Admin'),
#       (Employee, 'Employee'),
#       (Client, 'Client'),
#   )
#
#   id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)
#
#   def __str__(self):
#       return self.get_id_display()
#
#
# class CustomUser(AbstractUser):
#   roles = models.ManyToManyField(Role)
