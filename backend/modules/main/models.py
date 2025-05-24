from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, login, email, password, **extra_fields):
        if not login:
            raise ValueError('Логин должен быть указан')
        if not email:
            raise ValueError('Email должен быть указан')
        if not password:
            raise ValueError('Password должен быть указан')

        user = self.model(
            login=login,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(login, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    date_register = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    GENDER_CHOICES = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
    )
    
    personal_gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
        null=True
    )

    personal_photo = models.ImageField(
        upload_to='user_photos/%Y/%m/%d/',
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['email', 'name', 'last_name']

    def get_full_name(self):
        return f"{self.name} {self.last_name}"

    def get_short_name(self):
        return self.login

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    class Meta:
        db_table = 'p_user'

class Option(models.Model):
    module = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    value = models.TextField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_option'


class UserField(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    title = models.CharField(db_column='TITLE', max_length=255)
    entity_id = models.CharField(db_column='ENTITY_ID', max_length=70)
    field_name = models.CharField(db_column='FIELD_NAME', max_length=70)
    user_type_id = models.CharField(db_column='USER_TYPE_ID', max_length=70)
    xml_id = models.CharField(
        db_column='XML_ID', max_length=255, blank=True, null=True)
    sort = models.IntegerField(db_column='SORT', blank=True, null=True)
    multiple = models.IntegerField(db_column='MULTIPLE')
    mandatory = models.IntegerField(db_column='MANDATORY')
    show_filter = models.IntegerField(db_column='SHOW_FILTER')
    show_in_list = models.IntegerField(db_column='SHOW_IN_LIST')
    edit_in_list = models.IntegerField(db_column='EDIT_IN_LIST')
    is_searchable = models.IntegerField(db_column='IS_SEARCHABLE')

    class Meta:
        managed = False
        db_table = 'p_user_field'


class UserFieldEnum(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    xml_id = models.CharField(max_length=255, blank=True, null=True)

    user_field = models.ForeignKey(
        UserField, on_delete=models.CASCADE, related_name='user_field')

    class Meta:
        managed = False
        db_table = 'p_user_field_enum'
