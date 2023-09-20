"""
attendence system: record of coming inside and going outside

s  = "123_in,234_out,123_out"

Find out issues in this string, e.g. employee behaviour
out before in
never goes out
out twice
"""


def issues(s):

    my_dict = {}


    for i in s.split(","):
        x = i.split("_")

        if x[0] in my_dict:
            if (my_dict[x[0]] == "in" and x[1] == "out") or (my_dict[x[0]] == "out" and x[1] == "in"):
                my_dict[x[0]] = x[1]

            elif (my_dict[x[0]] == "in" and x[1] == "in") or (my_dict[x[0]] == "out" and x[1] == "out"):
                print("Employee ",x[0]," never went out to get in \n ")

        elif x[0] not in my_dict:
            if x[1] == "out":
                print("Employee ",x[0]," was never in to go out \n")
                my_dict[x[0]] = x[1]
            else:
                my_dict[x[0]] = x[1]

        x = []

    #print(my_dict)

    for i in my_dict:
        if my_dict[i] == "in":
            print("Employee ",i," is still in the office\n")







s = "123_in,123_in,123_out,234_out"

issues(s)

"""
Test Cases:
1. 

"""


