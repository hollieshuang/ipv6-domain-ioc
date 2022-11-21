# useage: python3 from-ipv6db-to-org-name-argv.py ../CERNET-IPv6-BOT/202211_bot_icmp-srcip.txt ../CERNET-IPv6-BOT/202211_bot_icmp-srcip.res
# useage: python3 from-ipv6db-to-org-name-argv.py ../CERNET-IPv6-BOT/202211_bot_tcp-udp-srcip.txt ../CERNET-IPv6-BOT/202211_bot_tcp-udp-srcip.res
#import SubnetTree
import os
import sys 
import time
import interval
#import IPy
import ipaddr
from random import randrange
from netaddr import IPRange

if __name__ == "__main__": 
    network_list = []
    for line in open('../data/z-ipv6-coun-city-rir.txt'):
        if "#" != line[0] and line[0] != "!":
            line = line.strip('\n')
            #line = line[:-1]
            #print("line=",line)
            array = line.split(',')
            #print("array[0]=",array[0])
            ip_network = array[0]
            lat = array[1]
            mask = ipaddr.IPNetwork(ip_network)
            # 保存网络表
            network_list.append((mask, ip_network, lat))
#            ip_attr[array[0]] = "%s" % array[1]
            #print(array[0],array[1])
    #要查询的ip文件和结果文件
    f_sd = open(sys.argv[1],'r')
    re_sd = open(sys.argv[2],'w')
    for linf in f_sd.readlines():
        linf = linf.strip('\n')
        #print(linf," len=",len(linf))
        if len(linf) < 7:
            continue
        for (mask, ip_network, lat) in network_list:
            #mask = ipaddr.IPNetwork(ip_network)
            addr = ipaddr.IPAddress(linf)
            if mask.Contains(addr):
                print(linf, ip_network, lat)
                re_sd.write(linf+' '+ip_network+' '+lat+'\n')
                break
            #else:
            #    print(linf,"NA")
            #    break


