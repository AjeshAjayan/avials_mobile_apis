# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Managers(models.Model):
    fullname = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    place = models.IntegerField(blank=True, null=True)
    is_terminated = models.BooleanField(blank=True, null=True)
    is_resigned = models.BooleanField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_joining = models.DateTimeField(blank=True, null=True)
    is_verified = models.BooleanField(blank=True, null=True)
    users_permissions_user = models.IntegerField(blank=True, null=True)
    users_permissions_role = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'managers'
