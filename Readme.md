# description:
* this project aims at finding new artifacts of execution and artifacts of executables present in a Windows 10 system.

# commands :
*  python .\finalScript.py -f <extension> --limit <limit, default=None>
  * give last files opened for a specific extension
  * example :
    * python .\finalScript.py -f pdf --limit 10
*   python .\finalScript.py --limit <limit> -run
  * Dumping executables run from The run command
  * example :
    * python .\finalScript.py --limit 4 -run
*   python .\finalScript.py -rec <guid> --limit 10
  * extract recent apps launched from a guid (that has a  form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx )  
  * To create a new guid : https://docs.microsoft.com/en-us/dotnet/api/system.guid.newguid?view=netcore-3.1
  * example :
    *  python .\finalScript.py -rec 974433A7-AACB-4BF8-87F6-26CA23F64435 --limit 10
*  python .\finalScript.py -gui --limit <limit>
  * dump latest GUI executables for all GUIDS
*  python .\finalScript.py --hash <regex> --limit <limit>  
  * dump the hash of   executables according to a regex
  * *important* : you should be root for this
  * note : this snippet use a builtin tool to parse AMCACHE hive
  * example :
    * python .\finalScript.py --hash .\*exe --limit 10  

*  python .\finalScript.py --powershell --limit <limit>
  * print last commands issued from powershell

# addition notes :
* provide -h for help
# Prerequites :
* python3 modules :
  * argparse; os;re ; shutil;pandas;json
