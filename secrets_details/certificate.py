import datetime
import OpenSSL.crypto
import os

def load_certificate():
    


def parse_p12(path, password):
    p12 = OpenSSL.crypto.load_pkcs12(file(path, 'rb').read(), password)
    return p12

def get_certificate_subject(p12):
    cert = p12.get_certificate()
    return cert.get_subject()

def get_certificate_expiration_date(p12):
    cert = p12.get_certificate()
    return datetime.datetime.strptime(cert.get_notAfter(), '%Y%m%d%H%M%SZ')