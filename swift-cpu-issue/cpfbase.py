#!/usr/bin/python

import os, time
def busyloop():
    for x in range(0, 100):
        os.urandom(500000)

def do_sleep():
    time.sleep(10)

def testload():
    busyloop()
    do_sleep()

testload()
