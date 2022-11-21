# ipv6-domain-ioc
# 20221120 update

1. 59 open source intelligence sources (650000 IOC records) were sorted out from maltrail, ntopng and other open source software of malicious traffic analysis systems: http://101.7.7.6/openioc.html  

2. Build IOC domain name resolution environment at 8 nodes of Education Network, China Unicom and Tencent Cloud to analyze and measure open source intelligence and summarize results
----11887 domain names can be parsed in v6: http://101.7.7.6/mal6.domain.ioc.txt
----There are 80,319 entries in the list of domain names that can be parsed in v4: http://101.7.7.6/mal.domain.ioc.txt  

3. 510 encrypted ore pool addresses: http://101.7.7.6/crypto-mining.txt

4. Through the list of domain names that can be parsed in v6, a server log of 101.7.8.9 DNS at the Beijing node on October 29/30 was matched on the big data platform, and 2217 domain names were accessed by 192 addresses. Eight IPv6 addresses access six domain names. There is little change between November and October

5. Provide download page: http://101.7.7.6:5006/file/list

The file structure is as follows:

1、CERNET-IPv6-BOT
1 /20 prefix 240c: c000/20 and 128 /28 prefixes:
st='net 240a:af80::/32'
for i in range(129,256):
    k= "{:02x}".format(i)
    st+=' or net 240a:af'+k+'::/32'
240a: a000 to collect non production network traffic on the IPv6 Internet

2. IPv6 Sensitive address "matches the netflow data of 41 nodes of the CERNET backbone network to obtain the IPv6 address list of sensitive ports, including the following 8. cat 20221121. netflow.txt | grep -- color=auto - e", 135 # "- e", 139 # "- e", 445 # "- e", 137 # "- e", 11211 # "- e", 27017 # "- e", 6379 # "- e", 3306 # "- e", 1433 # "- e", 5000 # "- e", 1521 # "- e", 9092 # ""

3. IPv6 active domain "obtains the list of malicious domain names from the blacklist of open source software of maltail and ntopng, and measures whether the domain name resolution result is active through multiple measurement points. If the IPv6 address of the resolution result is an active address on the public network, the domain name is recorded. The list of malicious domain names also includes the list of mining domain names, the list of qianxin commercial malicious domain names, and the list of open source malicious domain names threatening the fox threatfox"

4. IPv6 active ipaddress "is the same as the domain name resolution steps of IPv6 active domain in 3. Only IPv6 addresses resolved to public active addresses are recorded"

5. The IPv6 ioc dns log "is based on the domain name list of the IPv6 active domain in 3, and recursively parses the server log by matching 101.7.8.9 well-known dns with python programs. The log results also include the results of the list of four categories of malicious domain names in 3"

6. IPv6 rDNS rec "According to the blacklist of open source software of maltrail and ntopng, the domain name resolution results are measured through multiple nodes such as EDNET, China Unicom, Alibaba Cloud and Tencent Cloud, and whether the malicious domain name is active is judged according to whether the resolution results are public IPv6 addresses. If so, the list of IPv6 addresses and domain names is recorded"

7. Data "includes the original open source maltrail/ntopng malicious domain name list, mining domain name list, qianxin commercial malicious domain name list, threat fox threatfox open source malicious domain name list, alexa top100k domain name list file, and IPv6 address prefix company library"

8. Src "including the code file for querying the address prefix and the unit according to the IPv6 address, and the code file for querying the results of 101.7.8.9 recursive dns parsing log according to the malicious domain name list"

