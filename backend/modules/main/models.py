from django.db import models

class UserField(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    title = models.CharField(db_column='TITLE', max_length=255)
    entity_id = models.CharField(db_column='ENTITY_ID', max_length=70)
    field_name = models.CharField(db_column='FIELD_NAME', max_length=70)
    user_type_id = models.CharField(db_column='USER_TYPE_ID', max_length=70)
    xml_id = models.CharField(db_column='XML_ID', max_length=255, blank=True, null=True)
    sort = models.IntegerField(db_column='SORT', blank=True, null=True)
    multiple = models.IntegerField(db_column='MULTIPLE')
    mandatory = models.IntegerField(db_column='MANDATORY')
    show_filter = models.IntegerField(db_column='SHOW_FILTER')
    show_in_list = models.IntegerField(db_column='SHOW_IN_LIST')
    edit_in_list = models.IntegerField(db_column='EDIT_IN_LIST')
    is_searchable = models.IntegerField(db_column='IS_SEARCHABLE')

    class Meta:
        db_table = 'p_user_field'


class UserFieldEnum(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    xml_id = models.CharField(max_length=255, blank=True, null=True)

    user_field = models.ForeignKey(UserField, on_delete=models.CASCADE, related_name='user_field')
    
    class Meta:
        db_table = 'p_user_field_enum'


class User(models.Model):
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


class Option(models.Model):
    module = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    value = models.TextField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'p_option'