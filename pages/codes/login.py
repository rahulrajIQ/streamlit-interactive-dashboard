import datetime as dt

from py5paisa import FivePaisaClient

cred={"APP_NAME":"5P56151145",
      "APP_SOURCE":"5285",
      "USER_ID":"PXVUPM1Zrni",
      "PASSWORD":"OGcp3gqB7CN",
      "USER_KEY":"P4WScdWQBRaU5PGlodxNVxcPPeGOwVSX",
      "ENCRYPTION_KEY":"gIWagNeZ7PCsE6r6jokaoN0LHuQOig4k"
    }
def login():
    client = FivePaisaClient(email="raazx2j@gmail.com", passwd="austin#316", dob="19940901", cred = cred)
    client.login()
    return client