#!/usr/bin/python3
from os import system as bash
try:
    from getkey import getkey,keys
except:
    print("[\u001b[31;1m!\u001b[0m] module 'getkey' not installed.To install module run '\u001b[32;4;1mpip3\u001b[0m\u001b[32;1m install getkey\u001b[0m'")
    print("[\u001b[32;1m*\u001b[0m] pip press TAB two times, It will show your pip's highset version.Use that instead of pip3")
    exit()
from time import sleep as sleep
bash("clear")
def _question_banner_(_option_):
    _curser_="\u001b[32;1m•> \u001b[37;1m"
    _end_="\u001b[0m"
    _dict_={1:"  \u001b[2;1m",2:"  \u001b[2;1m"}
    if _option_ == 1:
        _dict_[1]=_curser_
    if _option_ == 2:
        _dict_[2]=_curser_
    print("\u001b[41;1m\u001b[37;1m              Confirm               \u001b[0m\n\n\n\n\n\n")
    print("Do you want to install ?\n")
    print(_dict_[1]+"Yes "+_end_)
    print(_dict_[2]+"No \n\n\n\n\n\n\n\n"+_end_)
    print("\u001b[41;1m                                     \u001b[0m\r",end="")
def _question_(_code_):
    _option_=1
    bash("clear")
    _question_banner_(_option_)
    while True:
        key=getkey()
        if key == keys.UP:
            _option_-=1
        if key == keys.DOWN:
            _option_+=1
        if _option_ < 1:
            _option_=2
        if _option_ >2:
            _option_=1
        if key == keys.ENTER:
            if _option_ == 2:
                bash("clear")
                break
            else:
                if _code_==1:
                    _sqlmap_()
                if _code_==2:
                    _metasploit_()
                if _code_==3:
                    _fatrat_()
                if _code_==4:
                    _nmap_()
                if _code_==5:
                    _recon_ng_()
                if _code_==6:
                    _macfinder_()
                if _code_==7:
                    _john_()
                if _code_==8:
                    _zipet_()
                if _code_==9:
                    _cracknow_()
                if _code_==10:
                    _aircrack_()
                if _code_==11:
                    _wifite_()
                if _code_==12:
                    _sfish_()
                if _code_==13:
                    _spish_()
                if _code_==14:
                    _heye_()
                if _code_==15:
                    _scall_()
                if _code_==16:
                    _smsb_()
                break
        bash("clear")
        _question_banner_(_option_)

def _sqlmap_():
    bash("clear")
    bash("pip install sqlmap")
    print("\u001b[42;1m\u001b[37;1m            Processend              \u001b[0m")
def _metasploit_():
    bash("clear")
    bash("pkg install unstable-repo && pkg install metasploit && apt-install metasploit-framework")

    print("\u001b[42;1m\u001b[37;1m            Processend              \u001b[0m")
def _fatrat_():
    bash("git clone https://github.com/Screetsec/TheFatRat.git && cd TheFatRat && chmod +x setup.sh && ./setup.sh")
    print("\u001b[42;1m\u001b[37;1m            Processend              \u001b[0m")
def _nmap_():
    bash("pkg install unstable-repo && pkg install nmap && apt-get install nmap")
    print("\u001b[42;1m\u001b[37;1m            Processend              \u001b[0m")
def _recon_ng_():
    bash("git clone https://github.com/RED-5-CRACKERS/Recon-ng4Termux.git && cd Recon-ng4Termux && chmod +x setup.sh && ./setup.sh")
    print("\u001b[42;1m\u001b[37;1m            Processend              \u001b[0m")
def _macfinder_():
    bash("git clone https://github.com/RED-5-CRACKERS/Mac_finder.git && cd Mac_finder && chmod +x setup && ./setup")
    print("\u001b[42;1m\u001b[37;1m            Processend              \u001b[0m") 
def _john_():
    bash("git clone https://github.com/magnumripper/JohnTheRipper.git")
    print("\u001b[42;1m\u001b[37;1m            Processend              \u001b[0m")
def _zipet_():
    bash("git clone https://github.com/RED-5-CRACKERS/Zipet.git")
    print("\u001b[42;1m\u001b[37;1m            Processend              \u001b[0m")
def _cracknow_():
    bash("git clone https://github.com/Madhava-mng/Cracknow.git")
    print("\u001b[42;1m\u001b[37;1m            Processend              \u001b[0m")
def _aircrack_():
    bash("pkg install root-repo && pkg install aircrack-ng && apt-get install aircrack-ng")
    print("\u001b[42;1m\u001b[37;1m            Processend              \u001b[0m")
def _wifite_():
    bash("git clone https://github.com/derv82/wifite2.git")
    print("\u001b[42;1m\u001b[37;1m            Processend              \u001b[0m")
