import plistlib
import datetime
import OpenSSL.crypto
import os


class profile_details(object):

    """defines the data inside a provisioing file"""
    __slots__ = ["AppIDName", "ApplicationIdentifierPrefix", "CreationDate", "DeveloperCertificates", "Entitlements",
                 "ExpirationDate", "Name", "ProvisionedDevices", "TeamIdentifier", "TeamName", "TimeToLive", "UUID", "Version"]

    __PLIST_START = '<?xml'
    __PLIST_END = '</plist>'

    @classmethod
    def readFromFile(cls, path):
        details = profile_details()
        fn = os.path.expanduser(path)
        with open(fn) as fp:
            data = fp.read()
        if data.find(profile_details.__PLIST_START) == -1:
            print "## Not a real provisioning profile ", path, " ##"
            return None
        xml = data[data.find(profile_details.__PLIST_START): data.find(profile_details.__PLIST_END) + len(profile_details.__PLIST_END)]
        pl = plistlib.readPlistFromString(xml)
        for key in details.__slots__:
            if 'DeveloperCertificates' in key:
                details.DeveloperCertificates = []
                for blob in pl.get(key):
                    details.DeveloperCertificates.append(profile_details.get_certificate_details(blob))
            else:
                setattr(details, key, pl.get(key, ''))
        return details

    @staticmethod
    def get_certificate_details(certificate_blob):
        c = OpenSSL.crypto
        cert = OpenSSL.crypto.X509
        cert = c.load_certificate(c.FILETYPE_ASN1, certificate_blob.data)
        ret = dict(cert.get_subject().get_components())
        ret['notAfter'] = datetime.datetime.strptime(cert.get_notAfter(), '%Y%m%d%H%M%SZ')
        return ret

    @property
    def expiration_time(self):
        return self.ExpirationDate.strftime("%X")

    @property
    def expiration_date(self):
        return self.ExpirationDate.strftime("%x")


def parse_provisioning(fn):
    profile = profile_details.readFromFile(fn)
    details = [profile.UUID, profile.expiration_time, profile.expiration_date,
               profile.Name, profile.AppIDName, profile.Entitlements['application-identifier']]
    return details
