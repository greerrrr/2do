#!/usr/bin/env python
import lib2do
import argparse
import sys
import os

def find_root(filelist):
    adjacencylist = dict()
    for todo in filelist:
        adjacent = []
        try:
            f = open(todo, "r")
        except:
            print "Failed to open %s when finding root."
            break

        for line in f:
            if line.strip()[0:2] == "./":
                adjacent.append(os.path.basename(line.strip()))
        adjacencylist[todo] = adjacent




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
            intkey+=1
    if intkey == 1:
        filepath = candidates[0]
    else:
        print "No file given. Please select one of:"
        for key in candidates:
            print key,":", candidates[key]
        selection = " "
        while selection != "" and selection.isdigit() == False:
            selection = raw_input("Select file [0-%i]:"%key)
            if selection == "":
                selection = "0"
        selection = int(selection)
        filepath = candidates[selection]

rootContext = lib2do.taskContext(filepath)
for task in rootContext.allTasks():
    print task.text
