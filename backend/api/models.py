# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Company(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.
    ful_name = models.CharField(db_column='FUL_NAME', max_length=255)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=255)  # Field name made lowercase.
    inn = models.BigIntegerField(db_column='INN')  # Field name made lowercase.
    kpp = models.BigIntegerField(db_column='KPP')  # Field name made lowercase.
    industry = models.CharField(db_column='INDUSTRY', max_length=255)  # Field name made lowercase.
    phone = models.BigIntegerField(db_column='PHONE')  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=255)  # Field name made lowercase.
    revenue = models.BigIntegerField(db_column='REVENUE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'company'


class Contact(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.
    last_name = models.CharField(db_column='LAST_NAME', max_length=255)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=255)  # Field name made lowercase.
    source = models.CharField(db_column='SOURCE', max_length=255)  # Field name made lowercase.
    phone = models.BigIntegerField(db_column='PHONE')  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contact'


class CrmDeal(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=255)  # Field name made lowercase.
    stage = models.CharField(db_column='STAGE', max_length=255)  # Field name made lowercase.
    contant = models.ForeignKey(Contact, models.DO_NOTHING, db_column='CONTANT_ID', blank=True, null=True)  # Field name made lowercase.
    company = models.ForeignKey(Company, models.DO_NOTHING, db_column='COMPANY_ID', blank=True, null=True)  # Field name made lowercase.
    responsible = models.ForeignKey('Users', models.DO_NOTHING, db_column='RESPONSIBLE_ID')  # Field name made lowercase.
    source = models.CharField(db_column='SOURCE', max_length=255)  # Field name made lowercase.
    comment = models.TextField(db_column='COMMENT', blank=True, null=True)  # Field name made lowercase.
    date_closed = models.DateField(db_column='DATE_CLOSED')  # Field name made lowercase.
    landing_date = models.ForeignKey('LandingRate', models.DO_NOTHING, db_column='LANDING_DATE_ID')  # Field name made lowercase.
    result = models.IntegerField(db_column='RESULT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crm_deal'


class LandingRate(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=255)  # Field name made lowercase.
    rate = models.FloatField(db_column='RATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'landing_rate'


class Statement(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    count_month = models.IntegerField(db_column='COUNT_MONTH')  # Field name made lowercase.
    count_contact = models.IntegerField(db_column='COUNT_CONTACT')  # Field name made lowercase.
    count_company = models.IntegerField(db_column='COUNT_COMPANY')  # Field name made lowercase.
    money_turnover = models.BigIntegerField(db_column='MONEY_TURNOVER')  # Field name made lowercase.
    comment = models.TextField(db_column='COMMENT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'statement'


class Users(models.Model):
    id = models.OneToOneField(Statement, models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.
    last_name = models.CharField(db_column='LAST_NAME', max_length=255)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=255)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'