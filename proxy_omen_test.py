import requests
from bs4 import BeautifulSoup
import json
import re
from time import sleep
import threading
import _thread

#import urllib2
ptyp = "socks5"
annon_level = "elite"
working_ips = []
headers = {
    'User-agent': 'Mozilla/5.0'
}
#
class run_proxies (threading.Thread):
    def __init__(self,x):
        self.__x = x
        threading.Thread.__init__(self)
    def run (self):
        proxy_url = "{}://{}".format(ptyp, ip)
            pre_proxie = {"https": proxy_url}
            #print("tedsting: " + ip)

            try:
                url = "https://httpbin.org/get'"
                response = requests.get(url,proxies=pre_proxie)
                print("{} is working ".format(ip))
            except:
                print("{} is dead, skiping".format(ip))


class proxy:

    def __init__(self, proxy_type, ip_addr, proxy_port):
            self.proxy_type = proxy_type
            self.ip_addr = ip_addr
            self.proxy_port = proxy_port
            #self.full_proxy = proxy_type + " " + ip_addr + proxy_port
    def full_ip(self):
        return "{} {} {}".format(self.proxy_type, self.ip_addr, self.proxy_port)

def get_proxie(ptype, annon_levely):
        api = "https://www.proxy-list.download/api/v1/get?type={}&anon={}".format(ptyp, annon_level)
        r = requests.get(api, headers=headers)
        proxy_content = r.text
        #print(proxy_content)
        ip_list = proxy_content.split()
        return(ip_list)

ip_list = get_proxie(ptyp, annon_level)
def test_proxy(input_ip_list):
        number_of_ip = len(input_ip_list)
        print("We are testing: {} ips".format(number_of_ip))
        num_threads = range(20)
        for tid in num_threads:
            threadps = run_proxies(tid)
        for ip in input_ip_list:
            for threadstart in tid:
                sleep(0.09)
                threadps.start()


            proxy_url = "{}://{}".format(ptyp, ip)
            pre_proxie = {"https": proxy_url}
            #print("tedsting: " + ip)
            """
            try:
                url = "https://httpbin.org/get'"
                response = requests.get(url,proxies=pre_proxie)
                print("{} is working ".format(ip))
            except:
                print("{} is dead, skiping".format(ip))
            """
            for x in range(20):
                run_proxies(x).join
            working_ips.append(ip)
#print(working_ips)
#x = 0
#run = run_proxies(x)
#for x in range(20):
    #run_proxies(x).start()

#get_proxie(ptyp, annon_level)
#test_proxy(ip_list)

#run_thread()
