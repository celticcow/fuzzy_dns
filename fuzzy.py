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

    conns = list()
    first_time = 0

    with open(file_name) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            src = row[0]
            dst = row[1]
            port = row[2]

            tmp_conn = conn(src, dst, port)

            if(first_time == 0):
                conns.append(tmp_conn)
                first_time = 1
                fuzzy_match(tmp_conn)
            else:
                found = 0
                for c in conns:
                    if(c.conn_compare(src, dst, port)):
                        #we have a existing connection
                        found = 1
                
                if(found == 0):
                    conns.append(tmp_conn)
                    fuzzy_match(tmp_conn)
                else:
                    c.increment_count()
            #if(fuzzy_match(dst) == False):
                #print(src + " -> " + dst + " : " + port)
                #fuzzy_match(dst)
            
        if(debug == 1):
            for con in conns:
                con.print_conn()
        
        ## need to retrn list
#end_of_read_file

def fuzzy_match(conn):
    """
    some statics
    199.82.243.70
    146.18.173.70
    """
    ip_addr = conn.get_dest()
    if(ip_addr == "199.82.243.70" or ip_addr == "146.18.173.70"):
        conn.set_metatag("outdated_dns server")
        #print(" outdated_dns server ")
        #return(False)
    elif("192.82.243.70" in ip_addr):
        conn.set_metatag("misconfig dns")
        #return(False)
    elif("199.112.46" in ip_addr):
        conn.set_metatag("anycast set wrong")
        #return(False)
    elif("199.81.46" in ip_addr):
        conn.set_metatag("anycast set wrong")
        #return(False)
    elif("198.112.46" in ip_addr):
        conn.set_metatag("anycast set wrong")
        #return(False)
    elif("192.112.45.53" in ip_addr):
        conn.set_metatag("anycast set wrong")
        #return(False)
    elif("192.116.46.53" in ip_addr):
        conn.set_metatag("anycast set wrong")
        #return(False)
    elif(ip_addr == "8.8.4.4" or ip_addr == "8.8.8.8"):
        conn.set_metatag("the googles")
        #return(False)
    else:
        conn.set_metatag("unknown dns")
        #return(True)
#end_of_fuzzy_match

def main():
    print("start of fuzzy dns")

    inputfile = "dns-out.csv"###"dns-test1.csv"

    conn_list = list()

    read_file(inputfile)

if __name__ == "__main__":
    main()