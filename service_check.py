#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# sudo pip install colorama
# sudo pip3 install requests
#
import subprocess
import traceback
import re
import time
import requests
import json
import os
#
from subprocess import Popen, PIPE, STDOUT
from time import sleep
from colorama import Fore, Style
#
#
failed   = " sudo systemctl --failed "
filename = "file_service_check.txt"
#
url_node = "https://nodejs.org/download/release/index.json"
#
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#
def ANSI_escape(input):
    # Remove ANSI escape sequences
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    data = ansi_escape.sub('', input)
    return data
#
def open_(command):
    n_ = Popen([command], shell=True, stdout=PIPE).stdout
    n_read = n_.read()
    return n_read
#
def open_utf_8(command):
    n_ = Popen([command], shell=True, stdout=PIPE, stderr=STDOUT).stdout
    n_read = n_.read()
    n_decode = n_read.decode('utf-8')
    return n_decode
    # open_("hostname | awk '{print $1}'")
#
def decode(versie_read,res):
    #decode_versie_read = versie_read.decode('utf-8')
    obj_read = str(versie_read) + '@'
    data_versie = obj_read.split('@')
    data_versie = data_versie[1]
    data_versie = data_versie.split('|')
    data_versie = data_versie[0]
    # Remove ANSI escape sequences
    nummer_versie = ANSI_escape(data_versie)
    nummer_versie = nummer_versie.strip(' ')
    nummer_versie = nummer_versie.replace("\n", "")
    nummer_versie = nummer_versie.strip(' ')
    #
    if nummer_versie == str :
        pass
#    if nummer_versie != float :
#        nummer_versie = str(0.0)
#        pass
    else:
        print ("decode is not a string")
        pass
    return nummer_versie
#
def service_check(service):
    service_ = open_utf_8("sudo service %s status" % service)
    #
    obj_service = str(service_) + ' ' + '  - '                                        # extention for preventing index error  # toevoeging ter voorkoming index error
    data_service = obj_service.split(' - ')
    data_service_ = data_service[0]
    data_service_ = data_service_.split(' ')
    data_service__ = data_service[1] + 'Active: ' + '(not found)' + ')'               # extention for preventing index error
    data_service__ = data_service__.split('Active: ')
    data_service__ = data_service__[1]
    data_service_s = data_service__.split(')')
    data_service_s = data_service_s[0]
    data_service_s = data_service_s.split('since ')
    data_service_status = data_service_s[0] + ')'
    #
    if data_service_[1] == '':
        name_service = service
    else:
        name_service = data_service_[1]
    #
    return name_service, data_service_status
    #
#
try:
    #
    print (" ")
    ip_decode = open_utf_8("hostname -I | awk '{print $1}'")
    ip = "ip = {} ".format(ip_decode)
    print (ip)
    #
    d_decode = open_utf_8("pwd")
    pwd = d_decode.strip('\n')
    d = "Working Directory = {} ".format(d_decode)
    print (d)
    #
    print ("check local nodejs")
    print ("... ")
    nodejs_decode = open_utf_8("node -v")
    nodejs_ = "local nodejs = {} ".format(nodejs_decode)
    print (nodejs_)
    v_nodejs = nodejs_decode.strip('v\n')
    value_nodejs = v_nodejs
    print (" ")
    #
    print ("check online nodejs")
    print ("... ")
    # https://nodejs.org/download/release/index.json
    node_online = requests.get(url_node)
    node_json = node_online.json()
    print ("...... ")
    list_node = node_json[0]
    dict_node = list_node['version']
    decode_node = str(dict_node)
    node_ = "online nodejs = {} ".format(decode_node)
    data_node = str(node_)
    print (data_node)
    v_node = dict_node.strip('v\n')
    value_node = v_node
    print (" ")
    #
    print ("check local npm")
    print ("... ")
    decode_npm_local = open_utf_8("npm -v")
    print ("...... ")
    data_npm_local = str(decode_npm_local)
    number_npm_value = data_npm_local.replace("\n", "")
    local_npm_value = "local npm = " + number_npm_value
    #
    print (local_npm_value)
    print (" ")
    #
    print ("check online npm")
    print ("... ")
    online_npm_read = open_utf_8("npm v npm")
    print ("...... ")
    number_online_npm = ()
    number_online_npm_value = decode(online_npm_read, number_online_npm)
    online_npm_value = "online npm = " + number_online_npm_value
    print (online_npm_value)
    print (" ")
    #
    print ("check local versie homebridge")
    print ("... ")
