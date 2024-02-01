import os, time, sys, webbrowser, subprocess, socket, platform, uuid, requests, json, shutil, threading
#Banner Stored DATA 
# MainBanner Data
B1 = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
B2 = "-----------------------------------------"
B3 = "---    TechOmniscient Organization    ---"
B4 = "---          TechMystic V0.0.1        ---"
B5 = "---   Script Security Level: 1.0.01   ---"
B6 = "-----------------------------------------"
B7 = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
Banner_msg = " Follow Us At 'GitHub' To Stay Upto Date"
Line = "*****************************************"
Endl = "    100% TechMystic Is Done Loading      "
Status_On = "Preminum Student"
Status_Off = "Unrecognized Student"

#SubBanner Data
FWB1 = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
FWB2 = "-----------------------------------------"
FWB3 = "---    TechOmniscient Organization    ---"
FWB4 = "---          TechMystic V0.0.1        ---"
FWB5 = "---   Script Security Level: 1.0.01   ---"
FWB6 = "-----------------------------------------"
FWB7 = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"     
FWBanner_msg = "Use Learner Approval Code To Gain Access"
FWLine = "*****************************************"
FWEndl = "    100% TechMystic Is Done Loading      "

#Colors Codes With Their Given Names
#Bright Text Colors
Dark_Black = "\u001b[30;1m"
Dark_Red = "\u001b[31;1m"
Dark_Green = "\u001b[32;1m"
Dark_Yellow = "\u001b[33;1m"
Dark_Blue = "\u001b[34;1m"
Dark_Magenta = "\u001b[35;1m"
Dark_Cyan = "\u001b[36;1m"
Dark_White = "\u001b[37;1m"

#Dark Text Colors 
Bright_Black = "\u001b[30m"
Bright_Red = "\u001b[31m"
Bright_Green = "\u001b[32m"
Bright_Yellow = "\u001b[33m"
Bright_Blue = "\u001b[34m"
Bright_Magenta = "\u001b[35m"
Bright_Cyan = "\u001b[36m"
Bright_White = "\u001b[37m"

#Bright Background Colors 
BG_Dark_Black = "\u001b[40;1m"
BG_Dark_Red = "\u001b[41;1m"
BG_Dark_Green = "\u001b[42;1m"
BG_Dark_Yellow = "\u001b[43;1m"
BG_Dark_Blue = "\u001b[44;1m"
BG_Dark_Magenta = "\u001b[45;1m"
BG_Dark_Cyan = "\u001b[46;1m"
BG_Dark_White = "\u001b[47;1m"

#Dark Background Colors 
BG_Bright_Black = "\u001b[40m"
BG_Bright_Red = "\u001b[41m"
BG_Bright_Green ="\u001b[42m"
BG_Bright_Yellow = "\u001b[43m"
BG_Bright_Blue = "\u001b[44m"
BG_Bright_Magenta = "\u001b[45m"
BG_Bright_Cyan = "\u001b[46m"
BG_Bright_White = "\u001b[47m"

#Rest Color
Rest = "\u001b[0m"

#Stored DATA 
#Connection Points
Host = "localhost"
Port = 80
Firewall_Based = [
'-> First',
'-> DarkDoor',
'-> 2021',
'-> First Local Darkweb Social Media',
'-> Tor Browser',
] 
DemonFireWall = [
'Updates',
'VPN Files',
'Yaaic Config',
'Darkweb Links',
'Learnerships',
'Apps',
'Hacking Lessons',
'Chat',
'More',
'MyAccount',
'Org Rules',
'About Us',
'Members List',
'Script Games',
'Org History',
'Chat Info',
'BlackDoc Info',
]
Binary_Firewall = [
'N',
'Y',
]
CD_OS = [
'L',
'W',
]
Numbering_Firewall = [
'0',
'1',
'2',
'3',
'4',
'5',
'6',
'7',
'8',
'9',
'10',
]
Firewall_CodeBase = [
'Divine INFINITY',
'PJmax',
'Deoderant Dee',
'GoldenThugRSS',
'RekcahHC_III',
'Spider Anongreyhat',
'RekcahHC_VII',
'Whitedevil',
'RekcahHC_IX',
'RekcahHC_X',
'RekcahHC_XI',
'Wizard',
'Krypto Hacker',
'Krypto Hackt',
'Demonichacker',
]
#MainFunctions --A
def clearConsole():
    Refresh = 'clear'   
    if os.name in ('nt', 'dos'): 
        #If Machine is running on Windows, it will use cls
        Refresh = 'cls'
    os.system(Refresh)
    warning = '-> Script Part | Cleared Screen Successfully - Alert'
    logsTMB(warning)

