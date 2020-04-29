# import hashlib
# import re
# import time
#
# from django.db import models
#
# # Create your models here.
# from utils.demo_help import ValidationError, RET, Language, random_str
#
#
# class SuUsers(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     email = models.CharField(unique=True, max_length=128, null=True)
#     mobile = models.CharField(unique=True, max_length=32, null=True)
#     international_tel_code = models.CharField(max_length=32, blank=True, null=True)
#     username = models.CharField(max_length=32, blank=True, null=True)
#     nick_name = models.CharField(max_length=32, blank=True, null=True)
#     header = models.CharField(max_length=255, blank=True, null=True)
#     password = models.CharField(max_length=32, blank=True, null=True)
#     salt = models.CharField(max_length=4, blank=True, null=True)
#     wx_union_id = models.CharField(max_length=64, blank=True, null=True)
#     qq_union_id = models.CharField(max_length=64, blank=True, null=True)
#     wb_union_id = models.CharField(max_length=64, blank=True, null=True)
#     status = models.IntegerField(default=1)
#     reg_time = models.IntegerField(default=time.time)
#     last_login_time = models.IntegerField(blank=True, null=True)
#     register_source = models.IntegerField(default=1)
#     identity = models.IntegerField(blank=True, null=True)
#
#     def get_password(self, password, salt):
#         md5 = hashlib.md5()
#         md5.update(password.encode('utf8'))
#         password = md5.hexdigest()
#
#         md5 = hashlib.md5()
#         md5.update(password.encode('utf8'))
#         password = md5.hexdigest()
#
#         md5 = hashlib.md5()
#         md5.update(password.encode('utf8'))
#         md5.update(salt.encode('utf8'))
#         password = md5.hexdigest()
#         return password
#
#     def set_password(self, password):
#         """
#         设置密码
#         :param password: 密码
#         :return:
#         """
#         # if not re.match("^(?:(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])).{6,16}$", password):
#         if not re.match(r"[0-9a-zA-Z~!@#$%^&*?\.+\-,/]{6,16}$", password):
#             raise ValidationError(RET.DATAERR, Language.get("password_err"))
#
#         self.salt = random_str(4)
#         self.password = self.get_password(password, self.salt)
#
#     def verification_password(self, password):
#         """
#         验证密码是否正确
#         :param password: 密码
#         :return:
#         """
#         password = self.get_password(password, self.salt)
#         return self.password == password
#
#     class Meta:
#         managed = False
#         db_table = 'su_users'
