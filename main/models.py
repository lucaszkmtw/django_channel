from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin       
from django.contrib.auth.models import Permission,Group
from django.contrib.contenttypes.models import ContentType     
from django.contrib.auth.models import AbstractUser

class Rol(models.Model):
    """Model definition for Rol."""

    # TODO: Define fields here
    id = models.AutoField(primary_key = True)
    rol = models.CharField('Rol', max_length=50,unique = True)

    class Meta:
        """Meta definition for Rol."""

        verbose_name = 'Rol'
        verbose_name_plural = 'Rols'

    def __str__(self):
        """Unicode representation of Rol."""
        return self.rol
    
    def save(self,*args,**kwargs):
        permisos_defecto = ['add','change','delete','view']
        if not self.id:
            nuevo_grupo,creado = Group.objects.get_or_create(name = f'{self.rol}')
            for permiso_temp in permisos_defecto:
                permiso,created = Permission.objects.update_or_create(
                    name = f'Can {permiso_temp} {self.rol}',
                    content_type = ContentType.objects.get_for_model(Rol),
                    codename = f'{permiso_temp}_{self.rol}'
                )
                if creado:
                    nuevo_grupo.permissions.add(permiso.id)
            super().save(*args,**kwargs)
        else:
            rol_antiguo = Rol.objects.filter(id = self.id).values('rol').first()
            if rol_antiguo['rol'] == self.rol:
                super().save(*args,**kwargs)
            else:
                Group.objects.filter(name = rol_antiguo['rol']).update(name = f'{self.rol}')
                for permiso_temp in permisos_defecto:
                    Permission.objects.filter(codename = f"{permiso_temp}_{rol_antiguo['rol']}").update(
                        codename = f'{permiso_temp}_{self.rol}',
                        name = f'Can {permiso_temp} {self.rol}'
                    )
                super().save(*args,**kwargs)
        

class UserProfile(AbstractUser):
    pass