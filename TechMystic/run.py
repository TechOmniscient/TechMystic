import os,sys,time
from Plugs.Configs.MainConfigs.Functions import *

#Main Menu Pages
#from Plugs.Configs.Pages.Chat_App import *
#from Plugins.Configs.Pages.Updates import *
#from Plugins.Configs.Pages.Learnerships import *

#More Menu Pages
#from Plugins.Configs.Pages.More_Menu_Pages.Org_Rules import *
#from Plugins.Configs.Pages.More_Menu_Pages.About_Us import *
#from Plugins.Configs.Pages.More_Menu_Pages.Students_List import *
#from Plugins.Configs.Pages.More_Menu_Pages.Script_Games import *
#from Plugins.Configs.Pages.More_Menu_Pages.Org_History import *
from Plugs.Configs.Pages.More_Menu_Pages.Chat_Info import *
#from Plugins.Configs.Pages.More_Menu_Pages.BlackDoc_Info import *

#This Script Must Not Be Copyrighted As It Will Make The Org Ban Your Learnership!
#Developed By: TechOmniscient
#Promoted By: TechOmniscient Group

#Owner; I created this script to keep students upto dated offline.
#       Please Use The Classified Information At Your own Risk
#       Our Organization Is Not Responsible For Our Students Misbehaviors
#       No Copyrighting


#All TechOmniscient TechMystic Stored Data -------- IF You May Change Something Here Your Program Wont Work Right.
#Learnership Data Storage
Identity = ""
Location = ""
Password = ""
Learnership = "Student_No_"
Telegram = "T.me/totm_"
Secret = "SNC"
Secret_Chat = "SCSC-"
PM_Active = False

#Main Page Functions
def Password_Error():
    clearConsole()
    NoLoad_Banner()
    print(Bright_Yellow +"Login Security")
    print(Bright_Red + Learnership + Identity + Bright_Green + Login_Main_msg)
    Moretime_Load()
    clearConsole()

def CPassword_Error():
    clearConsole()
    NoLoad_Banner()
    print(Bright_Yellow +"Login Security")
    print(Bright_Red + Learnership + Identity + Bright_Green + CPassword_Error_msg)
    Moretime_Load()
    clearConsole()

def Nickname_Error():
    clearConsole()
    NoLoad_Banner()
    print(Bright_Red + "Empty Input Error;" + Bright_Green + "\n\
Please make sure you enter your Nickname.")
    Moretime_Load()
    clearConsole()

def Nickname_Error2():
    clearConsole()
    NoLoad_Banner2()
    print(Bright_Red + "Empty Input Error;" + Bright_Green + "\n\
Please make sure you enter your Nickname.")
    Moretime_Load()
    clearConsole()

def iD_Error():
    clearConsole()
    NoLoad_Banner()
    print(Bright_Red + "Empty Input Error;" + Bright_Green + "\n\
Please make sure you enter your Org iD.")
    Moretime_Load()
    clearConsole()

def Location_Error():
    clearConsole()
    NoLoad_Banner()
    print(Bright_Red + "Empty Input Error;" + Bright_Green + "\n\
Please make sure you enter your Location.")
    Moretime_Load()
    clearConsole()

def Menu_Error():
    clearConsole()
    NoLoad_Banner()
    print(Bright_Red + "")
    Auto_Text_20 = "Error78; The Selected Menu Is Not Found."
    for char in Auto_Text_20:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.3)

    print("")
    Auto_Text_21 = "Or you have entered invailed Text!"
    for char in Auto_Text_21:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.3)
    print("")    
    print(Bright_Green +"If Menu is Chat, write 'Chat' not 'chat'")
    print("Note: You can use 'Chat' to chat with;")
    print("Mr RekcahDA_Bot!")
    Moretime_Load()

def Options_Error2():
    clearConsole()
    NoLoad_Banner2()
    print(Bright_Red + "")
    Auto_Text_20 = "Error77; The Selected Option Is Not Supported."
    for char in Auto_Text_20:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.3)

    print("")
    Auto_Text_21 = "Or you have entered invailed Text!"
    for char in Auto_Text_21:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.3)
    print("")    
    print(Bright_Green +"If Option is Y, write 'Y' not 'y'")
    Moretime_Load()

