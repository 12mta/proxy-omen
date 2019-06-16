import requests
from bs4 import BeautifulSoup
import json
import re
from time import sleep
#import urllib2
ptyp = "https"
annon_level = "elite"
class proxy:
    def __init__(self, proxy_type, ip_addr, proxy_port):
        self.proxy_type = proxy_type
        self.ip_addr = ip_addr
        self.proxy_port = proxy_port
        #self.full_proxy = proxy_type + " " + ip_addr + proxy_port
    def full_ip(self):
        return "{} {} {}".format(self.proxy_type, self.ip_addr, self.proxy_port)
#defines user_agent
user_agent = {'User-agent': 'Mozilla/5.0'}
headers = {
    'User-agent': 'Mozilla/5.0'
}
def get_proxie(ptype, annon_levely):
    api = "https://www.proxy-list.download/api/v1/get?type={}&anon={}".format(ptyp, annon_level)
    r = requests.get(api, headers=headers)
    proxy_content = r.text
    #print(proxy_content)
    ip_list = proxy_content.split()
    return(ip_list)

ip_list = get_proxie(ptyp, annon_level)
def test_proxy():
    ip_num_untested = len(ip_list)
    print("we are testinf {} proxies".format(ip_num_untested))
    for ip in ip_list:
        proxy_url = "{}://{}".format(ptyp, ip)
        pre_proxie = {"https": proxy_url}
        #print("testing: " + ip)
        working_ips = []
        try:
            sleep(1)
            url = "https://httpbin.org/ip'"
            response = requests.get(url,proxies=pre_proxie)
            print('{} is working'.format(ip))
            working_ips.append()
        except:
            print("{} is dead, skiping".format(ip))
get_proxie(ptyp, annon_level)
test_proxy()
print("don")
