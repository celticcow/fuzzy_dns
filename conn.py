#!/usr/bin/python3

"""
class defied to keep up with a connecton

source IP 
dest IP
Port (53 for our case here)

hit-count
"""

class conn(object):
    ## constructor
    def __init__(self, source="0.0.0.0", dest="0.0.0.0", port="0"):
        self.source = source
        self.dest = dest
        self.port = port
        self.count = 1
        self.metatag = ""
        

    #modifiers
    def set_source(self, source):
        self.source = source
    
    def set_dest(self, dest):
        self.dest = dest
    
    def set_port(self, port):
        self.port = port
    
    def increment_count(self):
        self.count = self.count + 1
    
    def set_metatag(self, tag):
        self.metatag = tag
    
    #accessors
    def get_source(self):
        return(self.source)
    
    def get_dest(self):
        return(self.dest)
    
    def get_port(self):
        return(self.port)

    def get_count(self):
        return(self.count)
    
    def get_metatag(self):
        return(self.metatag)

    def print_conn(self):
        print(self.source + " -> " + self.dest + " : " + self.port + " occured " + str(self.count) + " times" + " | " + self.metatag)
    
    #compare functions
    def conn_compare(self, s, d, p):
        if((self.source == s) and (self.dest == d) and (self.port == p)):
            return(True)
        else:
            return(False)