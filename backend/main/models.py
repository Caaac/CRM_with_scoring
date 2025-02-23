from django.db import models

class PUserField(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    entity_id = models.BigIntegerField()
    field_name = models.CharField(max_length=70)
    user_type_id = models.CharField(max_length=70)
    xml_id = models.CharField(max_length=255, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    multiple = models.BooleanField(default=False)
    mandatory = models.BooleanField(default=False)
    show_filter = models.BooleanField(default=False)
    show_in_list = models.BooleanField(default=False)
    edit_in_list = models.BooleanField(default=False)
    is_searchable = models.BigIntegerField()

    class Meta:
        db_table = 'p_user_field'


class PUserFieldEnum(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    xml_id = models.CharField(max_length=255, blank=True, null=True)

    user_field = models.ForeignKey(PUserField, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'p_user_field_enum'


class PUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    login = models.BigIntegerField()
    email = models.BigIntegerField()
    password = models.BigIntegerField()
    date_register = models.BigIntegerField()
    last_login = models.BigIntegerField()
    name = models.BigIntegerField()
    last_name = models.BigIntegerField()
    personal_gender = models.CharField(max_length=1)
    personal_photo = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'p_user'


class POption(models.Model):
    module = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    value = models.TextField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'p_option'