def Options_Error3():
    clearConsole()
    NoLoad_Banner2()
    print(Bright_Red + "")
    Auto_Text_20 = "Error77; The Selected Option Is Not Supported."
    for char in Auto_Text_20:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.3)

    print("")
    Auto_Text_21 = "Or you have entered invailed Text!"
    for char in Auto_Text_21:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.3)
    print("")    
    print(Bright_Green +"If Option is T&Cs, write 'T&Cs' not 't&cs'")
    Moretime_Load()

def Firewall_Error():
    clearConsole()
    NoLoad_Banner2()
    print(Bright_Red + "Empty Input Error;" + Bright_Green + "\n\
Please make sure you Answer That Question.\n\
" + Bright_Red + "If you are not a preminum student\n\
Register to get all answers to access\n\
The Locked Version\n\
"+ BG_Bright_Cyan + Bright_Magenta + "")
    Firewall_info = "--------How To Register To CHH.Org-------"
    for char in Firewall_info:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.3)
    print("")
    print(Rest + Bright_Red + "Register With Us Today\n\
To Register you must contact us\n\
At Facebook or Telegram seraching\n\
'TechOmniscient' then inbox us.\n\
We will then register you in CHH Org as a\n\
Preminum Student;" + Bright_Cyan + "\n\
Note; You cant register in this Version!")
    Moretime_Load()
    clearConsole()

def Access_Denied():
    clearConsole()
    NoLoad_Banner2()
    print(Bright_Red + "Wrong Input Error;" + Bright_Green + "\n\
Please make sure you Answer That Question\n\
Right and other Questions as well.\n\
" + Bright_Red + "If you are not a preminum student\n\
Register to get all answers to access\n\
The Locked Version\n\
\n\
" + BG_Bright_Cyan + Bright_Magenta)
    Firewall_info = "--------How To Register To CHH.Org-------"
    for char in Firewall_info:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.3)
    print("")
    print(Rest + Bright_Red + "Register With Us Today\n\
To Register you must contact us\n\
At Facebook or Telegram seraching\n\
'TechOmniscient' then inbox us.\n\
We will then register you in CHH Org as a\n\
Preminum Student;" + Bright_Cyan + "\n\
Note; You cant register in this Version!")
    Moretime_Load()

def Learnership_Details():
    #Logged in User Details
    User_Data = "-----Here is your Learnership Details-----"
    print(BG_Bright_Cyan + Bright_Magenta)
    for char in User_Data:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.3)
    print(Rest +"")
    print(Bright_Red + "User iD: " + Identity)
    print("Learnership: "+ Learnership + Identity)
    print(Bright_Red + "Nickname: " + Nickname)
    print("Location: "+ Location)
    print("Proton Email: " + Learnership + Identity + Bright_Magenta + "@" + Bright_Red + "protonmail.com")
    print("Telegram: "+ Bright_Magenta + "@" + Bright_Red + Telegram + Identity)
    print("Invited By: "+  Bright_Red + Invited_By)
    print("Registered Date: "+  Bright_Red + Registered_Date)
    print(Bright_Red + "Paying Student: " + Paying_Student)
    Security_info = "----------Account Secret Codes-----------"
    print(Rest + BG_Bright_Cyan + Bright_Magenta)
    for char in Security_info:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.2)
    print(Rest + "" + Bright_Red)
    print("Yaaic & Element Password: "+ Identity + Location[1] + Password[0] + Location[3] + Identity[0] + Password[4] + Password[6])
    print("DarkChat Code: "+ Secret_Chat + Identity + "-" + Location[0] + Password[3] + Location[4] + Identity[0] + Password[1] + Password[0])
    print("Unique Code: "+ Secret + Identity + "-" + Location[0] + Password[3] + Location[4] + Identity[0] + Password[1] + Password[0])
    warning = '-> Script Part | Viewed Learnership Details Successfully - Alert'
    logsTMB(warning)

