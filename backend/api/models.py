from django.db import models

class Company(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='NAME', max_length=255)
    ful_name = models.CharField(db_column='FUL_NAME', max_length=255)
    representative_name = models.CharField(
        db_column='REPRESENTATIVE_NAME', max_length=255)
    representative_last_name = models.CharField(
        db_column='REPRESENTATIVE_LAST_NAME', max_length=255)
    address = models.CharField(db_column='ADDRESS', max_length=255)
    inn = models.BigIntegerField(db_column='INN')
    kpp = models.BigIntegerField(db_column='KPP')
    industry = models.CharField(db_column='INDUSTRY', max_length=255)
    phone = models.BigIntegerField(db_column='PHONE')
    email = models.CharField(db_column='EMAIL', max_length=255)
    revenue = models.BigIntegerField(db_column='REVENUE')

    class Meta:
        managed = False
        db_table = 'company'


class Contact(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='NAME', max_length=255)
    last_name = models.CharField(db_column='LAST_NAME', max_length=255)
    gender = models.CharField(db_column='GENDER', max_length=255)
    source = models.CharField(db_column='SOURCE', max_length=255)
    phone = models.BigIntegerField(db_column='PHONE')
    email = models.CharField(db_column='EMAIL', max_length=255)
    person_age = models.IntegerField(
        db_column='PERSON_AGE', blank=True, null=True)
    person_income = models.BigIntegerField(
        db_column='PERSON_INCOME', blank=True, null=True)
    person_home_ownership = models.BigIntegerField(
        db_column='PERSON_HOME_OWNERSHIP', blank=True, null=True)
    person_emp_length = models.FloatField(
        db_column='PERSON_EMP_LENGTH', blank=True, null=True)
    loan_grade = models.CharField(
        db_column='LOAN_GRADE', max_length=255, blank=True, null=True)
    cb_person_cred_hist_length = models.BigIntegerField(
        db_column='CB_PERSON_CRED_HIST_LENGTH', blank=True, null=True)
    cb_person_default_on_file = models.IntegerField(
        db_column='CB_PERSON_DEFAULT_ON_FILE', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact'


class CrmDeal(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    title = models.CharField(db_column='TITLE', max_length=255)
    loan_amount = models.BigIntegerField(db_column='LOAN_AMOUNT')
    stage = models.CharField(db_column='STAGE', max_length=255)
    contant = models.ForeignKey(
        Contact, models.DO_NOTHING, db_column='CONTANT_ID', blank=True, null=True)
    company = models.ForeignKey(
        Company, models.DO_NOTHING, db_column='COMPANY_ID', blank=True, null=True)
    responsible = models.ForeignKey(
        'Users', models.DO_NOTHING, db_column='RESPONSIBLE_ID')
    source = models.CharField(
        db_column='SOURCE', max_length=255, blank=True, null=True)
    comment = models.TextField(db_column='COMMENT', blank=True, null=True)
    date_closed = models.DateField(
        db_column='DATE_CLOSED', blank=True, null=True)
    landing_rate = models.ForeignKey(
        'LandingRate', models.DO_NOTHING, db_column='LANDING_RATE_ID')
    result = models.IntegerField(db_column='RESULT', blank=True, null=True)
    profit = models.BigIntegerField(db_column='PROFIT', blank=True, null=True)
    loan_duration = models.BigIntegerField(
        db_column='LOAN_DURATION', blank=True, null=True)
    loan_status = models.BigIntegerField(
        db_column='LOAN_STATUS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_deal'


class LandingRate(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    title = models.CharField(db_column='TITLE', max_length=255)
    rate = models.FloatField(db_column='RATE')
    loan_intent = models.CharField(db_column='LOAN_INTENT', max_length=255)

    class Meta:
        managed = False
        db_table = 'landing_rate'


class Statement(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    created_by = models.ForeignKey(
        'Users', models.DO_NOTHING, db_column='CREATED_BY')
    count_month = models.IntegerField(db_column='COUNT_MONTH')
    count_contact = models.IntegerField(db_column='COUNT_CONTACT')
    count_company = models.IntegerField(db_column='COUNT_COMPANY')
    money_turnover = models.BigIntegerField(db_column='MONEY_TURNOVER')
    comment = models.TextField(db_column='COMMENT', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statement'


class Users(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='NAME', max_length=255)
    last_name = models.CharField(db_column='LAST_NAME', max_length=255)
    email = models.CharField(db_column='EMAIL', max_length=255)
    password = models.CharField(db_column='PASSWORD', max_length=255)

    class Meta:
        managed = False
        db_table = 'users'
