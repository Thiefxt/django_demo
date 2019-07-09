"""
@Author				: WarmXiao
@Email				: warm.xiao@ecoprint.tech
@Lost modifid		: 6/29/19 02:57
@Filename			: filter_test.py
@Description		: 
@Software           : PyCharm
"""
from rest_framework.filters import BaseFilterBackend


class IsOwnerFilterBackend(BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):


        return queryset.filter(owner=request.user)