import hashlib
import uuid

def my_str():
    str1=uuid.uuid4()
    u=str(str1).encode()
    md=hashlib.md5()
    md.update(u)
    return md.hexdigest()