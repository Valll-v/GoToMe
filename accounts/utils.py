import hashlib


def encode(str_) -> str:
    return hashlib.sha256(str_.encode('utf-8')).hexdigest()