#    versie_local_hb = Popen(["npm list -g homebridge"], shell=True, stdout=PIPE).stdout
#    versie_local_hb_read = versie_local_hb.read()
    versie_local_hb_read = open_utf_8("npm list -g homebridge")
    print ("...... ")
    number_local_hb = ()
    number_local_hb_value = decode(versie_local_hb_read, number_local_hb)
#    number_local_hb_value = str(number_local_hb_value)
    versie_local_hb_value = "local homebridge = " + number_local_hb_value
    print (versie_local_hb_value)
    print (" ")
    #
    print ("check online versie homebridge")
    print ("... ")
#    versie_hb_online = Popen(["npm v homebridge"], shell=True, stdout=PIPE).stdout
#    versie_online_hb_read = versie_hb_online.read()
    versie_online_hb_read = open_utf_8("npm v homebridge")
    print ("...... ")
    number_online_hb = ()
    number_online_hb_value = decode(versie_online_hb_read, number_online_hb)
    versie_online_hb_value = "online homebridge = " + number_online_hb_value
    print (versie_online_hb_value)
    print (" ")
    #
    print ("check local versie homebridge plugin Airco")
    print ("... ")
#    versie_local = subprocess.run(["npm list -g homebridge-panasonic-air-conditioner"], shell=True)
#    versie_local_p_a = Popen(["npm list -g homebridge-panasonic-air-conditioner"], shell=True, stdout=PIPE).stdout
#    versie_local_p_a_read = versie_local_p_a.read()
    versie_local_p_a_read = open_("npm list -g homebridge-panasonic-air-conditioner")
    print ("...... ")
    # homebridge-panasonic-air-conditioner@2.1.1
    number_local_p_a = ()
    number_local_p_a_value = decode(versie_local_p_a_read, number_local_p_a)
    versie_local_p_a_value = "local plugin = " + number_local_p_a_value
    print (versie_local_p_a_value)
    print (" ")
    #
    print ("check online versie homebridge plugin Airco")
    print ("... ")
#    versie_online = subprocess.run(["npm v homebridge-panasonic-air-conditioner"], shell=True)
#    versie_online_p_a = Popen(["npm v homebridge-panasonic-air-conditioner"], shell=True, stdout=PIPE).stdout
#    versie_online_p_a_read = versie_online_p_a.read()
    versie_online_p_a_read = open_("npm v homebridge-panasonic-air-conditioner")
    print ("...... ")
    # homebridge-panasonic-air-conditioner@6.1.6 |
    number_p_a_online = ()
    number_online_p_a_value = decode(versie_online_p_a_read, number_p_a_online)
    versie_online_p_a_value = "online plugin = " + number_online_p_a_value
    print (versie_online_p_a_value)
    print (" ")
    print (bcolors.RED + "Plugin is replaced by Platform" + bcolors.ENDC)
    print (" ")
    #
    print ("check HomeBridge service")
#    hb_service = 'HomeBridge'
    print ("... ")
    hb_service, hb_status = service_check('homebridge')
    print ("...... ")
    print ("{} = {}".format(hb_service, hb_status))
    print (" ")
    #
    print ("check Systeminfo service")
#    systeminfo_service = 'Systeminfo'
    print ("... ")
    systeminfo_service, systeminfo_status = service_check('systeminfo')
    print ("...... ")
    print ("{} = {}".format(systeminfo_service, systeminfo_status))
    print (" ")
    #
    print ("check MQTT-broker service")
#    mqtt_service = 'MQTT'
    print ("... ")
    mqtt_service, mqtt_status = service_check('mosquitto')
    print ("...... ")
#    print ('status = ' + mqtt_status)
    print ("{} = {}".format(mqtt_service, mqtt_status))
    print (" ")
    #
    print ("check Watertank service")
#    watertank_service = 'Watertank'
    print ("... ")
    watertank_service, watertank_status = service_check('watertank')
    print ("...... ")
    print ("{} = {}".format(watertank_service, watertank_status))
    print (" ")
    #
    print ("check system control")
    print ("... ")
    system_read = open_utf_8("sudo systemctl status")
    #
    system_read_S = system_read.split('\n')
#    print (system_read_S[0])                  # ● TUINHUIS
#    print (system_read_S[1])                  #     State: running
#    print (system_read_S[2])                  #      Jobs: 0 queued
#    print (system_read_S[3])                  #    Failed: 0 units
#    print (system_read_S[4])                  #     Since: Thu 1970-01-01 01:00:02 CET; 52 years 7 months ago'
    #
    system_name   = system_read_S[0].split(': ')
    system_s      = system_read_S[1].split(': ')
    system_state  = system_s[1]
    system_jobs   = system_read_S[2].split(': ')
    system_failed = system_read_S[3].split(': ')
    #
    data_system_ = (system_state + " ,  Failed : " + system_failed [1])
    #
    mes_system = "State {} = {}".format(system_name, data_system_)
    if system_state == "degraded":
        degraded_read = open_("sudo systemctl --failed")