def Login_Banner():
    print(Bright_Red + "Note; Wait For 50sec, It Will Finish Soon"+ Bright_Yellow)
    for char in B1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    for char in B2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    for char in B3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    for char in B4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    for char in B5:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    for char in B6:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    for char in B7:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print(Bright_Cyan + "")
    for char in Banner_msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Dark_Blue + BG_Dark_Green + "")
    for char in Line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.500)

    print(Rest + Bright_Green + BG_Dark_Blue)
    for char in Endl:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    
    print(BG_Dark_Red + Bright_Green)
    for char in Status_Off:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Rest +"")
    warning = '-> Script Part | Loaded LogIn Banner Successfully - Alert'
    logsTMB(warning)

def Index_Banner():
    #Welcoming Index Texts
    #Banner
    print(Bright_Red + "Note; Wait For 20sec, It Will Finish Soon"+ Bright_Yellow)
    for char in B1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B5:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B6:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B7:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Bright_Cyan + "")
    for char in Banner_msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Dark_Blue + BG_Dark_Green + "")
    for char in Line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.500)
    print(Rest + Bright_Green + BG_Dark_Blue)
    for char in Endl:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    
    print(BG_Dark_Blue + Bright_Green)
    for char in Status_On:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Rest +"")
    warning = '-> Script Part | Loaded Index Banner Successfully - Alert'
    logsTMB(warning)

def NoLoad_Banner():
    #Welcoming Index Texts
    #Banner
    print(Bright_Red + "Note; Wait For 0sec, It Will Finish Soon"+ Bright_Yellow)
    for char in B1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B5:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B6:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B7:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Bright_Cyan + "")
    for char in Banner_msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Dark_Blue + BG_Dark_Green + "")
    for char in Line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Rest + Bright_Green + BG_Dark_Blue)
    for char in Endl:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    
    print(BG_Dark_Blue + Bright_Green)
    for char in Status_On:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Rest +"")
    warning = '-> Script Part | Completed Varified No Load Banner Successfully - Alert'
    logsTMB(warning)

def NoLoad_Banner2():
    #Welcoming Index Texts
    #Banner
    print(Bright_Red + "Note; Wait For 0sec, It Will Finish Soon"+ Bright_Yellow)
    for char in B1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B5:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B6:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B7:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Bright_Cyan + "")
    for char in Banner_msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Dark_Blue + BG_Dark_Green + "")
    for char in Line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Rest + Bright_Green + BG_Dark_Blue)
    for char in Endl:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    
    print(BG_Dark_Red + Bright_Green)
    for char in Status_Off:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Rest +"")
    warning = '-> Script Part | Completed Unvarified No Load Banner Successfully - Alert'
    logsTMB(warning)

def Firewall_Banner():
    #Welcoming Index Texts
    #Banner
    print(Bright_Red + "Note; Wait For 0sec, It Will Finish Soon"+ Bright_Yellow)
    for char in FWB1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in FWB2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in FWB3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in FWB4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in FWB5:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in FWB6:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in FWB7:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Bright_Cyan + "")
    for char in FWBanner_msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Dark_Blue + BG_Dark_Green + "")
    for char in Line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Rest + Bright_Green + BG_Dark_Blue)
    for char in Endl:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    
    print(BG_Dark_Red + Bright_Green)
    for char in Status_Off:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Rest +"")
    warning = '-> Script Part | Completed Firewall Banner Successfully - Alert'
    logsTMB(warning)

#Network Connections
def InternetConnection():
    try:
        socket.create_connection((Host, Port), timeout=7)
        LogsSec = logsConfigs('Connection')
        if LogsSec <= 1:  
            warning = '-> Script Part | Checked Internet Connection Successfully - Alert'
            logsTMB(warning)
        return True
    except OSError:
        warning = '-> Script Part | Couldnt Check Internet Connection Successfully - Alert'
        logsTMB(warning)
        return False

def Running_InternetConnection():
    while True:
        if InternetConnection():
            return True
        else:
            return False

def Check_InternetConnection():
    if Running_InternetConnection() == True:
        return True
    else:
        return False
            
