#!/usr/bin/env python
import lib2do
import argparse
import sys

parser = argparse.ArgumentParser(prog="2do", description='Recursively read .2do files')
parser.add_argument("-f", help="The tasklist from to draw tasks from or add tasks to.", nargs='?', default=".2do")
parser.add_argument("-i", help="Inhibit recursive crawling for tasks",
                    action="store_false", dest="recurse")
flagsnshit = parser.parse_args()
print flagsnshit

# rootContext = lib2do.taskContext(sys.argv[1])
# for task in rootContext.allTasks():
#     print "* "+task.text
