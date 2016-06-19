import datetime
import OpenSSL.crypto
import os


def load_certificate(path, password=None):
    if os.path.splitext(path)[1] in ['.p12', '.pfx']:
        if password is None:
            raise TypeError('cannot open p12 file without a password')
        return certificate_from_p12(path, password)
    elif os.path.splitext(path)[1] in ['.cer', '.crt']:
        return certificate_from_cer(path)
    elif os.path.splitext(path)[1] in ['.pem']:
        return certificate_from_pem(path)
    else:
        raise TypeError('cannot choose certificate type')


def certificate_from_p12(path, password):
    p12 = OpenSSL.crypto.load_pkcs12(open(path, 'rb').read(), password)
    return p12.get_certificate()


def certificate_from_pem(path):
    pem = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, open(path, 'rb').read())
    return pem


def certificate_from_cer(path):
    cer = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, open(path, 'rb').read())
    return cer


def get_certificate_subject(cert):
    return cert.get_subject()


def get_certificate_cn(cert):
    subject = get_certificate_subject(cert)
    return subject.commonName


def get_certificate_expiration_date(cert):
    return datetime.datetime.strptime(cert.get_notAfter(), '%Y%m%d%H%M%SZ')
