CREATE TABLE `so_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '订单ID',
  `buyer_id` int(11) NOT NULL COMMENT '买家ID',
  `shop_id` int(11) NOT NULL DEFAULT '0' COMMENT '店铺ID,母订单ID为空',
  `parent_id` int(11) NOT NULL DEFAULT '0' COMMENT '母订单号',
  `order_sn` varchar(32) NOT NULL COMMENT '订单号',
  `order_type` tinyint(11) DEFAULT '0' COMMENT '订单类型 0：库存类，1: 定制类，2：生产类',
  `charge_id` int(11) DEFAULT NULL COMMENT '费用信息ID',
  `shopping_id` int(11) NOT NULL COMMENT '订单快递ID，（收货人，联系手机号，收货地址，配送费）',
  `status` tinyint(1) DEFAULT '0' COMMENT '订单状态  (库存类 0：取消订单， 1：待付款，2：待发货，3：待收货，4：待评价，5：已完成) （定制类 0：取消订单， 1：待接单，2：待付款，3：待确认印刷，4：待发货，  5：待收货，6：待评价，7：已完成） （生产类  0：取消订单，1：待付款，2：待确认印刷，3：待发货，  4：待收货，5：待评价，6：已完成）',
  `goods_count` int(11) NOT NULL DEFAULT '1' COMMENT '商品总数',
  `is_frozen` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否冻结订单，0：否，1：是',
  `from_source` tinyint(1) DEFAULT '0' COMMENT '平台,0[pc], 1[APP], 2[h5]',
  `create_time` int(11) NOT NULL COMMENT '下单时间',
  `remark` varchar(64) DEFAULT NULL COMMENT '订单备注',
  `resource` varchar(128) DEFAULT NULL COMMENT '来源,第三方推荐地址',
  `refund_id` int(11) DEFAULT NULL COMMENT '退款ID',
  PRIMARY KEY (`id`),
  KEY `buyer_id` (`buyer_id`) USING HASH,
  KEY `shop_id` (`shop_id`) USING HASH
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COMMENT='订单信息';



CREATE TABLE `so_order_goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '商品订单ID',
  `goods_name` varchar(128) NOT NULL COMMENT '商品名称',
  `goods_classify` text COMMENT '商品分类',
  `count` int(11) NOT NULL DEFAULT '1' COMMENT '商品数量',
  `money` decimal(10,2) NOT NULL COMMENT '商品价格（初始金额）',
  `image_url` varchar(128) DEFAULT NULL COMMENT '图片地址',
  `comment_id` int(11) DEFAULT NULL COMMENT '评价信息ID',
  `sf_id` int(11) DEFAULT NULL COMMENT '生产类订单，sf ID',
  `order_id` int(11) DEFAULT NULL COMMENT '订单ID',
  `goods_id` int(11) DEFAULT NULL COMMENT '商家ID',
  `should_money` decimal(10,2) DEFAULT '0.00' COMMENT '分摊后的应付金额',
  `shop_coupons` decimal(10,2) DEFAULT NULL COMMENT '商家优惠金额',
  `pt_coupons` decimal(10,2) DEFAULT NULL COMMENT '平台优惠金额',
  PRIMARY KEY (`id`),
  KEY `order_id` (`order_id`) USING HASH
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COMMENT='订单商品';


DROP TABLE IF EXISTS `su_users`;
CREATE TABLE `su_users` (
  `user_id` int(10) NOT NULL AUTO_INCREMENT COMMENT '用户id',
  `email` varchar(128) DEFAULT '' COMMENT '邮箱',
  `mobile` varchar(32) DEFAULT '' COMMENT '手机号',
  `international_tel_code` varchar(32) DEFAULT '86' COMMENT '国际电话区号',
  `username` varchar(32) DEFAULT NULL COMMENT '昵称',
  `nick_name` varchar(32) DEFAULT NULL COMMENT '用户名',
  `header` varchar(255) DEFAULT NULL COMMENT '头像图片地址',
  `password` varchar(32) DEFAULT NULL COMMENT '密码',
  `salt` char(4) DEFAULT NULL COMMENT '密码盐',
  `wx_union_id` varchar(64) DEFAULT NULL COMMENT '微信对应平台unionId',
  `qq_union_id` varchar(64) DEFAULT NULL COMMENT 'qq对应平台唯一unionId',
  `wb_union_id` varchar(64) DEFAULT NULL COMMENT '微博对应平台唯一unionId',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '用户状态,1[激活],2[冻结]',
  `reg_time` int(11) NOT NULL COMMENT '注册时间',
  `last_login_time` int(11) DEFAULT NULL COMMENT '最后登录时间',
  `register_source` tinyint(1) NOT NULL DEFAULT '1' COMMENT '注册来源,1[pc],2[qq],3[微博],4[微信],5[APP],6[h5]',
  PRIMARY KEY (`user_id`),
  KEY `email` (`email`),
  KEY `mobile` (`mobile`),
	UNIQUE KEY `wx_union_id` (`wx_union_id`),
	UNIQUE KEY `qq_union_id` (`qq_union_id`),
	UNIQUE KEY `wb_union_id` (`wb_union_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户主表';