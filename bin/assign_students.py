#!/usr/bin/env python3

"""
Assign students to experiments using constraints.
"""

from random import randint

class student:
    def __init__(self, csvline):
        words = csvline.split(',')
        self.fname = words[0]
        self.lname = words[1]
        self.ID    = words[3]
        self.experiments = []

    def __str__(self):
        outstr  = "%s %s (%s)"%(self.fname, self.lname, self.ID)
        #outstr += ": %s %s %s %s"%(self.experiments[0], self.experiments[1], self.experiments[2], self.experiments[3])
        return outstr

class student_list:
    def __init__(self):
        self.students = {}
        self.IDs      = []

    def read_csv(self, rfile):
        print("Reading %s ..."%rfile)
        for line in open(rfile, 'r').readlines()[1:]:
            s  = student(line)
            ID = s.ID
            self.IDs         += [ID]
            self.students[ID] = s

###

class exp:
    inorganic = False
    organic   = False
    physical  = False
    ana       = False
    comp      = False
    nmax      = 0

    def __init__(self):
        self.IDs  = []

    def check(self, student):
        """
        Check if a student can be added to this experiment.
        """
        if len(self.IDs) >= self.nmax:
            return False
        else:
            return True

    def add(self, ID, slist):
        self.IDs += [ID]
        slist.students[ID].experiments += ['xx']

class comp_mod(exp):
    organic   = True
    comp      = True
    nmax      = 8

    def __str__(self):
        return 'Comp. Mod.'

class drug_scaff(exp):
    organic   = True
    nmax      = 6

    def __str__(self):
        return 'Scaffolds'

class xray(exp):
    inorganic = True
    comp      = True
    nmax      = 12

    def __str__(self):
        return 'X-ray'

class paracetamol(exp):
    physical  = True
    nmax      = 8

    def __str__(self):
        return 'Paracetamol'

###

class block:
    def __init__(self, experiments, slist, bi):
        self.experiments = experiments
        self.slist       = slist
        self.IDs         = [ID for ID in slist.IDs]
        self.bi          = bi

    def assign(self):
        for exp in self.experiments:
            for i, ID in enumerate(self.IDs):
                if exp.check(ID):
                    exp.add(self.IDs.pop(i), self.slist)

    def report(self):
        for exp in self.experiments:
            print("\n*** Experiment %s (%s) ***"%(exp, self.bi))
            for ID in exp.IDs:
                print(self.slist.students[ID])

        print("\n*** Not assigned (%s) ***"%self.bi)
        for ID in self.IDs:
            print(self.slist.students[ID])
###

if __name__=='__main__':
    slist = student_list()
    slist.read_csv('mini.csv')

    exps_1a = [comp_mod(), drug_scaff(), xray(), paracetamol()]
    block_1a = block(exps_1a, slist, '1a')
    block_1a.assign()
    block_1a.report()

    exps_2a = [comp_mod(), drug_scaff(), xray(), paracetamol()]
    block_2a = block(exps_2a, slist, '2a')
    block_2a.assign()
    block_2a.report()