def _sfish_():
    bash("clear")
    bash("git clone https://github.com/UndeadSec/SocialFish.git")
    print("\u001b[42;1m\u001b[37;1m            Processend              \u001b[0m")
def _spish_():
    bash("clear")
    bash("git clone https://github.com/thelinuxchoice/shellphish.git")
    print("\u001b[42;1m\u001b[37;1m            Processend              \u001b[0m")
def _heye_():
    bash("clear")
    bash("git clone https://github.com/DarkSecDevelopers/HiddenEye.git")
    print("\u001b[42;1m\u001b[37;1m            Processend              \u001b[0m")
def _scall_():
    bash("clear")
    bash("git clone https://github.com/Aditya021/SpamCall.git")
    print("\u001b[42;1m\u001b[37;1m            Processend              \u001b[0m")
def _smsb_():
    bash("clear")
    bash("git clone https://github.com/AvinashReddy3108/YetAnotherSMSBomber.git")
    print("\u001b[42;1m\u001b[37;1m            Processend              \u001b[0m")
def _database_banner_(_option_):
    _curser_="\u001b[32;1m•> \u001b[37;1m"
    _end_="\u001b[0m"
    _dict_={1:"  \u001b[2;1m",2:"  \u001b[2;1m"}
    if _option_ == 1:
        _dict_[1]=_curser_
    if _option_ == 2:
        _dict_[2]=_curser_
    print("\u001b[41;1m\u001b[37;1m        DatabaseAssesment           \u001b[0m\n\n\n\n\n")
    print(_dict_[1]+"Sqlmap "+_end_)
    print(_dict_[2]+"Back \n\n\n\n\n\n\n\n\n\n\n"+_end_)
    print("\u001b[41;1m                                     \u001b[0m\r",end="")
def _database_():
    _option_=1
    _database_banner_(_option_)
    while True:
        key=getkey()
        bash("clear")
        if key == keys.UP:
            _option_-=1
        if key == keys.DOWN:
            _option_+=1
        if _option_ < 1:
            _option_=2
        if _option_ >2:
            _option_=1
        if key == keys.ENTER:
            if _option_ == 2:
                bash("clear")
                break
            else:
                _question_(_option_)
        _database_banner_(_option_)
def __option__(_option_):
    if _option_ == 1:
        _database_()
    if _option_ == 2:
        _exploitation_()
    if _option_ == 3:
        _information_()
    if _option_ == 4:
        _password_()
    if _option_ == 5:
        _wireless_()
    if _option_ == 6:
        _social_()
    if _option_ == 7:
        _spam_()

def _exploitation_banner_(_option_):
    _curser_="\u001b[32;1m•> \u001b[37;1m"
    _end_="\u001b[0m"
    _dict_={1:"  \u001b[2;1m",2:"  \u001b[2;1m",3:"  \u001b[2;1m"}
    if _option_ == 1:
        _dict_[1]=_curser_
    if _option_ == 2:
        _dict_[2]=_curser_
    if _option_ == 3:
        _dict_[3]=_curser_
    print("\u001b[41;1m\u001b[37;1m            Exploitation            \u001b[0m\n\n\n\n\n")
    print(_dict_[1]+"Metasploit-framework "+_end_)
    print(_dict_[2]+"Fatrat "+_end_)
    print(_dict_[3]+"Back \n\n\n\n\n\n\n\n\n\n"+_end_)
    print("\u001b[41;1m                                     \u001b[0m\r",end="")
def _exploitation_option_(_option_):
    if _option_==1:
        _question_(2)
    if _option_==2:
        _question_(3)
def _exploitation_():
    _option_=1
    _exploitation_banner_(_option_)
    while True:
        key=getkey()
        bash("clear")
        if key == keys.UP:
            _option_-=1
        if key == keys.DOWN:
            _option_+=1
        if _option_ < 1:
            _option_=3
        if _option_ >3:
            _option_=1
        if key == keys.ENTER:
            if _option_ == 3:
                bash("clear")
                break
            else:
                _exploitation_option_(_option_)
        _exploitation_banner_(_option_)


def _information_banner_(_option_):
    _curser_="\u001b[32;1m•> \u001b[37;1m"
    _end_="\u001b[0m"
    _dict_={1:"  \u001b[2;1m",2:"  \u001b[2;1m",3:"  \u001b[2;1m",4:"  \u001b[2;1m"}
    if _option_ == 1:
        _dict_[1]=_curser_
    if _option_ == 2:
        _dict_[2]=_curser_
    if _option_ == 3:
        _dict_[3]=_curser_
    if _option_ == 4:
        _dict_[4]=_curser_
    print("\u001b[41;1m\u001b[37;1m        Information Gathering       \u001b[0m\n\n\n\n\n")
    print(_dict_[1]+"Nmap "+_end_)
    print(_dict_[2]+"Recon-ng "+_end_)
    print(_dict_[3]+"Macfinder "+_end_)
    print(_dict_[4]+"Back \n\n\n\n\n\n\n\n\n"+_end_)
    print("\u001b[41;1m                                     \u001b[0m\r",end="")
