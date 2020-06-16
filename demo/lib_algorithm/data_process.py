"""
@Author				: xiaotao
@Email				: 18773993654@163.com
@Lost modifid		: 2020/6/9 08:09
@Filename			: data_process.py
@Description		: 
@Software           : PyCharm
"""
import numpy as np


def data_filtering(arr, n=1):
    """
    清洗曲线较高或较低数据，提取预期值
    :param arr: 二维数组如[[1], [2], [3]]
    :param n: 递归深度，默认1次
    :return: 预期值平均数
    """
    if n <= 0:
        return np.mean(arr)
    arr_mean = np.mean(arr)
    arr_std = np.std(arr, ddof=1)
    arr = [i for i in arr if arr_mean - arr_std < i[0] < arr_mean + arr_std]
    return data_filtering(arr, n-1)