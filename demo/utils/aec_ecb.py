"""
@Author				: WarmXiao
@Email				: warm.xiao@ecoprint.tech
@Lost modifid		: 19-8-26 19:24
@Filename			: aec_ecb.py
@Description		: 
@Software           : PyCharm
"""
import base64
import hashlib

from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
import base64


class AESCipher(object):

    def __init__(self, key):
        self.key = hashlib.md5(key.encode('utf8')).hexdigest().encode()
        self.unpad = lambda date: date[0:-ord(date[-1])]

    def aes_cipher(self, aes_str):
        # 使用key,选择加密方式
        aes = AES.new(self.key, AES.MODE_ECB)
        pad_pkcs7 = pad(aes_str.encode('utf-8'), AES.block_size, style='pkcs7')  # 选择pkcs7补全
        encrypt_aes = aes.encrypt(pad_pkcs7)
        # 加密结果
        # raw = self.pad(raw)
        # cipher = AES.new(self.key, AES.MODE_ECB)
        # return base64.b64encode(encrypt_aes).decode()

        encrypted_text = str(base64.b64encode(encrypt_aes), encoding='utf-8')  # 解码
        encrypted_text_str = encrypted_text.replace("\n", "")
        # 此处我的输出结果老有换行符，所以用了临时方法将它剔除
        return encrypted_text_str

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, decrData):  # 解密函数
        enc = base64.b64decode(decrData)
        aes = AES.new(self.key, AES.MODE_ECB)
        msg = aes.decrypt(enc).decode("utf8")
        return self.unpad(msg)


if __name__ == '__main__':
    key = 'X8fE6Gh6aC9dU1w2j3F6hdMv6lODe4dc'
    dict_msg = "{'return_code': 'SUCCESS', 'appid': 'wx2421b1c4370ec43b', 'mch_id': '10000100', 'nonce_str': 'TeqClE3i0mvn3DrK'}"
    msg = 'xZqBC03qLVAevnP6W7IA18TRxSDY2mt2Xeny4/YtWsAD9H2U3wXmNQqV1ts2OEJRBw1PpicxVrKcGyskpAcOy5UVFUDiSne2ksDzN7wXS1ziLY3T1XPTkhLsDyCJ+3PQ9Y/eYpm2CK7yXAqXbvZMpYaNpZeN7mvMUlMRiN+IdyA='
    print(AESCipher(key).aes_cipher(dict_msg))
    print(AESCipher(key).decrypt(msg))
