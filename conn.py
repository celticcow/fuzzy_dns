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
        self.count = 0

    #modifiers
    def set_source(self, source):
        self.source = source
    
    def set_dest(self, dest):
        self.dest = dest
    
    def set_port(self, port):
        self.port = port
    
    def increment_count(self):
        self.count = self.count + 1
    
    #accessors
    def get_source(self):
        return(self.source)
    
    def get_dest(self):
        return(self.dest)
    
    def get_port(self):
        return(self.port)

    def get_count(self):
        return(self.count)

    def print_conn(self):
        print(self.source + " -> " + self.dest + " : " + self.port + " occured " + self.count + " times")