def _information_option_(_option_): #### edit
    if _option_==1:
        _question_(4)
    if _option_==2:
        _question_(5)
    if _option_==3:
        _question_(6)
def _information_():
    _option_=1
    _information_banner_(_option_)
    while True:
        key=getkey()
        bash("clear")
        if key == keys.UP:
            _option_-=1
        if key == keys.DOWN:
            _option_+=1
        if _option_ < 1:
            _option_=4
        if _option_ >4:
            _option_=1
        if key == keys.ENTER:
            if _option_ == 4:
                bash("clear")
                break
            else:
                _information_option_(_option_)
        _information_banner_(_option_)

def _password_banner_(_option_):
    _curser_="\u001b[32;1m•> \u001b[37;1m"
    _end_="\u001b[0m"
    _dict_={1:"  \u001b[2;1m",2:"  \u001b[2;1m",3:"  \u001b[2;1m",4:"  \u001b[2;1m"}
    if _option_ == 1:
        _dict_[1]=_curser_
    if _option_ == 2:
        _dict_[2]=_curser_
    if _option_ == 3:
        _dict_[3]=_curser_
    if _option_ == 4:
        _dict_[4]=_curser_
    print("\u001b[41;1m\u001b[37;1m          Password Attacks          \u001b[0m\n\n\n\n\n")
    print(_dict_[1]+"John "+_end_)
    print(_dict_[2]+"Zipte "+_end_)
    print(_dict_[3]+"Cracknow "+_end_)
    print(_dict_[4]+"Back \n\n\n\n\n\n\n\n\n"+_end_)
    print("\u001b[41;1m                                     \u001b[0m\r",end="")
def _password_option_(_option_):
    if _option_==1:
        _question_(7)
    if _option_==2:
        _question_(8)
    if _option_==3:
        _question_(9)
def _password_():
    _option_=1
    _password_banner_(_option_)
    while True:
        key=getkey()
        bash("clear")
        if key == keys.UP:
            _option_-=1
        if key == keys.DOWN:
            _option_+=1
        if _option_ < 1:
            _option_=4
        if _option_ >4:
            _option_=1
        if key == keys.ENTER:
            if _option_ == 4:
                bash("clear")
                break
            else:
                _password_option_(_option_)
        _password_banner_(_option_)
def _wireless_banner_(_option_):
    _curser_="\u001b[32;1m•> \u001b[37;1m"
    _end_="\u001b[0m"
    _dict_={1:"  \u001b[2;1m",2:"  \u001b[2;1m",3:"  \u001b[2;1m"}
    if _option_ == 1:
        _dict_[1]=_curser_
    if _option_ == 2:
        _dict_[2]=_curser_
    if _option_ == 3:
        _dict_[3]=_curser_
    print("\u001b[41;1m\u001b[37;1m           Wireless Attacks         \u001b[0m\n\n\n\n\n")
    print(_dict_[1]+"Aircrack-ng "+_end_)
    print(_dict_[2]+"Wifite "+_end_)
    print(_dict_[3]+"Back \n\n\n\n\n\n\n\n\n\n"+_end_)
    print("\u001b[41;1m                                     \u001b[0m\r",end="")
def _wireless_option_(_option_):
    if _option_==1:
        _question_(10)
    if _option_==2:
        _question_(11)
def _wireless_():
    _option_=1
    _wireless_banner_(_option_)
    while True:
        key=getkey()
        bash("clear")
        if key == keys.UP:
            _option_-=1
        if key == keys.DOWN:
            _option_+=1
        if _option_ < 1:
            _option_=3
        if _option_ >3:
            _option_=1
        if key == keys.ENTER:
            if _option_ == 3:
                bash("clear")
                break
            else:
                _wireless_option_(_option_)
        _wireless_banner_(_option_)
##########
def _social_banner_(_option_):
    _curser_="\u001b[32;1m•> \u001b[37;1m"
    _end_="\u001b[0m"
    _dict_={1:"  \u001b[2;1m",2:"  \u001b[2;1m",3:"  \u001b[2;1m",4:"  \u001b[2;1m"}
    if _option_ == 1:
        _dict_[1]=_curser_
    if _option_ == 2:
        _dict_[2]=_curser_
    if _option_ == 3:
        _dict_[3]=_curser_
    if _option_ == 4:
        _dict_[4]=_curser_
    print("\u001b[41;1m\u001b[37;1m           Social Attacks           \u001b[0m\n\n\n\n\n")
    print(_dict_[1]+"SocialFish "+_end_)
    print(_dict_[2]+"ShellPhish"+_end_)
    print(_dict_[3]+"HiddenEye "+_end_)
    print(_dict_[4]+"Back \n\n\n\n\n\n\n\n\n"+_end_)
    print("\u001b[41;1m                                     \u001b[0m\r",end="")
