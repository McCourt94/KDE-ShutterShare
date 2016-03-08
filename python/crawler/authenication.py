#!/usr/bin/env python
import sys
import shutil
import urllib
 
import flickr
 
 
def get_link(permission):
    p = permission
    auth = flickr.Auth()
    t = auth.loginLink(p)
    return t

def get_token(frob):
    print frob
    f = frob
    auth = flickr.Auth()
    a = auth.getToken(f)
    return a  
 
def main():
    a = get_link('read')
    b = get_token('72157664127342812-0009eb03a57b9c2d-136083788')
    print b
    
 
if __name__ == '__main__':
    sys.exit(main())