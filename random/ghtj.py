l1 = ["test1", "test2", "test3", "test4", "test5"]
l2 = ["t", "t", "t","t", "t", "t","t", "f", "t","t", "f", "t"]
mydict = {}

if len(l1) == len(l2):
    for i in range(len(l1)):
        mydict[l1[i]] = l2[i]
else:
    for j in range(min(len(l1),len(l2))):
        mydict[l1[j]] = l2[j]

    for x in range(len(l2),len(l1)):
        mydict[l1[x]] = "NA"

if "f" in l2:
    print(l2.index("f") + 1)
else:
    print("No Failures")

#print(mydict)

"""
linked list: each node is pointing to next node
A -> B <-> C

A <-> B 
"""
#
# def cyclic(head):
#     first = head
#     last = head
#
#     while last.next != None:
#         if first == head:
#             first = first.next
#         else:
#             if first.next == last:
#                 print("This is the cyclic linked list")
#                 break
#             else:
#                 last = first
#                 first = first.next







"""
remote server: run tests on it
"""
# import os
#
# class trigger_automation:
#
#     def __init__(self):
#         response = os.run("ssh username@ip")
#         if "Login Successful" in response:
#             self.trigger_run()
#             os.run("python3 /Users/gajanan/trigger.py")
#         else:
#             print("Error while doing ssh to the machine")
#             return False

    # def ssh_machine(self):
    #
    #
    # def trigger_run(self):
    #     res = os.run("ssh username@ip")
    #     response = os.run("python3 /Users/gajanan/trigger.py")
    #     if res:
    #         pass
    #     else:
    #         print("Error while triggering the automation")
    #         return False
    #



















"""
registration api: need documentation from devs

request:
[FEMALE, MALE, OTHER]
field: values from set of values 
fields accepting multiple values
fields accepting single value
fields optional none
mandatory keys

response:
- Mandatory fields are missing: print proper error of missing field
- field which accepts one value but we sent multiple
- getting response after successful registration
- generating id after registration
- 500: server errors

"""



