#        degraded_ = Popen(["sudo systemctl --failed"], shell=True, stdout=PIPE).stdout
#        degraded_read = degraded_.readlines()
        degraded_1 = str(degraded_read)
        degraded_list = ['ERROR END ']
#        degraded_list = [' TEST@TEST.service loaded failed test helper\n', 'ERROR END ']
        for line in degraded_read:
            if b".service" in line:
                l = line.decode("utf-8")
                degraded_list.insert(0, l)
#        print (degraded_list)
        for item in degraded_list:
            d = str(item)
            d_s = d.split(' ')
            d_1 = d_s[1]
            print (d_1)
        mes_system = name_system_ + " = " +  data_system_ + '\n' + "use " + failed + " for information "
        print (mes_system)
    else:
        print (mes_system)
    print (" ")
    #
    #
    if value_nodejs != value_node:
        print (bcolors.RED + "not equel nodejs" + bcolors.ENDC)
#        process = subprocess.run(["sudo npm install -g npm"], shell=True)
        sleep(5)
        print (" ")
    else:
        print (bcolors.OKGREEN + "equal nodejs" + bcolors.ENDC)
        print (" ")
    #
    if number_npm_value != number_online_npm_value:
        print (bcolors.RED + "not equel npm" + bcolors.ENDC)
#        process = subprocess.run(["sudo npm install -g npm"], shell=True)
        sleep(5)
        print (" ")
    else:
        print (bcolors.OKGREEN + "equal npm" + bcolors.ENDC)
        print (" ")
    #
    if number_local_hb_value != number_online_hb_value:
        print (bcolors.RED + "not equal homebridge" + bcolors.ENDC)
#        process = subprocess.run(["sudo npm install -g homebridge"], shell=True)
        print (" ")
    else:
        print (bcolors.OKGREEN + "equal homebridge" + bcolors.ENDC)
        print (" ")
    #
    if number_local_p_a_value != number_online_p_a_value:
        print (bcolors.RED + "not equal plugin Airco" + bcolors.ENDC)
#        process = subprocess.run(["sudo npm install -g homebridge-panasonic-air-conditioner"], shell=True)
        print (" ")
    else:
        print (bcolors.OKGREEN + "equal plugin Airco" + bcolors.ENDC)
        print (" ")
    #
    user = os.getlogin()
    print (user)
    #
    time_now = time.time
    # Schrijf naar File dan copy t.b.v. mail
    # write to File then copy for mail
    #
    # f= open("/home/{}/{}".format(user,filename),"w+")
    f= open("{}/{}".format(pwd,filename),"w+")
    #
    f.write("{}\r".format(ip))
    f.write("{}\r".format(nodejs_))
    f.write("{}\r".format(data_node))
    f.write("{}\r\n".format(local_npm_value))
#    f.write("%s\r\n" % online_npm_value)
    f.write("{}\r\n".format(versie_local_hb_value))
#    f.write("%s\r\n" % versie_online_hb_value)
    f.write("{}\r\n".format(versie_local_p_a_value))
#    f.write("%s\r\n" % versie_online_p_a_value)
    f.write("\r\n")
#    f.write("{} = {}\r\n".format(domoticz_service, domoticz_status))
    f.write("{} = {}\r\n".format(hb_service, hb_status))
    f.write("{} = {}\r\n".format(systeminfo_service, systeminfo_status))
#    f.write("{} = {}\r\n".format(input_service, input_status))
    f.write("{} = {}\r\n".format(mqtt_service, mqtt_status))
    f.write("{} = {}\r\n".format(watertank_service, watertank_status))
    f.write("{}\r\n".format(mes_system))
#    f.write(time_now)
    f.close
    print ("File Writen ")
#    Popen(["scp {}/{} pi@10.0.1.27:/home/pi/{}".format(pwd, filename, filename)], shell=True)
#     open_("scp {}/{} pi@10.0.1.27:/home/pi/{}".format(pwd, filename, filename))
    print (bcolors.OKBLUE + filename + bcolors.ENDC)
#    print ("File COPIED ")
    print (" ")
    #
except Exception as e:
        print (" ")
        print (bcolors.FAIL + "Oops!  Try again..." + bcolors.ENDC)
        print (" ")
        print (traceback.format_exc())
except KeyboardInterrupt:
        print (bcolors.WARNING + "ctrl + C Pressed" + bcolors.ENDC)
#
