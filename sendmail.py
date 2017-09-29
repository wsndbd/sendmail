#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '51tt11@51tt11.xyz'

import sys,os,time,datetime

timeNow = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

list_file = open('mail_address/part_0.txt')
try:
    temp_addr = list_file.readlines()
finally:
    list_file.close()
addr_list = temp_addr

conf_file = open('set.txt')
try:
    temp_conf = conf_file.readlines()
finally:
    conf_file.close()
set_list = temp_conf

def get_mail_fomat(index):
    return_str = set_list[index]
    return_str = return_str.replace("\n","")
    return_str = return_str.split('=')[1]
    return return_str

def send(to_addr,from_addr,subject,content,nick):
    try:
        os.system("cat %s|mutt -e 'set content_type=text/html' -e 'set realname=%s'  -e 'my_hdr from: %s'  -s %s  %s " % (content,nick, from_addr, subject, to_addr))
        os.system("echo '%s send to --> %s' >>log.txt " % (timeNow, to_addr))
        time.sleep(60)
        return True
    except:
        return False

if __name__ == '__main__':
    send_succeed_num = 0
    send_fail_num = 0
    mail_from = get_mail_fomat(0)
    mail_nick = get_mail_fomat(1)
    mail_subject = get_mail_fomat(2)
    mail_content = get_mail_fomat(3)

    for i in addr_list:
        if send(i,mail_from,mail_subject,mail_content,mail_nick):
            send_succeed_num +=1
        else:
            send_fail_num +=1
    os.system("echo 'All mails send finished! total Send --> %s' >>log.txt " % send_succeed_num)
    os.system('''echo "邮件群发已经完成，共发送%s封邮件。如有其它需要，请联系IT或运维" |mutt -s '请注意，邮件群发已经完成！' -e 'my_hdr from: root@51tt11.xyz' -c '51tt11@51tt11.xyz' ''' % send_succeed_num)
    os.system('''echo "邮件群发已经完成，共发送%s封邮件。如有其它需要，请联系IT或运维" >> log.txt''' % send_succeed_num)
