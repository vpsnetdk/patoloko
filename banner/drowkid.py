# -*- coding: UTF-8 -*-
# Generado en PatoMods. [by @drowkid01]
import os, sys, time
# Normal
black="\033[0;30m"
red="\033[0;31m"
green="\033[0;32m"
yellow="\033[0;33m"  
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
white="\033[0;37m"
# Bold
bblack="\033[1;30m"
bred="\033[1;31m"
bgreen="\033[1;32m"
byellow="\033[1;33m"
bblue="\033[1;34m"
bpurple="\033[1;35m"
bcyan="\033[1;36m"
bwhite="\033[1;37m"

# @patomods

# @drowkid01

# @botlatmx

logo='''
	\033[1;30m	╭─━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─╮
	\033[1;97m	█\033[1;96m	┏━┓┏━┓╺┳╸┏━┓╻  ┏━┓╻┏ ┏━┓\033[1;97m	█
	\033[1;97m	█\033[1;96m	┣━┛┣━┫ ┃ ┃ ┃┃  ┃ ┃┣┻┓┃ ┃\033[1;97m	█
	\033[1;97m	█\033[1;96m	╹  ╹ ╹ ╹ ┗━┛┗━╸┗━┛╹ ╹┗━┛\033[1;97m	█
	\033[1;30m	╰─━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─╯
'''

def slowprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.01)
slowprint(logo)
