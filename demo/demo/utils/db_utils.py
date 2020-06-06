"""
@Author				: xiaotao
@Email				: 18773993654@163.com
@Lost modifid		: 2020/6/6 08:39
@Filename			: db_utils.py
@Description		: 
@Software           : PyCharm
"""


def dict_fetchall(cursor):
    """""Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
