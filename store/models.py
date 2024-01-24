from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class StoreUser(AbstractUser):
    OWNER = 1
    STOREKEEPER =2
    SALESMAN=3
    ACCOUNTANT=4

    Role_choices = ((OWNER,'OWNER'),
                    (STOREKEEPER,'STOREKEEPER'),
                    (SALESMAN,'SALESMAN'),
                    (ACCOUNTANT,'ACCOUNTANT'),
                    )

    role = models.PositiveSmallIntegerField(choices=Role_choices,default=3)

    class Meta:
        permissions = [('can_add_storeuser','can add srore user'),
                        ('can_update_storeuser','can update storeuser'),
                        ('can_delete_storeuser','can delete user recored'),
                        ('can_add_edit_delete_role','can add/edit/delete role'),]


