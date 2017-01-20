# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    iduser = models.AutoField(db_column='idUser', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=45)
    password = models.CharField(max_length=45)
    type = models.CharField(db_column='Type', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'User'


class Answer(models.Model):
    idanswer = models.IntegerField(primary_key=True)
    idquiz = models.IntegerField(blank=True, null=True)
    ans = models.CharField(max_length=45, blank=True, null=True)
    yans = models.CharField(db_column='yAns', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'answer'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Quetion(models.Model):
    idquetion = models.AutoField(primary_key=True)
    idquiz = models.IntegerField()
    q_d = models.CharField(max_length=45)
    a = models.CharField(db_column='A', max_length=45, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=45, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=45, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ans = models.CharField(db_column='Ans', max_length=45, blank=True, null=True)  # Field name made lowercase.
    marks = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'quetion'


class Quizdetails(models.Model):
    idquiz = models.AutoField(primary_key=True)
    creator = models.CharField(max_length=45)
    timelimit = models.IntegerField(db_column='timeLimit', blank=True, null=True)  # Field name made lowercase.
    subject = models.CharField(max_length=45, blank=True, null=True)
    total = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'quizDetails'


class Userrecord(models.Model):
    iduserrecord = models.AutoField(db_column='iduserRecord', primary_key=True)  # Field name made lowercase.
    idquiz = models.IntegerField(blank=True, null=True)
    iduser = models.IntegerField(db_column='idUser', blank=True, null=True)  # Field name made lowercase.
    score = models.IntegerField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
    userrecordcol = models.CharField(db_column='userRecordcol', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'userRecord'
