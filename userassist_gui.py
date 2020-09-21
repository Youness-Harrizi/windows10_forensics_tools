# On a Windows System, every GUI-based programs launched from the desktop are tracked in this registry key:
import winreg
from  datetime import datetime as dt
import codecs
from datetime import datetime, timedelta




def userAssistParser(limit):
    access_registry = winreg.ConnectRegistry(None,winreg.HKEY_CURRENT_USER)
    path=r"Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist"
    paths=[]
    listA=["Focus Count","Time Focused","Last updated","Name:REG_Binary" ]

    access_key = winreg.OpenKey(access_registry,path)
    for i in range(10) : # 100 is just a number that can't be reached
        try:
            guid=winreg.EnumKey(access_key,i)
            #print(guid)
            temp=path+"\\" +str(guid)+"\Count"

            #paths.append(temp)
            #print("============")
            subkey=winreg.OpenKey(access_registry,temp)
            # now print the value name  :
            # querry info about the key
            info=winreg.QueryInfoKey(subkey)
            # (number of subkeys, number of values , last second)

            num_values=info[1]

            if num_values >1 :
                print("========= NEW GUID",i)
                print('metadata:\n')
                time =datetime(1601, 1, 1) + timedelta(seconds=info[2]/10**7)
                print("\nThe key was last updated",time)
                print("Total number of values for this GUID ",num_values)
                print("GUID ",guid)

                if limit > num_values:

                    limit=num_values
                    print("limit",limit)
                for j in range(num_values-limit,num_values):
                    keyname=winreg.EnumValue(subkey,j)[0]
                    #print("=====START\n\n")
                    if keyname:
                        print("\nGUI executable : "+str(j),codecs.encode(keyname, 'rot_13'))

                    #print(winreg.EnumValue(subkey,j)[2:])
                    #print("======END\n\n")
                print("\n\n")


        except   :
            pass





def enumvalues(key):
    i=0
    values=[]
    while True :
        try :
            values.append(winreg.EnumValue(key,i))
            i+=1


        except :
            pass
    return values


if __name__ == '__main__':
    userAssistParser(10)
