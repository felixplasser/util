#!/usr/bin/env python3

"""
Assign students to experiments using constraints.
"""

from random import randint

class student:
    mxi = 1
    mxo = 1
    mxp = 1
    mxa = 1
    mxb = 1
    mxc = 1
    mod = 'CMC'

    def __init__(self, csvline):
        words = csvline.split(',')
        self.fname = words[0]
        self.lname = words[1]
        self.ID    = words[3]
        self.experiments = []

    def __str__(self):
        outstr  = "%s %s (%s) - %s"%(self.fname, self.lname, self.ID, self.mod)
        #outstr += ": %s %s %s %s"%(self.experiments[0], self.experiments[1], self.experiments[2], self.experiments[3])
        return outstr

    def check(self, experiment):
        """
        Check if a student can be assigned a given experiment.
        """
        norganic = 0
        ninorganic = 0
        nphys = 0
        nana = 0
        nbio = 0
        ncomp = 0
        for e in self.experiments:
            if e.__str__() == experiment.__str__(): return False # Don't assign the same experiment twice
            if e.organic:   norganic += 1
            if e.inorganic: ninorganic += 1
            if e.physical:  nphys += 1
            if e.ana:       nana += 1
            if e.bio:       nbio += 1
            if e.comp:      ncomp += 1

        if experiment.organic:   norganic += 1
        if experiment.inorganic: ninorganic += 1
        if experiment.physical:  nphys += 1
        if experiment.ana:       nana += 1
        if experiment.bio:       nbio += 1
        if experiment.comp:      ncomp += 1

        print(norganic, ninorganic, nphys, nana, nbio, ncomp)

        if norganic > self.mxo:   return False
        if ninorganic > self.mxi: return False
        if nphys > self.mxp:      return False
        if nana  > self.mxa:      return False
        if nbio  > self.mxb:      return False
        if ncomp > self.mxc:      return False

        return True

class CMC029_student(student):
    mxi = 1
    mxo = 2
    mxp = 1
    mxa = 0
    mxb = 0
    mxc = 2
    mod = 'CMC029'

class CMC027_student(student):
    mxi = 1
    mxo = 1
    mxp = 0
    mxa = 0
    mxb = 2
    mxc = 0
    mod = 'CMC027'

class CMC026_student(student):
    mxi = 1
    mxo = 1
    mxp = 1
    mxa = 1
    mxb = 1
    mxc = 1
    mod = 'CMC026'

class student_list:
    def __init__(self):
        self.students = {}
        self.IDs      = []

    def read_csv(self, rfile, stype):
        print("Reading %s ..."%rfile)
        for line in open(rfile, 'r').readlines()[1:]:
            s  = stype(line)
            ID = s.ID
            self.IDs         += [ID]
            self.students[ID] = s

    def report(self):
        print("\n*** Report over students ***")
        for ID in self.IDs:
            print(self.students[ID], [str(e) for e in self.students[ID].experiments])

###

class exp:
    inorganic = False
    organic   = False
    physical  = False
    ana       = False
    bio       = False
    comp      = False
    nmax      = 0
    expname   = ''

    def __init__(self):
        self.IDs  = []

    def check(self, student):
        """
        Check if a student can be added to this experiment.
        """
        if len(self.IDs) >= self.nmax:
            return False
        else:
            return student.check(self)

    def add(self, student):
        self.IDs += [student.ID]
        student.experiments += [self]

    def __str__(self):
        return self.expname

# Semester 1

class drug_scaff(exp):
    organic   = True
    nmax      = 8
    expname   = 'Scaffolds in drug devel.'

class green_cross(exp):
    organic   = True
    nmax      = 8
    expname   = 'Green catalytic cross coupling.'

class comp_mod(exp):
    organic   = True
    comp      = True
    nmax      = 8
    expname   = 'Comp. modelling'

class prot_lig(exp):
    bio  = True
    nmax = 8
    expname   = 'Protein-ligand binding'

class cell_resp(exp): # also Semester 2
    bio  = True
    nmax = 8
    expname   = 'Cell responses'

class thiamine(exp):
    ana  = True
    nmax = 8
    expname   = 'Thiamine content'

class hplc(exp):
    ana  = True
    nmax = 8
    expname   = 'HPLC'

# Semester 2

class xray(exp):
    inorganic = True
    comp      = True
    nmax      = 8
    expname   = 'X-ray'

class zeolites(exp):
    inorganic = True
    nmax      = 8
    expname   = 'Zeolites'

class fingerprint(exp):
    inorganic = True
    nmax      = 8
    expname   = 'Fingerprinting reagents'

class salen(exp):
    inorganic = True
    nmax      = 8
    expname   = 'M-SALEN complexes'

class paracetamol(exp):
    physical  = True
    nmax      = 8
    expname   = 'Paracetamol'

class tio2(exp):
    physical = True
    nmax     = 8
    expname   = 'Properties of TiO2'

###

class block:
    def __init__(self, experiments, slist, bi):
        self.experiments = experiments
        self.slist       = slist
        self.assigned    = [False for ID in slist.IDs]
        self.bi          = bi

    def assign(self):
        for exp in self.experiments:
            for i, ID in enumerate(self.slist.IDs):
                if self.assigned[i]:
                    continue
                elif exp.check(slist.students[ID]):
                    exp.add(slist.students[ID])
                    self.assigned[i] = True

    def report(self):
        for exp in self.experiments:
            print("\n*** Experiment %s (%s) ***"%(exp, self.bi))
            print("  Number of students: %i"%len(exp.IDs))
            for ID in exp.IDs:
                print(self.slist.students[ID])

        print("\n*** Not assigned (%s) ***"%self.bi)
        for i, yn in enumerate(self.assigned):
            if not yn:
                print(self.slist.students[self.slist.IDs[i]])
###

if __name__=='__main__':
    slist = student_list()
    slist.read_csv('CMC029_participants.csv', CMC029_student)
    slist.read_csv('CMC027_participants.csv', CMC027_student)
    slist.read_csv('CMC026_participants.csv', CMC026_student)


    exps_1a = [comp_mod(), prot_lig(), cell_resp(), drug_scaff(), green_cross(), thiamine(), hplc()]
    block_1a = block(exps_1a, slist, '1a')
    block_1a.assign()
    block_1a.report()

    #slist.IDs.reverse()

    print('Second round')
    exps_1b = [comp_mod(), prot_lig(), cell_resp(), drug_scaff(), green_cross(),  thiamine(), hplc()]
    block_1b = block(exps_1b, slist, '1b')
    block_1b.assign()
    block_1b.report()

    #exps_2a = [comp_mod(), drug_scaff(), xray(), paracetamol()]
    #block_2a = block(exps_2a, slist, '2a')
    #block_2a.assign()
    #block_2a.report()

    #exps_2b = [comp_mod(), drug_scaff(), xray(), paracetamol()]
    #block_2b = block(exps_2b, slist, '2b')
    #block_2b.assign()
    #block_2b.report()

    slist.report()
