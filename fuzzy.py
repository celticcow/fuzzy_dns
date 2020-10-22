#!/usr/bin/python3

import csv
import ipaddress

from conn import conn

"""
trying to find bad dns calls
fuzzy logic around ip schema
"""

def read_file(file_name):
    print("reading file")

    debug = 1

    with open(file_name) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            src = row[0]
            dst = row[1]
            port = row[2]

            if(fuzzy_match(dst) == False):
                print(src + " -> " + dst + " : " + port)
                #fuzzy_match(dst)
            #much more to come here

#end_of_read_file

def fuzzy_match(ip_addr):
    """
    some statics
    199.82.243.70
    146.18.173.70
    """
    if(ip_addr == "199.82.243.70" or ip_addr == "146.18.173.70"):
        #print(" outdated_dns server ")
        return(False)
    
    if("192.82.243.70" in ip_addr):
        #print(" misconfig dns ")
        return(False)

    if("199.112.46" in ip_addr):
        #print(" anycast set wrong ")
        return(False)
    
    if("199.81.46" in ip_addr):
        #print(" anycast set wrong ")
        return(False)
    
    if("198.112.46" in ip_addr):
        #print(" anycast set wrong ")
        return(False)
    
    if("192.112.45.53" in ip_addr):
        #print(" anycast set wrong ")
        return(False)

    if("192.116.46.53" in ip_addr):
        #print(" anycast set wrong ")
        return(False)
    
    if(ip_addr == "8.8.4.4" or ip_addr == "8.8.8.8"):
        #print(" the googles ")
        return(False)
    
    return(True)

def main():
    print("start of fuzzy dns")

    inputfile = "dns-out.csv"

    read_file(inputfile)

if __name__ == "__main__":
    main()