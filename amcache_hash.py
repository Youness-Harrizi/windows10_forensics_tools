import os
import re
import shutil
import pandas as pd
import json
try:
    import re
    has_re = True
except ImportError:
    has_re=False
    print ("you need to get re  ")
# this file should be launched as root
def amcacheParser(regex,limit):
    command=r"AmcacheParser.exe -f C:\Windows\appcompat\Programs\Amcache.hve --csv ./tmp  "
    command
    os.system(command) # run only once after that I will delete files
    # fileName=20200601171557_Amcache_UnassociatedFileEntries

    # look for my fileName
    boolean=False
    if regex:
        mod_re = re.compile(regex ,re.I)
        boolean=True
    rootdir = "tmp"
    file_regex = re.compile('.*Unassociated.*')
    counter=0
    for root, dirs, files in os.walk(rootdir):
        for file in files:
            #print("counter",counter)
            if file_regex.match(file):

                df=pd.read_csv(".\\tmp\\"+file)
                #print(df)
                if not limit :
                    limit=10000 # unreachable
                for index, c in df.iterrows():
                    if  counter<limit :
                        appname= c["FullPath"].split("\\")[-1]
                        #print("appname",appname)
                        if not boolean:
                            # no regex present
                            #print("regex not present")
                            dict={"APPID":c["ProgramId"],"Appname":appname,"FullPath":c["FullPath"],"SHA1":c["SHA1"]}
                            print("program {} :{}".format(counter,json.dumps(dict, indent=2)))
                            counter+=1

                        else :
                            if re.findall(mod_re,appname):
                                #print("regex  present")
                                dict={"APPID":c["ProgramId"],"Appname":appname,"FullPath":c["FullPath"],"SHA1":c["SHA1"]}
                                print("dict {} :{}".format(counter,json.dumps(dict, indent=2)))
                                counter+=1
                        #print("\n\n")

                break
        break
    # remove the temp directory
    shutil.rmtree(rootdir)

if __name__ == '__main__':
    regex=".*\.exe"
    amcacheParser(regex,None)
