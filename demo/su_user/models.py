# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import hashlib
import re

from django.db import models

from utils.demo_help import Language, ValidationError, random_str, RET


class SoOrder(models.Model):
    buyer_id = models.IntegerField()
    shop_id = models.IntegerField()
    parent_id = models.IntegerField()
    order_sn = models.CharField(max_length=32)
    order_type = models.IntegerField(blank=True, null=True)
    charge_id = models.IntegerField(blank=True, null=True)
    shopping_id = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    goods_count = models.IntegerField()
    is_frozen = models.IntegerField()
    from_source = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField()
    remark = models.CharField(max_length=64, blank=True, null=True)
    resource = models.CharField(max_length=128, blank=True, null=True)
    refund_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'so_order'


class SoOrderGoods(models.Model):
    goods_name = models.CharField(max_length=128)
    goods_classify = models.TextField(blank=True, null=True)
    count = models.IntegerField()
    money = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.CharField(max_length=128, blank=True, null=True)
    comment_id = models.IntegerField(blank=True, null=True)
    sf_id = models.IntegerField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    goods_id = models.IntegerField(blank=True, null=True)
    should_money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shop_coupons = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pt_coupons = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'so_order_goods'


class SuUsers(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    mobile = models.CharField(max_length=32, blank=True, null=True)
    international_tel_code = models.CharField(max_length=32, blank=True, null=True)
    username = models.CharField(max_length=32, blank=True, null=True)
    nick_name = models.CharField(max_length=32, blank=True, null=True)
    header = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=32, blank=True, null=True)
    salt = models.CharField(max_length=4, blank=True, null=True)
    wx_union_id = models.CharField(unique=True, max_length=64, blank=True, null=True)
    qq_union_id = models.CharField(unique=True, max_length=64, blank=True, null=True)
    wb_union_id = models.CharField(unique=True, max_length=64, blank=True, null=True)
    status = models.IntegerField()
    reg_time = models.IntegerField()
    last_login_time = models.IntegerField(blank=True, null=True)
    register_source = models.IntegerField()

    def get_password(self, password, salt):
        md5 = hashlib.md5()
        md5.update(password.encode('utf8'))
        password = md5.hexdigest()

        md5 = hashlib.md5()
        md5.update(password.encode('utf8'))
        password = md5.hexdigest()

        md5 = hashlib.md5()
        md5.update(password.encode('utf8'))
        md5.update(salt.encode('utf8'))
        password = md5.hexdigest()
        return password

    def set_password(self, password):
        """
        设置密码
        :param password: 密码
        :return:
        """
        # if not re.match("^(?:(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])).{6,16}$", password):
        if not re.match(r"[0-9a-zA-Z~!@#$%^&*?\.+\-,/]{6,16}$", password):
            raise ValidationError(RET.DATAERR, Language.get("password_err"))

        self.salt = random_str(4)
        self.password = self.get_password(password, self.salt)

    def verification_password(self, password):
        """
        验证密码是否正确
        :param password: 密码
        :return:
        """
        password = self.get_password(password, self.salt)
        return self.password == password

    class Meta:
        managed = False
        db_table = 'su_users'
