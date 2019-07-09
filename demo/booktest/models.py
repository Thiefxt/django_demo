# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import datetime

from django.db import models
from django.core.cache import cache


class SoOrder(models.Model):
    """订单表"""
    buyer_id = models.IntegerField()            # 买家ID
    shop_id = models.IntegerField()             # '店铺ID,母订单ID为空'
    parent_id = models.IntegerField()           # 母订单号
    order_sn = models.CharField(max_length=32)  # 订单号
    order_type = models.IntegerField(blank=True, null=True)     # 订单类型 0：库存类，1: 定制类，2：生产类
    charge_id = models.IntegerField(blank=True, null=True)      # 费用信息ID
    shopping_id = models.IntegerField()         # 订单快递ID，（收货人，联系手机号，收货地址，配送费）
    status = models.IntegerField(blank=True, null=True)     # 订单状态  (库存类 0：取消订单， 1：待付款，2：待发货，3：待收货，4：待评价，5：已完成) （定制类 0：取消订单， 1：待接单，2：待付款，3：待确认印刷，4：待发货，  5：待收货，6：待评价，7：已完成） （生产类  0：取消订单，1：待付款，2：待确认印刷，3：待发货，  4：待收货，5：待评价，6：已完成）
    goods_count = models.IntegerField()     # 商品总数
    is_frozen = models.IntegerField()       # 是否冻结订单，0：否，1：是
    from_source = models.IntegerField(blank=True, null=True)    # 平台,0[pc], 1[APP], 2[h5]
    create_time = models.IntegerField()     # 下单时间
    remark = models.CharField(max_length=64, blank=True, null=True)     # 订单备注
    resource = models.CharField(max_length=128, blank=True, null=True)      # 来源,第三方推荐地址
    refund_id = models.IntegerField(blank=True, null=True)      # 退款ID

    @staticmethod
    def create_order_sn():
        """
        生成订单号
        :return:
        """
        date_str = datetime.datetime.now().strftime('%Y%m%d')
        key = 'order_sn' + date_str
        if not cache.has_key(key):
            cache.set(key, 0, 24 * 60 * 60)
        now = cache.incr(key, 1)
        order_sn = date_str + str(now).zfill(6)
        return order_sn

    class Meta:
        managed = False
        db_table = 'so_order'


class SoOrderGoods(models.Model):
    goods_name = models.CharField(max_length=128)       # 商品名称
    goods_classify = models.TextField(blank=True, null=True)        # 商品分类
    count = models.IntegerField()           # 商品数量
    money = models.DecimalField(max_digits=10, decimal_places=2)    # 商品价格（初始金额）
    image_url = models.CharField(max_length=128, blank=True, null=True)     # 图片地址
    comment_id = models.IntegerField(blank=True, null=True)     # 评价信息ID
    sf_id = models.IntegerField(blank=True, null=True)          # 生产类订单，sf ID
    order = models.ForeignKey(SoOrder, models.DO_NOTHING, related_name="order", blank=True, null=True)        # 订单ID
    goods_id = models.IntegerField(blank=True, null=True)           # 商家ID
    should_money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)      # 分摊后的应付金额
    shop_coupons = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)      # 商家优惠金额
    pt_coupons = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)        # 平台优惠金额

    class Meta:
        managed = False
        db_table = 'so_order_goods'
