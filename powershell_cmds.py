# C:\Users\younes\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline
import os
import subprocess



def main(limit):
    #print(os.environ['USERPROFILE'])
    print("Start with Powershell =====\n")
    path=os.environ['USERPROFILE']+ "\\AppData\\Roaming\\Microsoft\\Windows\\PowerShell\\PSReadline\\ConsoleHost_history.txt"

    print("path : ",path)
    with open(path,"r") as f:
        lines=f.readlines()[::-1]
        for i  in range(limit) :
            print(lines[i])
    #print("Command Prompt ======\n")
    #os.system("doskey /history")



if __name__ == '__main__':
    main(10)
