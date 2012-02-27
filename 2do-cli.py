#!/usr/bin/env python
import lib2do
import argparse
import sys
import os

parser = argparse.ArgumentParser(prog="2do", description='Recursively read .2do files')
parser.add_argument("path", help="The tasklist from to draw tasks from or add tasks to.", nargs='?')
parser.add_argument("-i", help="Inhibit recursive crawling for tasks",
                    action="store_false", dest="recurse")
args = parser.parse_args()
filepath = args.path

if filepath is None:
    candidates = dict()
    intkey = 0
    for filename in os.listdir("."):
        if filename[-4:] == ".2do":
            candidates[intkey] = filename
    print "No file given. Please select one of:"
    for key in candidates:
        print key,":", candidates[key]
    selection = input("Select file [1-%i]:"%key)
    filepath = candidates[selection]

rootContext = lib2do.taskContext(filepath)
for task in rootContext.allTasks():
    print task.text