#The Script Loop
def Run():
    while True:
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        clearConsole()
        if LoggedIn <= 1:
            Index_Banner()
            Index_Welcome_msg()
        else:
            NoLoad_Banner()
        Learnership_Details()
        InternetConnection_Status()
        logsTMB('-> Script Part | LoggedIn Successfully - Pass')
        Main_Menu()
        Answer = input(Bright_Cyan +"Select Menu:" + Bright_Red + "\n[+] ->" + Bright_Cyan)
        if Answer == DemonFireWall[0]:
            InternetConnection_Status()
            #Updates Script
            logsTMB('-> Script Part | Updates Page - Pass')
            Updates_Page()
            Home()
            break
        #End Part

        elif Answer == DemonFireWall[1]:
            InternetConnection_Status()
            #VPN Files Script
            logsTMB('-> Script Part | VPN Files Page - Pass')
            VPN_Files()    
            Home()
            break
        #End Part

        elif Answer == DemonFireWall[2]:
            InternetConnection_Status()
            #Yaaic Config Script
            logsTMB('-> Script Part | Yaaic Configs Page - Pass')
            Yaaic_Config()
            break
        #End Part

        elif Answer == DemonFireWall[3]:
            InternetConnection_Status()
            #DarkWeb Links Script
            logsTMB('-> Script Part | Darkweb Links Page - Pass')
            Darkweb_Links()
            Home()
            break
        #End Part

        elif Answer == DemonFireWall[4]:
            InternetConnection_Status()
            #Learnership Script
            logsTMB('-> Script Part | Learnerships Page - Pass')
            Learnerships()
            Home()
            break
        #End Part

        elif Answer == DemonFireWall[5]:
            InternetConnection_Status()
            #Apps Script
            logsTMB('-> Script Part | Updates Page - Pass')
            Apps()
            Home()
            break
        #End Part

        elif Answer == DemonFireWall[6]:
            InternetConnection_Status()
            #Hacking Lessons Script
            logsTMB('-> Script Part | Updates Page - Pass')
            Hacking_Lessons()
            continue
        #End Part

        elif Answer == DemonFireWall[7]:
            InternetConnection_Status()
            #Chatting Script
            logsTMB('-> Script Part | Chat App Page - Pass')
            Chat_App()
            break
        #End Part    
        
        elif Answer == DemonFireWall[8]:
            InternetConnection_Status()
            #More Menu
            clearConsole() 
            #Banner
            NoLoad_Banner()
            InternetConnection_Status()
            #Index Texts In Animated Format
            print(Bright_Green)
            for char in Header:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            print("")
            for char in Main_msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            print("")
            for char in Main_msg2:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            print("")
            #Logged in User Details
            Learnership_Details()
            More_Menu()
            More_MenuQ = input(Bright_Cyan +"Select Menu:" + Bright_Red + "\n[+] ->" + Bright_Cyan)
            if More_MenuQ == DemonFireWall[9]:
                InternetConnection_Status()
                #MyAccount Page
                clearConsole()
                NoLoad_Banner()
                logsTMB('-> Script Part | Updates Page - Pass')
                Learnership_Details()
                Home()
                break
                #End Part..................................................
            
            elif More_MenuQ == DemonFireWall[10]:
                InternetConnection_Status()
                #Organization Rules
                clearConsole()
                NoLoad_Banner()
                logsTMB('-> Script Part | Updates Page - Pass')
                Org_Rules()
                Home()
                break

                #End Line Of Rules..............................................................        
            elif More_MenuQ == DemonFireWall[11]:
                InternetConnection_Status()
                #About The Org
                clearConsole()
                NoLoad_Banner()
                logsTMB('-> Script Part | Updates Page - Pass')
                About_Us()
                Home()
                break

            elif More_MenuQ == DemonFireWall[12]:
                InternetConnection_Status()
                #Students List Page
                clearConsole()
                NoLoad_Banner()
                logsTMB('-> Script Part | Updates Page - Pass')
                Students_List()
                Home()
                break

            elif More_MenuQ == DemonFireWall[13]:
                InternetConnection_Status()
                #Script Games Page
                clearConsole()
                NoLoad_Banner()
                logsTMB('-> Script Part | Updates Page - Pass')
                Script_Games()
                Home()
                break
            
            elif More_MenuQ == DemonFireWall[14]:
                InternetConnection_Status()
                #Script Games Page
                clearConsole()
                NoLoad_Banner()
                logsTMB('-> Script Part | Updates Page - Pass')
                Org_History()
                Home()
                break

            elif More_MenuQ == DemonFireWall[15]:
                InternetConnection_Status()
                #Script Games Page
                clearConsole()
                NoLoad_Banner()
                logsTMB('-> Script Part | Updates Page - Pass')
                Chat_Info()
                Home()
                break

            elif More_MenuQ == DemonFireWall[16]:
                InternetConnection_Status()
                #Script Games Page
                clearConsole()
                NoLoad_Banner()
                logsTMB('-> Script Part | Org Info Page - Pass')
                Home()
                break
            else:
                InternetConnection_Status()
                logsTMB('-> Menu Field - Error')
                Menu_Error()
                continue
        else:
            InternetConnection_Status()
            logsTMB('-> Menu Field - Error')
            Menu_Error()
            continue

