"""
@Author				: WarmXiao
@Email				: warm.xiao@ecoprint.tech
@Lost modifid		: 8/8/19 20:24
@Filename			: my_page.py
@Description		: 
@Software           : PyCharm
"""
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class Standard(PageNumberPagination):
    """自定义分页规则"""
    page_size = 5   # 指定默认每页显示多少条数据 如果前端未指定那就用此值
    max_page_size = 10  # 前端在指定每页显示条数时，最大限制
    page_query_param = "page"   # 指定前端在控制显示第几页时的查询关键字名字
    page_size_query_param = "page_size"     # 指定前端在控制显示每页显示多少条数据的查询关键字， 默认不写为Nonepip

    def get_paginated_response(self, data):
        rst = {
            "page_total": self.page.paginator.num_pages,  # [总页数]
            "total": self.page.paginator.count,  # [总条数]
            "page_index": self.page.number,  # [当前页数]
            "data": data
        }

        return Response(data=rst)