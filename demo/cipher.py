

def md5(target):
    return hashlib.md5(target.encode("utf-8")).hexdigest()
    