def Home():
    Home = input(BG_Bright_Red + Bright_Green + "Do you wanna go back? <(Y/N)>" + Rest + Bright_Red + '\n[+] ->' + Bright_Green)
    if Home == "N":
        InternetConnection_Status()
        Logout_System()
    elif Home == "Y":
        InternetConnection_Status()
        Run()
    else:
        InternetConnection_Status()
        logsTMB('-> Script Part | Answering Field [Home Option] - Error')
        Options_Error2()

def Firewall_CodeBase_Scanner():
    while True:
        global PM_Active
        if Nickname != Firewall_CodeBase[0]:
            if Nickname != Firewall_CodeBase[1]:
                if Nickname != Firewall_CodeBase[2]:
                    if Nickname != Firewall_CodeBase[3]:
                        if Nickname != Firewall_CodeBase[4]:
                            if Nickname != Firewall_CodeBase[5]:
                                if Nickname != Firewall_CodeBase[6]:
                                    if Nickname != Firewall_CodeBase[7]:
                                        if Nickname != Firewall_CodeBase[8]:
                                            if Nickname != Firewall_CodeBase[9]:
                                                if Nickname != Firewall_CodeBase[10]:
                                                    if Nickname != Firewall_CodeBase[11]:
                                                        if Nickname != Firewall_CodeBase[12]:
                                                            if Nickname != Firewall_CodeBase[13]:
                                                                if Nickname != Firewall_CodeBase[14]:
                                                                    InternetConnection_Status()
                                                                    logsTMB('-> User Recognization - Error')
                                                                    Broken_User()
                                                                    break

                                                                else:
                                                                    InternetConnection_Status()
                                                                    PM_Active = True
                                                                    warning = '-> Script Part | Scanned For User Successfully - Alert'
                                                                    logsTMB(warning)
                                                                    Run()
                                                            else:
                                                                InternetConnection_Status()
                                                                PM_Active = True
                                                                warning = '-> Script Part | Scanned For User Successfully - Alert'
                                                                logsTMB(warning)
                                                                Run()
                                                        else:
                                                            InternetConnection_Status()
                                                            PM_Active = True
                                                            warning = '-> Script Part | Scanned For User Successfully - Alert'
                                                            logsTMB(warning)
                                                            Run()
                                                    else:
                                                        InternetConnection_Status()
                                                        PM_Active = True
                                                        warning = '-> Script Part | Scanned For User Successfully - Alert'
                                                        logsTMB(warning)
                                                        Run()
                                                else:
                                                    InternetConnection_Status()
                                                    PM_Active = True
                                                    warning = '-> Script Part | Scanned For User Successfully - Alert'
                                                    logsTMB(warning)
                                                    Run()
                                            else:
                                                InternetConnection_Status()
                                                PM_Active = True
                                                warning = '-> Script Part | Scanned For User Successfully - Alert'
                                                logsTMB(warning)
                                                Run()
                                        else:
                                            InternetConnection_Status()
                                            PM_Active = True
                                            warning = '-> Script Part | Scanned For User Successfully - Alert'
                                            logsTMB(warning)
                                            Run() 
                                    else:
                                        InternetConnection_Status()
                                        PM_Active = True
                                        warning = '-> Script Part | Scanned For User Successfully - Alert'
                                        logsTMB(warning)
                                        Run() 
                                else:
                                    InternetConnection_Status()
                                    PM_Active = True
                                    warning = '-> Script Part | Scanned For User Successfully - Alert'
                                    logsTMB(warning)
                                    Run() 
                            else:
                                InternetConnection_Status()
                                PM_Active = True
                                warning = '-> Script Part | Scanned For User Successfully - Alert'
                                logsTMB(warning)
                                Run() 
                        else:
                            InternetConnection_Status()
                            PM_Active = True
                            warning = '-> Script Part | Scanned For User Successfully - Alert'
                            logsTMB(warning)
                            Run() 
                    else:
                        InternetConnection_Status()
                        PM_Active = True
                        warning = '-> Script Part | Scanned For User Successfully - Alert'
                        logsTMB(warning)
                        Run() 
                else:
                    InternetConnection_Status()
                    PM_Active = True
                    warning = '-> Script Part | Scanned For User Successfully - Alert'
                    logsTMB(warning)
                    Run()
            else:
                InternetConnection_Status()
                PM_Active = True
                warning = '-> Script Part | Scanned For User Successfully - Alert'
                logsTMB(warning)
                Run() 
        else:
            InternetConnection_Status()
            PM_Active = True
            warning = '-> Script Part | Scanned For User Successfully - Alert'
            logsTMB(warning)
            Run()