def Lost_InternetConnection():
    delSessions()
    clearConsole()
    NoLoad_Banner2()
    warning = '-> Script Part | Confirmed Losted Internet Connection Successfully - Warning'
    logsTMB(warning)
    print(Bright_Red + '\nPlease Note: You Just Lost Connection\nFor Total 7 Seconds So We Logged You Out!\nTo Proceed Please Run TechMystic PTS Again\nThank You For Studying With Us!')
    logsTMB('-> Scritp Part | Connection Lost And Logged Out Successfully - Alert')
    quit()

def InternetConnection_Status():
    if Check_InternetConnection() != True:
            Lost_InternetConnection()

#General Memory
def logsTMB(fileD):
    fileL = 'Plugs/Configs/MainConfigs/DATA/logs.txt'
    if os.path.exists(fileL):
        with open(fileL, 'a') as file:
            file.write('\n' + fileD)
    else:
        with open('Plugs/Configs/MainConfigs/DATA/logs.txt', 'w') as file:
            file.write(fileD)

def logsConfigs(fileT):
    fileL = 'Plugs/Configs/MainConfigs/DATA/LogsConfigs/Logs_' + fileT + '.txt'
    try:
        with open(fileL, 'r') as file:
            fileD = int(file.read())
            if fileT != 'Connection':
                warning = '-> Script Part | Opened And Read file:(' + fileT + '.txt) Successfully - Alert'
                logsTMB(warning)
            else:
                if fileD == 2:
                    warning = '-> Script Part | Opened And Read file:(' + fileT + '.txt) Successfully - Alert'
                    logsTMB(warning)
                elif fileD == 12:
                    warning = '-> Script Part | Opened And Read file:(' + fileT + '.txt) Successfully - Alert'
                    logsTMB(warning)
                elif fileD == 22:
                    warning = '-> Script Part | Opened And Read file:(' + fileT + '.txt) Successfully - Alert'
                    logsTMB(warning)
                elif fileD == 32:
                    warning = '-> Script Part | Opened And Read file:(' + fileT + '.txt) Successfully - Alert'
                    logsTMB(warning)
                elif fileD == 42:
                    warning = '-> Script Part | Opened And Read file:(' + fileT + '.txt) Successfully - Alert'
                    logsTMB(warning)
                elif fileD == 52:
                    warning = '-> Script Part | Opened And Read file:(' + fileT + '.txt) Successfully - Alert'
                    logsTMB(warning)

    except FileNotFoundError:
        fileD = 0
    fileD += 1
    with open(fileL, 'w') as file:
        file.write(str(fileD))
        if fileT != 'Connection':
            warning = '-> Script Part | Writted file:(' + fileT + '.txt) Successfully - Alert'
            logsTMB(warning)
        else:
            if fileD == 2:
                warning = '-> Script Part | Writted file:(' + fileT + '.txt) Successfully - Alert'
                logsTMB(warning)
            elif fileD == 12:
                warning = '-> Script Part | Writted file:(' + fileT + '.txt) Successfully - Alert'
                logsTMB(warning)
            elif fileD == 22:
                warning = '-> Script Part | Writted file:(' + fileT + '.txt) Successfully - Alert'
                logsTMB(warning)
            elif fileD == 32:
                warning = '-> Script Part | Writted file:(' + fileT + '.txt) Successfully - Alert'
                logsTMB(warning)
            elif fileD == 42:
                warning = '-> Script Part | Writted file:(' + fileT + '.txt) Successfully - Alert'
                logsTMB(warning)
            elif fileD == 52:
                warning = '-> Script Part | Writted file:(' + fileT + '.txt) Successfully - Alert'
                logsTMB(warning)
    return fileD    

def CountedFields(fileT):
    fileL = 'Plugs/Configs/MainConfigs/DATA/CountedFields_Info/Fielder_' + fileT + '.txt'
    try:
        with open(fileL, 'r') as file:
            fileD = int(file.read())
            warning = '-> Script Part | Opened And Read file:(' + fileT + '.txt) Successfully - Alert'
            logsTMB(warning)

    except FileNotFoundError:
        fileD = 0
    fileD += 1
    with open(fileL, 'w') as file:
        file.write(str(fileD))
        warning = '-> Script Part | Writted file:(' + fileT + '.txt) Successfully - Alert'
        logsTMB(warning)
    return fileD    

