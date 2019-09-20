# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager


class SysButton(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    create_user_id = models.IntegerField(db_column='CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    icon = models.CharField(db_column='ICON', max_length=30, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    code = models.TextField(db_column='CODE', blank=True, null=True)  # Field name made lowercase.
    # platform_id = models.IntegerField(db_column='PLATFORM_ID', blank=True, null=True)  # Field name made lowercase.
    # platform_name = models.CharField(db_column='PLATFORM_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    create_user_name = models.CharField(db_column='CREATE_USER_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_button'


class SysMenu(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    parent_id = models.IntegerField(db_column='PARENT_ID', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    # orderby = models.IntegerField(db_column='ORDERBY', blank=True, null=True)  # Field name made lowercase.
    # is_leaf = models.CharField(db_column='IS_LEAF', max_length=10, blank=True, null=True)  # Field name made lowercase.
    # is_quick_in = models.IntegerField(db_column='IS_QUICK_IN', blank=True, null=True)  # Field name made lowercase.
    icon = models.CharField(db_column='ICON', max_length=30, blank=True, null=True)  # Field name made lowercase.
    # platform_id = models.IntegerField(db_column='PLATFORM_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_menu'


class SysMenuButton(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    menu_id = models.ForeignKey('SysMenu', on_delete=models.CASCADE)  # Field name made lowercase.
    button_id = models.ForeignKey('SysButton', on_delete=models.CASCADE)  # Field name made lowercase.
    # button_url = models.CharField(db_column='BUTTON_URL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    # platform_id = models.IntegerField(db_column='PLATFORM_ID', blank=True, null=True)  # Field name made lowercase.
    # full_url = models.CharField(db_column='FULL_URL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_menu_button'


class SysOrg(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    parent_id = models.CharField(db_column='PARENT_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    # orgidpath = models.TextField(db_column='ORGIDPATH', blank=True, null=True)  # Field name made lowercase.
    # org_type = models.SmallIntegerField(db_column='ORG_TYPE', blank=True, null=True)  # Field name made lowercase.
    # org_style = models.CharField(db_column='ORG_STYLE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    # first_id = models.IntegerField(db_column='FIRST_ID', blank=True, null=True)  # Field name made lowercase.
    # is_leaf = models.CharField(db_column='IS_LEAF', max_length=10, blank=True, null=True)  # Field name made lowercase.
    create_user_id = models.IntegerField(db_column='CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.
    update_user_id = models.IntegerField(db_column='UPDATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    # orgnamepath = models.TextField(db_column='ORGNAMEPATH', blank=True, null=True)  # Field name made lowercase.
    # orgdesc = models.TextField(db_column='ORGDESC', blank=True, null=True)  # Field name made lowercase.
    # staff = models.CharField(db_column='STAFF', max_length=50, blank=True, null=True)  # Field name made lowercase.
    # short_name = models.CharField(db_column='SHORT_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    # is_depedencies = models.CharField(db_column='IS_DEPEDENCIES', max_length=5, blank=True, null=True)  # Field name made lowercase.
    # platform_id = models.IntegerField(db_column='PLATFORM_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_org'


class SysOrgRole(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    role_id = models.ForeignKey('SysRole', on_delete=models.CASCADE)  # Field name made lowercase.
    org_id = models.ForeignKey('SysOrg', on_delete=models.CASCADE)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    # platform_id = models.IntegerField(db_column='PLATFORM_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_org_role'


class SysRole(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='REMARK', blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.
    update_user_id = models.IntegerField(db_column='UPDATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    create_user_id = models.IntegerField(db_column='CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    # company_id = models.CharField(db_column='COMPANY_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    # identity = models.CharField(db_column='IDENTITY', max_length=10, blank=True, null=True)  # Field name made lowercase.
    # role_type = models.SmallIntegerField(db_column='ROLE_TYPE', blank=True, null=True)  # Field name made lowercase.
    # system_type = models.SmallIntegerField(db_column='SYSTEM_TYPE', blank=True, null=True)  # Field name made lowercase.
    # platform_id = models.IntegerField(db_column='PLATFORM_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_role'


class SysRoleButton(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    role_id = models.ForeignKey('SysRole', on_delete=models.CASCADE)  # Field name made lowercase.
    button_id = models.ForeignKey('SysButton', on_delete=models.CASCADE)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    menu_id = models.ForeignKey('SysMenu', on_delete=models.CASCADE)  # Field name made lowercase.
    # platform_id = models.IntegerField(db_column='PLATFORM_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_role_button'


class SysRoleMenu(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    role_id = models.ForeignKey('SysRole', on_delete=models.CASCADE)  # Field name made lowercase.
    menu_id = models.ForeignKey('SysMenu', on_delete=models.CASCADE)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    # platform_id = models.IntegerField(db_column='PLATFORM_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_role_menu'


# class SysRoleParam(models.Model):
#     id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
#     role_id = models.ForeignKey('SysRole', on_delete=models.CASCADE)  # Field name made lowercase.
#     param_id = models.ForeignKey('')  # Field name made lowercase.
#     status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     platform_id = models.IntegerField(db_column='PLATFORM_ID', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'sys_role_param'


class SysUser(models.Model):
    # identifier = models.CharField(max_length=40, unique=True)
    # USERNAME_FIELD = 'identifier'

    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    account = models.CharField(db_column='ACCOUNT', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=100)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=32)  # Field name made lowercase.
    # birthday = models.DateTimeField(db_column='BIRTHDAY', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=32, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    # mobile = models.CharField(db_column='MOBILE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    # email = models.CharField(db_column='EMAIL', max_length=32, blank=True, null=True)  # Field name made lowercase.
    # address = models.TextField(db_column='ADDRESS', blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.
    update_user_id = models.IntegerField(db_column='UPDATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    create_user_id = models.IntegerField(db_column='CREATE_USER_ID', blank=True, null=True)  # Field name made lowercase.
    # agent_id = models.CharField(db_column='AGENT_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    # agent_phone = models.CharField(db_column='AGENT_PHONE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    # agent_last_login_time = models.DateTimeField(db_column='AGENT_LAST_LOGIN_TIME', blank=True, null=True)  # Field name made lowercase.
    # user_icon = models.CharField(db_column='USER_ICON', max_length=50, blank=True, null=True)  # Field name made lowercase.
    # role_type = models.CharField(db_column='ROLE_TYPE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    staff = models.CharField(db_column='STAFF', max_length=50, blank=True, null=True)  # Field name made lowercase.
    # user_zw = models.CharField(db_column='USER_ZW', max_length=100, blank=True, null=True)  # Field name made lowercase.
    # task_notice_min = models.CharField(db_column='TASK_NOTICE_MIN', max_length=32, blank=True, null=True)  # Field name made lowercase.
    # models.ForeignKey(to="Publish", to_field="nid")
    # org_id = models.IntegerField(db_column='ORG_ID', blank=True, null=True)  # Field name made lowercase.
    org_id = models.ForeignKey(db_column='ORG_ID', to="SysOrg", to_field="id",blank=True, null=True,on_delete=models.CASCADE)  # Field name made lowercase.
    # task_message_min = models.CharField(db_column='TASK_MESSAGE_MIN', max_length=32, blank=True, null=True)  # Field name made lowercase.
    # agent_pwd = models.CharField(db_column='AGENT_PWD', max_length=32, blank=True, null=True)  # Field name made lowercase.
    # config_status = models.CharField(db_column='CONFIG_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    # night_account = models.CharField(db_column='NIGHT_ACCOUNT', max_length=32, blank=True, null=True)  # Field name made lowercase.
    # submit_status = models.CharField(db_column='SUBMIT_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    # marry_date = models.CharField(db_column='MARRY_DATE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    # kids_born_date = models.CharField(db_column='KIDS_BORN_DATE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    # marital_status = models.CharField(db_column='MARITAL_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    # bearing_status = models.CharField(db_column='BEARING_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    # politics_status = models.CharField(db_column='POLITICS_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    # census_register_type = models.CharField(db_column='CENSUS_REGISTER_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    # native_place = models.CharField(db_column='NATIVE_PLACE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    # nation = models.CharField(db_column='NATION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    # oa_account = models.CharField(db_column='OA_ACCOUNT', max_length=128, blank=True, null=True)  # Field name made lowercase.
    # oa_account_status = models.CharField(db_column='OA_ACCOUNT_STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    # platform_id = models.IntegerField(db_column='PLATFORM_ID', blank=True, null=True)  # Field name made lowercase.
    # department_name = models.CharField(db_column='DEPARTMENT_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    # department_path = models.CharField(db_column='DEPARTMENT_PATH', max_length=100, blank=True, null=True)  # Field name made lowercase.
    # modify_password_lasttime = models.DateTimeField(db_column='MODIFY_PASSWORD_LASTTIME', blank=True, null=True)  # Field name made lowercase.
    # objects = UserManager()
    class Meta:
        # managed = False
        db_table = 'sys_user'


class SysUserOrg(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.ForeignKey('SysUser', on_delete=models.CASCADE)  # Field name made lowercase.
    org_id = models.ForeignKey('SysOrg', on_delete=models.CASCADE)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    # platform_id = models.IntegerField(db_column='PLATFORM_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_user_org'


class SysUserRole(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.ForeignKey('SysUser', on_delete=models.CASCADE)  # Field name made lowercase.
    role_id = models.ForeignKey('SysRole', on_delete=models.CASCADE)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    # platform_id = models.IntegerField(db_column='PLATFORM_ID', blank=True, null=True)  # Field name made lowercase.
    org_id = models.ForeignKey('SysOrg', on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_user_role'