def Login_Detector():
    while True:
        global Identity
        global Location 
        global Password 
        global Learnership 
        global Telegram 
        global Secret 
        global Secret_Chat   

        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        clearConsole()
        #Banner
        AutoLoc = checkTMB('User', 'Location')
        if AutoLoc == False:
            NoLoad_Banner2()
            #Login System & Instructions
            Login_System()

        if checkTMB("User", "iD") == False:
            Identity = input(Bright_Cyan +"iD: ")
            sendTMB("User", "iD", Identity)
        else:
            Identity = recvTMB("User", "iD")
        if len(Identity) > 0:
            warning = '-> Script Part | Identity - Pass'
            logsTMB(warning)
            if checkTMB("User", "Password") == False:
                Password = input("Password: ")
                sendTMB("User", "Password", Password)
            else:
                Password = recvTMB("User", "Password")
            if len(Password) >= 8:
                InternetConnection_Status()
                warning = '-> Script Part | Password - Pass'
                logsTMB(warning)
                if checkTMB("User", "Cpassword") == False:  
                    Cpassword = input("Confirm Password: ")
                    sendTMB("User", "Cpassword", Cpassword)
                else:
                    Cpassword = recvTMB("User", "Cpassword")
                if len(Cpassword) >= 8:
                    InternetConnection_Status()
                    warning = '-> Script Part | Confirm Password - Pass'
                    logsTMB(warning)
                    if Password == Cpassword:
                        warning = '-> Script Part | Passwords Match - Pass'
                        logsTMB(warning)
                        if checkTMB("User", "Location") == False:
                            Location = input("Location: ")
                            sendTMB("User", "Location", Location)
                        else:
                            Location = recvTMB("User", "Location")
                        if len(Location) > 1:
                            InternetConnection_Status()
                            warning = '-> Script Part | Location - Pass'
                            logsTMB(warning)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            print(Dark_Blue + BG_Dark_Green + Line + Rest)
                            Firewall_CodeBase_Scanner()
                        else:
                            InternetConnection_Status()
                            logsTMB('-> Location - Error')
                            Location_Error()
                            continue
                    else:
                        InternetConnection_Status()
                        logsTMB('-> Confirmed Password1 - Error')
                        CPassword_Error()
                        continue
                        #The End Of The Script!
                else:
                    InternetConnection_Status()
                    logsTMB('-> Confirmed Password2 - Error')
                    CPassword_Error()
                    continue
            else:
                InternetConnection_Status()
                logsTMB('-> Password - Error')
                Password_Error()
                continue
        else:
            InternetConnection_Status()
            logsTMB('-> User iD - Error')
            iD_Error()
            continue                                   