def sendTMB(fileF, fileT, fileD):
    with open('Plugs/Configs/MainConfigs/DATA/' + fileF +'_Info/'+ fileF +'_'+ fileT +'.txt', 'w') as file:
        file.write(fileD)
        warning = '-> Script Part | Writted file:(' + fileF +'_'+ fileT +'.txt) Successfully - Alert'
        logsTMB(warning)

def recvTMB(fileF, fileT):
    with open('Plugs/Configs/MainConfigs/DATA/'+ fileF +'_Info/'+ fileF +'_'+ fileT +'.txt', 'r') as file:
        fileD = file.read()
        warning = '-> Script Part | Opened And Read file:(' + fileF +'_'+ fileT +'.txt) Successfully - Alert'
        logsTMB(warning)
        return fileD

def checkTMB(fileF, fileT):
    fileD = 'Plugs/Configs/MainConfigs/DATA/'+ fileF +'_Info/'+ fileF +'_'+ fileT +'.txt'
    if os.path.exists(fileD):
        fileD_Result = 'Y'
        warning = '-> Script Part | Checked file:(' + fileF +'_'+ fileT +'.txt) Successfully - Alert'
        logsTMB(warning)
        return True
    else:
        fileD_Result = 'N'
        warning = '-> Script Part | Couldnt Check file:(' + fileF +'_'+ fileT +'.txt) Successfully - Warning'
        logsTMB(warning)
        return False

def delTMB(fileF, fileT):
    fileD = 'Plugs/Configs/MainConfigs/DATA/'+ fileF +'_Info/'+ fileF +'_'+ fileT +'.txt'
    if os.path.exists(fileD):
        os.remove(fileD)
        warning = '-> Script Part | Deleted file:(' + fileF +'_'+ fileT +'.txt) Successfully - Alert'
        logsTMB(warning)
    else:
        pass

def delSessions():
    folderL = 'Plugs/Configs/MainConfigs/DATA/LogsConfigs/'
    fileL = 'Plugs/Configs/MainConfigs/DATA/logs.txt'
    if os.path.exists(folderL):
        shutil.rmtree(folderL)
        os.makedirs(folderL, exist_ok=True)
    else:
        pass
        
    if os.path.exists(fileL):
        os.remove(fileL)
    else:
        pass

#Manual Memory
def TnCsAgree_File():
    filename = 'Plugs/Configs/MainConfigs/DATA/TnCs_Info/tncs_agreed.txt'
    return filename

def TnCsViewed_File():
    filename = 'Plugs/Configs/MainConfigs/DATA/TnCs_Info/tncs_viewed.txt'
    return filename

def TnCsAgreed():
    with open('Plugs/Configs/MainConfigs/DATA/TnCs_Info/tncs_agreed.txt', 'w') as file:
        file.write('Y')
        warning = '-> Script Part | Writted file:(tncs_agreed.txt) Successfully - Alert'
        logsTMB(warning)

def TnCsAgreed_Scan():
    with open('Plugs/Configs/MainConfigs/DATA/TnCs_Info/tncs_agreed.txt', 'r') as file:
        TnCs = file.read()
        warning = '-> Script Part | Opened And Read file:(tncs_agreed.txt) Successfully - Alert'
        logsTMB(warning)
        return TnCs

def TnCsViewed():
    with open('Plugs/Configs/MainConfigs/DATA/TnCs_Info/tncs_viewed.txt', 'w') as file:
        file.write('Y')
        warning = '-> Script Part | Writted file:(tncs_viewed.txt) Successfully - Alert'
        logsTMB(warning)

def TnCsViewed_Scan():
    with open('Plugs/Configs/MainConfigs/DATA/TnCs_Info/tncs_viewed.txt', 'r') as file:
        TnCs = file.read()
        warning = '-> Script Part | Opened And Read file:(tncs_viewed.txt) Successfully - Alert'
        logsTMB(warning)
        return TnCs

def iP_Info():
    iP_Address = socket.gethostbyname(socket.gethostname())
    logsTMB('-> Script Part | Got User iP Address Successfully - Pass')
    return iP_Address

def Mac_Info():
    Mac_Address = ':'.join(['{:02X}'.format((uuid.getnode() >> elements) & 0xFF) for elements in range(5, -1, -1)])
    logsTMB('-> Script Part | Got User Mac Address Successfully - Pass')
    return Mac_Address

