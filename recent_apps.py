#!python3
import winreg
from  datetime import datetime as dt
# to convert UTC to local time
from datetime import datetime, timedelta
import json


def parseRecentApps(numberApps,guid):
    access_registry = winreg.ConnectRegistry(None,winreg.HKEY_CURRENT_USER)
    guid="{"+str(guid)+"}"
    #guid should be in this form (between brackets )
    path="Software\\Microsoft\\Windows\\CurrentVersion\\Search\\RecentApps\\" +guid+"\\RecentItems"
    print("path : ",path)

    access_key = winreg.OpenKey(access_registry,"Software\\Microsoft\\Windows\\CurrentVersion\\Search\\RecentApps\\" +guid+"\\RecentItems")
    #accessing the key to open the registry directories under
    if not numberApps:
        numberApps=10000 # max number unreachable
    for i  in range(numberApps):
        try:
          x =winreg.EnumKey(access_key,i)
          #print("x",x)
          subkey=winreg.CreateKey(access_key, x)
          #print("GUID: ",guid)
          print("=======New value ======\n")
          display_name=winreg.EnumValue(subkey,2)[1]
          encryptedPath=winreg.EnumValue(subkey,1)[1]
          utctimestamp=winreg.EnumValue(subkey,3)[1]
          time =datetime(1601, 1, 1) + timedelta(seconds=utctimestamp/10**7)
          print("time ",time )
          dict={"display_name":display_name,"encryptedPath":encryptedPath,"time":str(time)}

          print(json.dumps(dict, indent=2))



        except  :
            pass



if __name__ == '__main__':
    parseRecentApps(None,"809e7f24-072f-4099-9890-7203cfe6916f")
