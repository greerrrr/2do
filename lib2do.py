import os
import sys
import pdb
import logging
logging.basicConfig(level=logging.DEBUG, filename =
                    os.path.expanduser("~/.2do.log") , filemode  = "w")

class entry:
    def __init__(self,line):
        self.text=line.strip("\n")
        self.contents = line.strip()
        self.isReference = False
        self.isTask = False
        if self.contents == "":
            pass
        elif self.contents[0:2] == "./":
            self.isReference = True
        elif self.contents[0] == "*":
            self.isTask = True

class taskContext:
    def __init__(self,filename):
        self.name = filename
        self.fullpath = os.path.abspath(filename)
        todofile = open(filename, "r+")
        self.entries = []
        #pdb.set_trace()
        for line in todofile:
            self.entries.append(entry(line))

    def allTasks(self):
        all = []
        #pdb.set_trace()
        logging.debug("Running allTasks() from "+self.fullpath)
        os.chdir(os.path.dirname(self.fullpath))
        for item in self.entries:
            if item.isReference:
                subtasks = taskContext(item.contents).allTasks()
                for task in subtasks:
                    all.append(task)
                os.chdir(os.path.dirname(self.fullpath))
            else:
                all.append(item)
        return all

#    def addTask(self, input):
#        self.entries.append()