def CurrentOS():
    OperatingSys = platform.system()
    logsTMB('-> Script Part | Got User Operating System Successfully - Pass')
    return OperatingSys

def LinuxDistro():
        system = platform.system()
        release = platform.release()
        if system == "Linux":
            logsTMB('-> Script Part | Got Linux User Distribution Successfully - Pass')
            return f" {release}"
        else:
            return "Not A Linux Operating System"


#Pip3 AutoInstallation
def install_pip3():
    subprocess.check_call([sys.executable, "-m", "ensurepip", "default-pip"])

#Linux Auto ScreenResizer
def screenResize(width, height):
    sys = platform.system()

    if sys == 'Linux':
        active_win_id = subprocess.check_output(['xdotool', 'getactivewindow']).decode('utf-8').strip()
        subprocess.run(['xdotool', 'windowsize', '--sync', active_win_id, str(width), str(height)])
    elif sys == 'Darwin':
        subprocess.run(['osascript', '-e', f'tell application "Terminal" to resize window to {w} by {h}'])
    elif sys == 'Windows':
        print(Bright_Red + "Please Note; Windows Can't Resize The Terminal.")
        pass
    else:
        print(Bright_Red + f"Unsupported Operating System: {sys}")

#Important Stored DATA
DATA_On = InternetConnection()

iP_Address = iP_Info()
Mac_Address = Mac_Info()
OS = CurrentOS()


if OS == "Linux":
    LinuxDistro = LinuxDistro()


if DATA_On == False:
    clearConsole()
    NoLoad_Banner2()
    print(Rest + Bright_Red + "\nPlease Note;" + Bright_Magenta + "\nTechMystic Script Can't Run Offline\nSo Make Sure Your Internet Connection\nIs On And Connecting Well Because Of Our\nTechMystic Python Script Cant Run Offline")
    LogsSec = logsConfigs('Offline')
    if LogsSec == 1:
        warning = '-> Script Part | Internet Connection Failed - Warning'
        logsTMB(warning)
    quit()

else:
    LoggedIn = CountedFields('LoggedIn')
    LoggedIn_RealTime = logsConfigs('LoggedIn')
    if Host != "localhost":
        InternetThread = threading.Thread(target=Running_InternetConnection)
        InternetThread.start()
        
        #Checking For Pip Installation And Install It If Is Not Installed
        pipMsg = "It Looks Like TechMystic Can't Find Pip3."
        pipSearch = "TechMystic Is Searching 4 Pip3 To Install"
        pipInstall = "TechMystic Now Installing Pip3..."
        pipInstalled = "TechMystic Is Done Installing Pip3!"
        LogsSec = logsConfigs('Online')
        if LogsSec == 1:
            warning = '-> Script Part | You Running TechMystic Online - Alert'
            logsTMB(warning)

        try:
            import pip3
            LogsSec = logsConfigs('Pip3')
            if LogsSec == 1:
                warning = '-> Script Part | Pip3 Imported Successfully - Alert'
                logsTMB(warning)
              
        except ImportError:
            clearConsole()
            NoLoad_Banner2()
            print(Bright_Magenta)
            for char in pipMsg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            print(Dark_Red + BG_Dark_Cyan + "")
            for char in pipSearch:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.500)
            print(Rest + Bright_Green + BG_Dark_Blue)
            for char in pipInstall:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)
            print(Rest + Bright_Magenta)
            #install_pip3()
            print(Rest + Bright_Green + BG_Dark_Blue)
            for char in pipInstalled:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            print(Rest)
    else:
        InternetThread = threading.Thread(target=Running_InternetConnection)
        InternetThread.start()
        #screenResize(100, 15)
        clearConsole()
        NoLoad_Banner2()
        print(Bright_Red + "\nPlease Note;\nTechMystic Is Running In A Localhost Mode")
        LogsSec = logsConfigs('Localhost')
        if LogsSec == 1:    
            warning = '-> Script Part | You Running TechMystic Locally - Warning'
            logsTMB(warning)

        #Viewing PHP Page
        WebURL = "http://localhost/techmystic/recv-data.php"
        A = "CypherIndex"
        B = "RSS"
        data = {'Name': A, 'Surname': B, 'Post': 'P_Info'}
        
        try:
            response = requests.post(WebURL, data=data)
            print(response.text)
        except requests.RequestException as e:
            print(f"Request error: {e}")
        
