from django.db import models

class CrmContact(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='NAME', max_length=255)
    last_name = models.CharField(db_column='LAST_NAME', max_length=255)
    second_name = models.CharField(db_column='SECOND_NAME', max_length=255)
    created_by_id = models.BigIntegerField(db_column='CREATED_BY_ID')
    birthdate = models.DateField(db_column='BIRTHDATE', blank=True, null=True)
    photo = models.BigIntegerField(db_column='PHOTO', blank=True, null=True)
    modify_by_id = models.BigIntegerField(db_column='MODIFY_BY_ID', blank=True, null=True)
    assigned_by_id = models.BigIntegerField(db_column='ASSIGNED_BY_ID', blank=True, null=True)
    company_id = models.BigIntegerField(db_column='COMPANY_ID', blank=True, null=True)
    source_id = models.BigIntegerField(db_column='SOURCE_ID', blank=True, null=True)
    lead_id = models.BigIntegerField(db_column='LEAD_ID', blank=True, null=True)
    date_create = models.DateTimeField(db_column='DATE_CREATE')
    date_modify = models.DateTimeField(db_column='DATE_MODIFY')

    class Meta:
        managed = False
        db_table = 'p_crm_contact'


class CrmDeal(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    title = models.CharField(db_column='TITLE', max_length=255)
    created_by_id = models.BigIntegerField(db_column='CREATED_BY_ID')
    modify_by_id = models.BigIntegerField(db_column='MODIFY_BY_ID', blank=True, null=True)
    assigned_by_id = models.BigIntegerField(db_column='ASSIGNED_BY_ID')
    lead_id = models.BigIntegerField(db_column='LEAD_ID', blank=True, null=True)
    company_id = models.BigIntegerField(db_column='COMPANY_ID', blank=True, null=True)
    contact_id = models.BigIntegerField(db_column='CONTACT_ID', blank=True, null=True)
    stage_id = models.CharField(db_column='STAGE_ID', max_length=255)
    is_new = models.IntegerField(db_column='IS_NEW')
    closed = models.IntegerField(db_column='CLOSED')
    type_id = models.BigIntegerField(db_column='TYPE_ID')
    opportunity = models.CharField(db_column='OPPORTUNITY', max_length=255, blank=True, null=True)
    date_create = models.DateTimeField(db_column='DATE_CREATE')
    date_modify = models.DateTimeField(db_column='DATE_MODIFY')

    class Meta:
        managed = False
        db_table = 'p_crm_deal'


class CrmFieldMulti(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    entity = models.CharField(db_column='ENTITY', max_length=25)
    element_id = models.BigIntegerField(db_column='ELEMENT_ID')
    type_id = models.CharField(db_column='TYPE_ID', max_length=20)
    value_type = models.CharField(db_column='VALUE_TYPE', max_length=30)
    value = models.CharField(db_column='VALUE', max_length=255)

    class Meta:
        managed = False
        db_table = 'p_crm_field_multi'


class CrmStatus(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    entity_id = models.CharField(db_column='ENTITY_ID', max_length=255)
    status_id = models.CharField(db_column='STATUS_ID', max_length=255)
    title = models.CharField(db_column='TITLE', max_length=255)
    color = models.CharField(db_column='COLOR', max_length=255)
    system_status = models.IntegerField(db_column='SYSTEM_STATUS')
    semantics = models.CharField(db_column='SEMANTICS', max_length=1, blank=True, null=True)
    sort = models.BigIntegerField(db_column='SORT')

    class Meta:
        managed = False
        db_table = 'p_crm_status'