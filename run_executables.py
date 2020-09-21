#!python3
import winreg
# to convert UTC to local time
from datetime import datetime, timedelta
# convert a list to dict
from utils import listToDict


def enumValues(key):
    values=[]
    i=0
    while True :
        try :
            # filter values :
            value=winreg.EnumValue(key,i)

            if value[0]=="MRUList":
                i+=1
                continue
            #value[1]= # remove last 2 elements

            values.append([value[0],value[1][:-2],value[2]])
            i+=1


        except  :
            pass
            return values
    return values
def runMruParser(limit):
    # limit is the limit number of shown executables
    counter=0
    list=["Name in Registry","Command","Count"]
    access_registry = winreg.ConnectRegistry(None,winreg.HKEY_CURRENT_USER)

    access_key = winreg.OpenKey(access_registry,r"Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU")
    #accessing the key to open the registry directories under
    values=enumValues(access_key)[::-1]
    dict=listToDict(list,values)
    # sort based on the MRU LIST :HGFEDCBA ALWAYS ???????
    # filter the executables to be done
    for i in range(len(values)):
        if counter < limit:
            print("executable {} : {} ".format(i,listToDict(list,values[i])))
            counter+=1


if __name__ == '__main__':
    runMruParser(5)
