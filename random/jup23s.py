import json
strg = """
{
"networks": {
        "v44": {
            "vlan_id": "44"
        },
        "v33": {
            "vlan_id": "33"
        }
    },
"ospf_areas": {
        "33": {
            "type": "nssa",
            "networks": {
                "v33": {
                    "interface_type": "nbma",
                    "passive": false
                }
            }
        },
        "44": {
            "type": "stub",
            "networks": {
                "v44": {
                    "interface_type": "p2mp",
                    "passive": false
                }
            }
        }
    }}
"""




def add_input(strg,ospf_areas,type_network="stub",interface_type="p2mp", passive=False):
    mydict = json.loads(strg)

    # mydict["ospf_areas"][ospf_areas]["type"] = type

    if ospf_areas in mydict["ospf_areas"]:
        print("Area is already there")
    else:

        ospf = dict()

        ospf[ospf_areas] = type_network
        network_dict = dict()
        x = "v"+ospf_areas
        network_dict[x] = {}
        network_dict[x]["interface_type"] = interface_type
        network_dict[x]["passive"] = passive

        mydict[ospf_areas]= dict()
        mydict[ospf_areas]["type"]= type_network
        mydict[ospf_areas]["networks"] = dict()
        mydict[ospf_areas]["networks"] = network_dict

        print(mydict)


add_input(strg = strg,ospf_areas = "44")

add_input(strg=strg,ospf_areas="77",type_network="notstub",interface_type="pmp",passive=True)










class A:
    def __init__(self):
        pass
    A = 10

    def one(self):
        pass

class B(A):
    def __init__(self):
        pass
    A = 18

    def two(self):
        pass