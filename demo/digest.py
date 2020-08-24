import hashlib

def md5(target):
    h = hashlib.md5()
    h.update(target.encode("utf-8"))
    return h.hexdigest()
    
def sha1(target):
    h = hashlib.sha1()
    h.update(target.encode("utf-8"))
    return h.hexdigest()


if __name__=='__main__':
    target = '123'
    print(md5(target))
    print(sha1(target))