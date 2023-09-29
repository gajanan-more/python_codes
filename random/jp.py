#
# #s = "mist@Dist2> show bgp summary Warning: License key missing; One or more members of the VC require 'bgp' license Threading mode: BGP I/O Default eBGP mode: advertise - accept, receive - accept Groups: 2 Peers: 4 Down peers: 0 Table          Tot Paths  Act Paths Suppressed    History Damp State    Pending inet.0                        2          2          0          0          0          0 bgp.evpn.0 16         16          0          0          0          0 Peer                     AS      InPkt     OutPkt    OutQ   Flaps Last Up/Dwn State|#Active/Received/Accepted/Damped... 10.255.240.7          65003       7942       7469       0       0 2d 11:31:09 Idle inet.0: 1/1/1/0 10.255.240.9          65004       7942       7474       0       0 2d 11:31:04 Establ inet.0: 1/1/1/0 172.16.254.3          65003      12618     777079       0       0 2d 11:30:59 Establ bgp.evpn.0: 8/8/8/0 default-switch.evpn.0: 7/7/7/0 __default_evpn__.evpn.0: 1/1/1/0 172.16.254.4          65004      12854     777216       0       0 2d 11:30:55 Connect bgp.evpn.0: 8/8/8/0 default-switch.evpn.0: 7/7/7/0 has context menu"
#
# s = """mist@Dist2> show bgp summary
#
#
#
# Warning: License key missing; One or more members of the VC require 'bgp' license
#
#
#
# Threading mode: BGP I/O
# Default eBGP mode: advertise - accept, receive - accept
# Groups: 2 Peers: 4 Down peers: 0
# Table          Tot Paths  Act Paths Suppressed    History Damp State    Pending
# inet.0               2          2          0          0          0          0
# bgp.evpn.0           16         16          0          0          0          0
#
# Peer                     AS      InPkt     OutPkt    OutQ   Flaps Last Up/Dwn State|#Active/Received/Accepted/Damped...
# 10.255.240.7          65003       7942       7469       0       0 2d 11:31:09 Idle inet.0: 1/1/1/0
# 10.255.240.9          65004       7942       7474       0       0 2d 11:31:04 Establ inet.0: 1/1/1/0
# 172.16.254.3          65003      12618     777079       0       0 2d 11:30:59 Establ bgp.evpn.0: 8/8/8/0 default-switch.evpn.0: 7/7/7/0 __default_evpn__.evpn.0: 1/1/1/0
# 172.16.254.4          65004      12854     777216       0       0 2d 11:30:55 Connect bgp.evpn.0: 8/8/8/0 default-switch.evpn.0: 7/7/7/0 """
#
# count = 0
# l2 = []
# if 'bgp' not in s:
#     count = 0
# else:
#     l1 = s.split("\n")
#     #print(l1)
#     for i in l1:
#         if 'Establ' in i:
#             l2 = i.split(" ")
#             #print(l2)
#
#             print("IP Address: ",l2[0]," AS: ",l2[10])
#     # mydict = {}
#     # #print(l1)
#     # for i in l1:
#     #     if i in mydict:
#     #         mydict[i] += 1
#     #     else:
#     #         mydict[i] = 1
#     #
#     # print(mydict)
#     #
#     # for j in mydict:
#     #     if mydict[j] > 1:
#     #         if j.isalpha():
#     #             print(j, ":", mydict[j])
#
#
#
#
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://mail.google.com/mail/u/0/#inbox")

username_field = driver.find_element_by_id("identifierId")

username_field.send_keys("dfdsfasdfadsgsdaga")

next_button = driver.find_element_by_id("identifierNext")

next_button.click()

password_field = driver.find_element_by_name("Passwd")



























