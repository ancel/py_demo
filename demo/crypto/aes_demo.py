from Crypto.Cipher import AES
from Crypto import Random
import base64

key = Random.new().read(AES.block_size)  # 随机生成密钥
iv = Random.new().read(AES.block_size)   # 随机生成IV

BS = 16  # 分组数据长度
# 填充补齐最后一块数据
# 例如需要补5个字节，在后面填充5个\x05
# 补12个字节则填充12个\x0c
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 

# 删除补充的数据
# 最后一位是\x06则删除末尾6个字节
unpad = lambda s : s[0:-ord(s[-1:])]

msg = "Hello AES Encryption"

# Encryption
cbc_cipher = AES.new(key, AES.MODE_CBC, IV=iv)
cipher_text = iv + cbc_cipher.encrypt(pad(msg))  # 将IV和密文一起传送
# Decryption
cbc_decipher = AES.new(key, AES.MODE_CBC, IV=cipher_text[:16])  #  密文前16位为IV
# 前16位为IV，不需要解密
decrypted_text = cbc_decipher.decrypt(cipher_text[16:])
print('CBC Mode Encrypted text: ', base64.urlsafe_b64encode(cipher_text))  # 对字节数据进行base64编码
print('CBC Mode Decrypted text: ', unpad(decrypted_text))  # 去除末尾的填充字符