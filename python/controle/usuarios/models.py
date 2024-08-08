from django.db import models
from django.contrib.auth.models import(
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None):
        usuario = self.model(
            email = self.normalize_email(email)
        )

        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        if password:
            usuario.set_password(password)

            usuario.save()
            return usuario
        
    def create_superuser(self, email, password):
        usuario =self.create_user(
            email = self.normalize_email(email),
            password = password,
        )
        
        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True

        usuario.set_password(password)

        usuario.save()
        return usuario    

class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name = "E-mail do usuário",
        max_length = 100,
        unique = True,
    )

    is_active = models.BooleanField(
    verbose_name = "Usuario está ativo",
    default = True,
    )

    is_staff = models.BooleanField(
        verbose_name = "Usuario é da equipe",
        default= False,
    )

    is_superuser = models.BooleanField(
        verbose_name = "Usuario administrador",
        default = False,
    )

    objects = UsuarioManager()
    
    USERNAME_FIELD = "email"

    class Meta:
        Verbose_name = "Usuário"
        Verbose_name_plural = "Usuários" 
        db_table = "usuario"

        def __str__(self):
            return self.email
        
