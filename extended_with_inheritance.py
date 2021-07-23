from iiifprezi3 import *
global BASEURL
BASEURL = 'http'

class Manifest(Manifest):

    def set_id(self,id=None,extend_baseurl=None):
        if extend_baseurl:
            if id:
                raise ValueError(
                    "Set id using extendbase_url or id not both.")
            else:
                self.id = "/".join((BASEURL,extend_baseurl))
        else:
            if id is None:
                raise ValueError(
                    "Use id or extend_baseurl for setting id.")
            else:
                self.id = id
    