#Screen
try:
    while True:
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        clearConsole()
        if LoggedIn <= 1:
            Login_Banner()
        else:
            NoLoad_Banner2()
        Scanned_TnCsAgreed_File = TnCsAgree_File()
        if os.path.exists(Scanned_TnCsAgreed_File):
            Scanned_TnCsAgreed = TnCsAgreed_Scan()
            if Scanned_TnCsAgreed == 'Y':
                warning = '-> Script Part | Auto Scanned T&Cs Agreed - Pass'
                logsTMB(warning)
                pass
            else:
                logsTMB('-> Scanning TnCsAgreed File - Error')
                print(Bright_Red + 'Please Note; TechMystic Cant Handle TnCs\n In This Machine, To Fix This...\n Please Delete This Script And Reinstall It\n Or Contact Us At policies@techmystic.co.za\n\n Thank You Bye, Till We Meet Again!')
                quit()
        else:
            Scanned_TnCsViewed_File = TnCsViewed_File()
            if os.path.exists(Scanned_TnCsViewed_File):
                Scanned_TnCsViewed = TnCsViewed_Scan()
                if Scanned_TnCsViewed == 'Y':
                    warning = '-> Script Part | Auto Scanned T&Cs Viewed - Pass'
                    logsTMB(warning)
                    Index_Welcome_msg2()
                    TnCs_QnAs = input(Bright_Red + "Do You Agree To Our T&Cs? <(Y/N)>\n[+] ->" + Bright_Green)
                    if TnCs_QnAs == Binary_Firewall[0]:
                        InternetConnection_Status()
                        print("")
                        print(Bright_Red + "Please Note;\n\
You Are Not Allowed To Proceed\n\
With Lessons Of TechMystic PTS Academy\n\
So Please We Advice You To Delete This\n\
With The Immediate Effect As You Have\n\
Chosen To Not Agree With TechMystic PTS\n\
Privacy, Policies, Terms And Conditions.\n\n\
Good Bye It Was Nice Meeting You")
                        warning = '-> Script Part | Munual T&Cs Disagreed - Warning'
                        logsTMB(warning)
                        break
                    elif TnCs_QnAs == "Y":
                        InternetConnection_Status()
                        TnCsAgreed()
                        Index_Welcome_msg3()
                    else:
                        InternetConnection_Status()
                        logsTMB('-> Script Part | Answering Field [T&Cs Q&As] - Error')
                        Options_Error2() 
                else:
                    InternetConnection_Status()
                    logsTMB('-> Scanning TnCsViewed File - Error')
                    print(Bright_Red + 'Please Note; TechMystic Cant Handle TnCs\n In This Machine, To Fix This...\n Please Delete This Script And Reinstall It\n Or Contact Us At policies@techmystic.co.za\n\n Thank You Bye, Till We Meet Again!')
                    quit()
            else:
                InternetConnection_Status()
                Index_Welcome_msg2()
                TnCs_QnAs = input(Bright_Cyan + "\nPlease Make Sure You Type: "+ Bright_Red + "<(T&Cs)>"+ Bright_Cyan +"\nTo Read Our T&Cs On Our Website Before \nUsing, Agreeing Or Disagreeing With T&Cs!\n" + Bright_Red+ "[+] ->" + Bright_Green)
                if TnCs_QnAs == "T&Cs":
                    InternetConnection_Status()
                    TnCsViewed()
                    urlRedirect("https://techmystic.co.za/policies.php")
                    continue
                else:
                    InternetConnection_Status()
                    logsTMB('-> Script Part | Answering Field [T&Cs] - Error')
                    Options_Error3()



        Scanned_TnCsAgreed_File = TnCsAgree_File()
        if os.path.exists(Scanned_TnCsAgreed_File):
            Scanned_TnCsAgreed = TnCsAgreed_Scan()
            if Scanned_TnCsAgreed == 'Y':
                if checkTMB("User", "Registered_Student") == False:
                    Answer = input(Bright_Red + "Are you registered? <(Y/N)>\n[+] ->" + Bright_Green)
                    sendTMB("User", "Registered_Student", Answer)
                else:
                    Answer = recvTMB('User', "Registered_Student")
                if Answer == Binary_Firewall[0]:
                    warning = '-> Script Part | Registered Student - Pass'
                    logsTMB(warning)
                    if checkTMB("User", "Nickname") == False:
                        print(Bright_Cyan + "Please Note; Your Nickname Will Be Used\nAcross The Platform To Address You.")
                        Nickname = input(Bright_Cyan + "Nickname: " + Bright_Green)
                        sendTMB("User", "Nickname", Nickname)
                    else:
                        Nickname = recvTMB("User", "Nickname")
                    if len(Nickname) >= 1:
                        print(Bright_Cyan + Nickname + Bright_Red + " Please Contact Us;\n\
https://facebook.com/chhorg or try\n\
At Https://t.me/cryptichatshackers Now\n\
Know Register and get the Organization\n\
Password...\n\n\
You Can't Register here in this version!")
                        Logout_System2()
                        break
                    else:
                        logsTMB('-> Nickname Field Validation - Error')
                        Nickname_Error2()
                        continue
                elif Answer == Binary_Firewall[1]:
                    if LoggedIn <= 1:
                        if checkTMB('Firewall', 'Paying_Student') == False:
                            Learnership_Scanner = "If you are a student of the TechMystic PS\n\
Please Enter Firewall Security Details;"
                            print(Bright_Magenta)
                            for char in Learnership_Scanner:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.1)
                            print("")
                        else:
                            Learnership_Scanned = "You Will Shortly Login Automatically\n\
Please Wait Few More Seconds..."
                            print(Bright_Magenta)
                            for char in Learnership_Scanned:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.1)
                            print("")
                    if checkTMB("User", "Nickname") == False:
                        print(Bright_Magenta + "\nPlease Note; Your Nickname Will Be Used\nAcross The Platform To Address You.")
                        Nickname = input(Bright_Cyan + "Nickname: " + Bright_Green)
                        sendTMB("User", "Nickname", Nickname)
                    else:
                        Nickname = recvTMB("User", "Nickname")
                    if len(Nickname) >= 1:
                        warning = '-> Script Part | Student Nickname - Pass'
                        logsTMB(warning)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        clearConsole()
                        Firewall_Banner()
                        InternetConnection_Status()
                        print(Bright_Red + "Thank You " + Nickname + "\n\
For Coming To Study With Us!\n\n\
" + Bright_Green + "Please Pass Throgh To Login!")
                        print(Bright_Yellow + "Security Tasks;\n\
"+ Bright_Magenta + Ls1 + Bright_Red + "). When Did The TechMystic PTS Start?\n\
"+ Bright_Magenta + Ls2 + Bright_Red + "). Who Founded TechMystic PTS Academy?\n\
"+ Bright_Magenta + Ls3 + Bright_Red + "). What Is The Name of TechMystic PTS\n\
Mother Comapny Of TechMystic?\n\
"+ Bright_Magenta + Ls4 + Bright_Red + "). What is the TechMystic PTS\n\
Secret Password for Preminum Learners?\n\
"+ Bright_Magenta + Ls5 + Bright_Red + "). Who Invited You?\n\
"+ Bright_Magenta + Ls6 + Bright_Red + "). Which Year Did you Register?\n\
"+ Bright_Magenta + Ls7 + Bright_Red + "). Are You In The Paying Leaners List?\n")
                        if checkTMB("Firewall", "Date") == False:
                            Login = input(Bright_Cyan + Ls1 + "). " + Rest  + "Q1 Answer;\n\
" + Bright_Red)
                            sendTMB("Firewall", "Date", Login)
                        else:
                            Login = recvTMB("Firewall", "Date")
                        if len(Login) <=5:
                            logsTMB('-> Login Date Field | Was Not Over 5 Chars - Error')
                            Firewall_Error()
                            Logout_System()
                            break
                        else:
                            if Login != Firewall[0]:
                                InternetConnection_Status()
                                logsTMB('-> Login Field | Wrong Date So (Access Denied) - Error')
                                Access_Denied()
                                Logout_System()
                                break
                            else:
                                if checkTMB("Firewall", "Founder") == False:
                                    Login = input(Bright_Cyan + Ls2 + "). " + Rest + "Q2 Answer;\n\
" + Bright_Red)
                                    sendTMB("Firewall", "Founder", Login)
                                else:
                                    Login = recvTMB("Firewall", "Founder")
                                if len(Login) <=5:
                                    InternetConnection_Status()
                                    logsTMB('-> Login Founder Field | Was Not Over 5 Chars - Error')
                                    Firewall_Error()
                                    Logout_System()
                                    break
                                else:
                                    if Login != Firewall[1]:
                                        InternetConnection_Status()
                                        logsTMB('-> Login Field | Wrong Founder So (Access Denied) - Error')
                                        Access_Denied()
                                        Logout_System()
                                        break
                                    else:
                                        if checkTMB("Firewall", "Company") == False:
                                            Login = input(Bright_Cyan + Ls3 + "). " + Rest + "Q3 Answer;\n\
" + Bright_Red)
                                            sendTMB("Firewall", "Company", Login)
                                        else:
                                            Login = recvTMB("Firewall", "Company")
                                        if len(Login) <=5:
                                            InternetConnection_Status()
                                            logsTMB('-> Login Company Field | Was Not Over 5 Chars - Error')
                                            Firewall_Error()
                                            Logout_System()
                                            break
                                        else:
                                            if Login != Firewall[2]:
                                                InternetConnection_Status()
                                                logsTMB('-> Login Field | Wrong Company So (Access Denied) - Error')
                                                Access_Denied()
                                                Logout_System()
                                                break
                                            else:
                                                if checkTMB("Firewall", "Password") == False:
                                                    Login = input(Bright_Cyan + Ls4 + "). " + Rest + "Q4 Answer;\n\
" + Bright_Red)
                                                    sendTMB("Firewall", "Password", Login)
                                                else:
                                                    Login = recvTMB("Firewall", "Password")
                                                if len(Login) <=5:
                                                    InternetConnection_Status()
                                                    logsTMB('-> Login Password Field | Was Not Over 5 Chars - Error')
                                                    Firewall_Error()
                                                    Logout_System()
                                                    break
                                                else:
                                                    if Login != Firewall[3]:
                                                        InternetConnection_Status()
                                                        logsTMB('-> Login Field | Wrong Password So (Access Denied) - Error')
                                                        Access_Denied()
                                                        Logout_System()
                                                        break
                                                    else:
                                                        if checkTMB("Firewall", "Invitation") == False:
                                                            Invited_By = input(Bright_Cyan + Ls5 + "). " + Rest +  "Q5 Answer;\n\
" + Bright_Cyan + "-> " + Bright_Red)
                                                            sendTMB("Firewall", "Invitation", Invited_By)
                                                        else:
                                                            Invited_By = recvTMB("Firewall", "Invitation")
                                                        if len(Invited_By) <=1:
                                                            InternetConnection_Status()
                                                            logsTMB('-> Login Invitation Field | Was Not Over 1 Chars - Error')
                                                            Firewall_Error()
                                                            Logout_System()
                                                            break
                                                        else:
                                                            if checkTMB("Firewall", "Registered_Year") == False:
                                                                Registered_Date = input(Bright_Cyan + Ls6 + "). " + Rest +  "Q6 Answer;\n\
" + Bright_Cyan + "-> " + Bright_Red)
                                                                sendTMB("Firewall", "Registered_Year", Registered_Date)
                                                            else:
                                                                Registered_Date = recvTMB("Firewall", "Registered_Year")
                                                            if len(Registered_Date) <=3:
                                                                InternetConnection_Status()
                                                                logsTMB('-> Login RegDate Field | Was Not Over 3 Chars - Error')
                                                                Firewall_Error()
                                                                Logout_System()
                                                                break
                                                            else:
                                                                if checkTMB("Firewall", "Paying_Student") == False:
                                                                    Paying_Student = input(Bright_Cyan + Ls7 + "). " + Rest + "Q7 Answer; <(Y/N)>\n\
" + Bright_Cyan + "-> " + Bright_Red)
                                                                    sendTMB("Firewall", "Paying_Student", Paying_Student)
                                                                else:
                                                                    Paying_Student = recvTMB("Firewall", "Paying_Student")
                                                                if len(Paying_Student) <=0:
                                                                    InternetConnection_Status()
                                                                    logsTMB('-> Login Paying_Student Field | Was Empty - Error')
                                                                    Firewall_Error()
                                                                    Logout_System()
                                                                    break
                                                                else:
                                                                    if Paying_Student == "Y":
                                                                        InternetConnection_Status()
                                                                        Paying_Student = "Yes"
                                                                        Login_Detector()
                                                                    elif Paying_Student == "N":
                                                                        InternetConnection_Status()
                                                                        Paying_Student = "No"
                                                                        Login_Detector()
                                                                    else:
                                                                        InternetConnection_Status()
                                                                    logsTMB('-> Script Part | Answering Field [Paying Student] - Error')
                                                                    Options_Error2()
                                                                    break
                                                                                                                    
                    else:
                        InternetConnection_Status()
                        logsTMB('-> Nickname Field - Error')
                        Nickname_Error2()
                        continue
                else:
                    InternetConnection_Status()
                    logsTMB('-> Script Part | Answering Field [Registered Student] - Error')
                    Options_Error2()
                    continue
            else:
                clearConsole()
                NoLoad_Banner2()
                print(Bright_Red + "Warning: You Can't Access TechMystic\nWithout Agreeing To TechMystic T&Cs\n\nSo Please Review Our T&CS.")
except KeyboardInterrupt:
    delSessions()

finally:
    logsTMB('-> Script Part | Cleared Previous Session Logs Successfully - Alert')
    clearConsole()
    NoLoad_Banner2()
    if Check_InternetConnection() == True:
        print(Bright_Red + f"\nThank You For Learning At TechMystic PTS\nAcademy, Learning iT Lessons Never Truely\nGot This Easy And Fun With A Terminal...\n\nWe Hope To See You Soon And Complete Your\nCareer With TechMystic PTS Academy!")
    else:
        Lost_InternetConnection()
    logsTMB('-> Scritp Part | Logged Out Successfully - Alert')