def _social_option_(_option_): 
    if _option_==1:
        _question_(12)
    if _option_==2:
        _question_(13)
    if _option_==3:
        _question_(14)
def _social_():
    _option_=1
    _social_banner_(_option_)
    while True:
        key=getkey()
        bash("clear")
        if key == keys.UP:
            _option_-=1
        if key == keys.DOWN:
            _option_+=1
        if _option_ < 1:
            _option_=4
        if _option_ >4:
            _option_=1
        if key == keys.ENTER:
            if _option_ == 4:
                bash("clear")
                break
            else:
                _social_option_(_option_)
        _social_banner_(_option_)
##########
def _spam_banner_(_option_):
    _curser_="\u001b[32;1m•> \u001b[37;1m"
    _end_="\u001b[0m"
    _dict_={1:"  \u001b[2;1m",2:"  \u001b[2;1m",3:"  \u001b[2;1m"}
    if _option_ == 1:
        _dict_[1]=_curser_
    if _option_ == 2:
        _dict_[2]=_curser_
    if _option_ == 3:
        _dict_[3]=_curser_
    print("\u001b[41;1m\u001b[37;1m                Spamers             \u001b[0m\n\n\n\n\n")
    print(_dict_[1]+"Spamcall "+_end_)
    print(_dict_[2]+"YetAnothersmsBomper "+_end_)
    print(_dict_[3]+"Back \n\n\n\n\n\n\n\n\n\n"+_end_)
    print("\u001b[41;1m                                     \u001b[0m\r",end="")
def _spam_option_(_option_):
    if _option_==1:
        _question_(15)
    if _option_==2:
        _question_(16)
def _spam_():
    _option_=1
    _spam_banner_(_option_)
    while True:
        key=getkey()
        bash("clear")
        if key == keys.UP:
            _option_-=1
        if key == keys.DOWN:
            _option_+=1
        if _option_ < 1:
            _option_=3
        if _option_ >3:
            _option_=1
        if key == keys.ENTER:
            if _option_ == 3:
                bash("clear")
                break
            else:
                _spam_option_(_option_)
        _spam_banner_(_option_)
##########
def _menu_banner_(_option_):
    _curser_="\u001b[32;1m•> \u001b[37;1m"
    _end_="\u001b[0m"
    _dict_={1:"  \u001b[2;1m",
            2:"  \u001b[2;1m",
            3:"  \u001b[2;1m",
            4:"  \u001b[2;1m",
            5:"  \u001b[2;1m",
            6:"  \u001b[2;1m",
            7:"  \u001b[2;1m",
            8:"  \u001b[2;1m"}
    if _option_ == 1:
        _dict_[1]=_curser_
    if _option_ == 2:
        _dict_[2]=_curser_
    if _option_ == 3:
        _dict_[3]=_curser_
    if _option_ == 4:
        _dict_[4]=_curser_
    if _option_ == 5:
        _dict_[5]=_curser_
    if _option_ == 6:
        _dict_[6]=_curser_
    if _option_ == 7:
        _dict_[7]=_curser_
    if _option_ == 8:
        _dict_[8]=_curser_
    print("\u001b[41;1m\u001b[37;1m               Menu                 \u001b[0m\n\n\n\n\n")
    print(_dict_[1]+"Database Assement "+_end_)
    print(_dict_[2]+"Exploitation Tool "+_end_)
    print(_dict_[3]+"Information Gathering "+_end_)
    print(_dict_[4]+"Password Attacks "+_end_)
    print(_dict_[5]+"Wireless "+_end_)
    print(_dict_[6]+"Social Engnearing "+_end_)
    print(_dict_[7]+"Spamers "+_end_)
    print(_dict_[8]+"Exit \n\n\n\n\n"+_end_)
    print("\u001b[41;1m                                     \u001b[0m\r",end="")
def _menu_():
    _option_=1
    sleep(0.2)
    _menu_banner_(_option_)
    while True:
        key=getkey()
        bash("clear")
        if key == keys.UP:
            _option_-=1
        if key == keys.DOWN:
            _option_+=1
        if _option_ < 1:
            _option_ = 8
        if _option_ > 8:
            _option_ = 1
        if key == keys.ENTER:
            if _option_ != 8:
                __option__(_option_)
            else:
                break
        _menu_banner_(_option_)

_menu_()

