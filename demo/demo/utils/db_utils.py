"""
@Author				: xiaotao
@Email				: 18773993654@163.com
@Lost modifid		: 2020/6/6 08:39
@Filename			: db_utils.py
@Description		: 
@Software           : PyCharm
"""
from django.db import connections


def dict_fetchall(cursor):
    """""Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def cursor_execute(sql, db_name="mes"):
    """execute sql"""
    with connections[db_name].cursor() as cursor:
        # cursor.callproc()
        cursor.execute(sql)
        rows = dict_fetchall(cursor)
    return rows
