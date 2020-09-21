import argparse
import recent_apps as recentApps
import userassist_gui as userassist
import run_executables as runEx
import openSavedMRU as mru
import amcache_hash as amcache
import powershell_cmds as cmd

parser = argparse.ArgumentParser()
# add  argument
parser.add_argument('-gui',"--guiOnly" , action="store_true",dest='gui', help="dump GUI executable")
parser.add_argument("--limit" , action="store",dest='limit', type=int,default=None)
parser.add_argument('-rec',"--recentGuid", action="store", dest="guid",help="extract recent apps launched from a guid folder that has a  form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx \n  To create a new one refer to documentation  ")
# not sure if guid is user's guid or folder guid https://docs.microsoft.com/en-us/windows/win32/shell/knownfolderid?redirectedfrom=MSDN
parser.add_argument('-run',action='store_true', help="extract executables from run command")
parser.add_argument("-f","--file",action="store",type=str,dest="extension",help="give last files opened for a specific extension")
parser.add_argument("--hash",action="store",dest="hash",type=str,help="give SHA1 hash of files ")

parser.add_argument("--powershell" , action="store_true",dest='power',help="print last commands ",default=None)

results = parser.parse_args()
if results.run:
    # EXPREIENCED OK !!!!!!
    print("start RUN")
    print("Dumping executables run from The run command : \n")
    runEx.runMruParser(results.limit)
    print("end")
elif results.guid :
    # EXPREIENCED OK !!!!!!
    print("START RECENT")
    print("Dump recent app launched based on a GUID \n")
    recentApps.parseRecentApps(results.limit,results.guid)
elif results.gui:
    # EXPREIENCED OK !!!!!!
    print("START GUI")
    print("DUMP GUI APPS \n")
    userassist.userAssistParser(results.limit)
elif results.extension:
        # EXPREIENCED OK !!!!!!
    print("START extension")
    mru.osmruParser(results.extension,results.limit)


elif results.hash:
    # EXPREIENCED OK !!!!!!
    print("DUMPING SHA1 hash of files from amcache hive ")
    print("You should be root for this ")
    amcache.amcacheParser(results.hash,results.limit)
    # result.hash is a regex


elif results.power!=None:
    print("Dump Command line arguments")
    cmd.main(results.limit)
