#!python3
import winreg
# to convert UTC to local time
from datetime import datetime, timedelta
import struct
import re

def listToDict(lstA, lstB):
    zippedLst = zip(lstA, lstB)
    op = dict(zippedLst)
    return op

def parse_MRUListEx(mrulist):
    size = (len(mrulist)) / 4
    struct_arg = "<%sI" % (size)
    print("size",size)
    return struct.unpack(struct_arg, mrulist)
def parse(binaryVal):
    result=""
    for i in range(len(binaryVal)):
        print(binaryVal[i])
def enumValues(key,extension):
    values=[]
    i=0
    while True :
        try :
            value=winreg.EnumValue(key,i)

            binaryvalue=str(value[1])
            binaryvalue=binaryvalue[:binaryvalue.find(extension)] # reverse
            binaryvalue=binaryvalue[::-1]
            #print("======\n")
            #print(binaryvalue)
            binaryvalue=binaryvalue[:binaryvalue.find("00")]
            binaryvalue=binaryvalue[::-1]
            #print("======\n")
            #print(binaryvalue)
            value=[value[0],binaryvalue+extension,value[2]]
            #print(value)


            values.append(value)
            i+=1

        except  :
            pass
            return values

    return [c for c in values if c[1]== "MRUListEx"]

def osmruParser(extension,limit):
    access_registry = winreg.ConnectRegistry(None,winreg.HKEY_CURRENT_USER)
    access_key = winreg.OpenKey(access_registry,r"Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU\\"+extension)
    values=enumValues(access_key,extension)

    if not limit :
        # limit is None
        limit=len(values)
    if limit >len(values):
        print("limit exceeds values !!!!!")
        limit=len(values)
    for i in range(limit):

        print("\nFile {} : {} ".format(i,values[i]))

if __name__ == '__main__':
    osmruParser("pdf",10)
