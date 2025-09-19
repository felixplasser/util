#!/usr/bin/env python3

"""
Assign students to experiments using constraints.
"""

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
        self.experiments = 4 * [not_assigned()]

    def __str__(self):
        outstr  = "%s %s (%s) - %s"%(self.fname, self.lname, self.ID, self.mod)
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
            if e is None: continue
            if e.expname == experiment.expname: return False # Don't assign the same experiment twice

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

class CMC026_004_student(student):
    mxi = 1
    mxo = 1
    mxp = 1
    mxa = 1
    mxb = 0
    mxc = 1
    mod = 'CMC026-004'

class CMC026_007_student(student):
    mxi = 1
    mxo = 1
    mxp = 1
    mxa = 0
    mxb = 1
    mxc = 1
    mod = 'CMC026-007'


class student_list:
    def __init__(self):
        self.students = {}
        self.IDs      = []

    def read_csv(self, rfile, stype):
        print("\nReading %s ..."%rfile)

        nread = 0
        for line in open(rfile, 'r').readlines()[1:]:
            s  = stype(line)
            ID = s.ID
            self.IDs         += [ID]
            self.students[ID] = s
            nread += 1

        print("Read %i students for %s"%(nread, stype.mod))

    def report(self):
        print("\n*** Report over students ***")
        for ID in self.IDs:
            print(self.students[ID], [str(e) for e in self.students[ID].experiments])

    def write_csv(self, cname='CMC02x.csv'):
        f = open(cname, 'w')
        f.write('Module,Option,ID,First name,Last name,Block 1a,Block 1b,Block 2a,Block 2b\n')
        for ID in self.IDs:
            student = self.students[ID]
            outstr  = student.mod[:6] + ','
            if len(student.mod) > 6:
                outstr += 'CMC' + student.mod[7:]
            outstr += ','
            outstr += ID + ','
            outstr += student.fname + ','
            outstr += student.lname + ','
            outstr += student.experiments[0].lecturer + ','
            outstr += student.experiments[1].lecturer + ','
            outstr += student.experiments[2].lecturer + ','
            outstr += student.experiments[3].lecturer
            outstr += '\n'
            f.write(outstr)
        f.close()

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

    def __init__(self, nmax = None):
        self.IDs  = []
        if not nmax is None:
            self.nmax = nmax

    def check(self, student):
        """
        Check if a student can be added to this experiment.
        """
        if len(self.IDs) >= self.nmax:
            return False
        else:
            return student.check(self)

    def add(self, student, expi):
        self.IDs += [student.ID]
        student.experiments[expi] = self

    def __str__(self):
        return self.lecturer + ": " + self.expname

class not_assigned(exp):
    expname   = 'N/A'
    lecturer  = 'N/A'

# Semester 1

class drug_scaff(exp):
    organic   = True
    nmax      = 6
    expname   = 'Scaffolds in drug devel.'
    lecturer  = 'Weaver/Warrington'

class green_cross(exp):
    organic   = True
    nmax      = 12
    expname   = 'Green catalytic cross coupling.'
    lecturer  = 'Malkov/Buckley'

class comp_mod(exp):
    organic   = True
    comp      = True
    nmax      = 8
    expname   = 'Comp. modelling'
    lecturer  = 'Plasser/Kimber'

class prot_lig(exp):
    bio  = True
    nmax = 8
    expname   = 'Protein-ligand binding'
    lecturer  = 'Bellamy-Carter'

class cell_resp(exp): # also Semester 2
    bio  = True
    nmax = 8
    expname   = 'Cell responses'
    lecturer  = 'Pearce'

class thiamine(exp):
    ana  = True
    nmax = 6
    expname   = 'Thiamine content'
    lecturer  = 'Managh'

class hplc(exp):
    ana  = True
    nmax = 4
    expname   = 'HPLC'
    lecturer  = 'Reynolds'

# Semester 2

class xray(exp):
    inorganic = True
    comp      = True
    nmax      = 5
    expname   = 'X-ray'
    lecturer  = 'Elsegood/Smith'

class zeolites(exp):
    inorganic = True
    nmax      = 8
    expname   = 'Zeolites'
    lecturer  = 'Dann/Kondrat'

class fingerprint(exp):
    inorganic = True
    nmax      = 8
    expname   = 'Fingerprinting reagents'
    lecturer  = 'Kelly'

class salen(exp):
    inorganic = True
    nmax      = 6
    expname   = 'M-SALEN complexes'
    lecturer  = 'Fernandez-Mato'

class paracetamol(exp):
    physical  = True
    nmax      = 8
    expname   = 'Paracetamol'
    lecturer  = 'McPherson/Claxton/Heaton'

class tio2(exp):
    physical = True
    nmax     = 8
    expname  = 'Properties of TiO2'
    lecturer = 'Ibraimo-Patia/Heaton'

###

class block:
    def __init__(self, slist, bi, expi):
        self.experiments = []
        self.slist       = slist
        self.assigned    = [False for ID in slist.IDs]
        self.bi          = bi   # Block index
        self.expi        = expi # Experiment index for student

    def assign(self, experiments, module='CMC'):
        for exp in experiments:
            for i, ID in enumerate(self.slist.IDs):
                if self.assigned[i]:
                    continue

                if not module in slist.students[ID].mod:
                    continue

                if exp.check(slist.students[ID]):
                    exp.add(slist.students[ID], self.expi)
                    self.assigned[i] = True
        self.experiments += experiments

    def report(self):
        for exp in self.experiments:
            print("\nExperiment %s (%s)"%(exp, self.bi))
            print("  Number of students: %i / %i"%(len(exp.IDs), exp.nmax))
            # for ID in exp.IDs:
            #     print(self.slist.students[ID])

        print("\n*** Not assigned (%s) ***"%self.bi)
        for i, yn in enumerate(self.assigned):
            if not yn:
                print(self.slist.students[self.slist.IDs[i]])

###

def assign_S1(slist):
    print("\n+++ Starting S1 +++")
    block_1a = block(slist, '1a', 0)
    block_1b = block(slist, '1b', 1)

    # Manual assignments (both blocks)
    # Analytical
    block_1a.assign([thiamine(3), hplc(3)], 'CMC026-004')
    block_1b.assign([thiamine(3), hplc(3)], 'CMC026-004')

    # Assign cell_resp to CMC026-007 for both blocks
    block_1a.assign([cell_resp()], 'CMC026-007')
    block_1b.assign([cell_resp()], 'CMC026-007')

    # CMC027
    block_1a.assign([prot_lig(7)], 'CMC027')
    block_1b.assign([prot_lig(8)], 'CMC027')

    exps_1a = [comp_mod(), drug_scaff(), green_cross()]
    block_1a.assign(exps_1a)
    block_1a.report()

    exps_1b = [comp_mod(), drug_scaff(), green_cross()]
    block_1b.assign(exps_1b)
    block_1b.report()

    #slist.write_csv('S1_assignments.csv')

def assign_S2(slist):
    print("\n+++ Starting S2 +++")
    block_2a = block(slist, '2a', 2)
    block_2b = block(slist, '2b', 3)

    # CMC027
    block_2a.assign([cell_resp(7)], 'CMC027')
    block_2b.assign([cell_resp(7)], 'CMC027')

    # Use custom order to get all slots filled

    block_2a.assign([xray(), zeolites(6), fingerprint(6), salen()])
    block_2b.assign([xray()])

    # Then inorganic
    block_2a.assign([paracetamol(7), tio2(7)])
    block_2b.assign([zeolites(5), fingerprint(5), salen(), paracetamol(8), tio2(8)])

    block_2a.report()
    block_2b.report()

if __name__=='__main__':
    slist = student_list()
    slist.read_csv('CMC029_participants.csv', CMC029_student)
    slist.read_csv('CMC027_participants.csv', CMC027_student)
    slist.read_csv('CMC026-004_participants.csv', CMC026_004_student)
    slist.read_csv('CMC026-007_participants.csv', CMC026_007_student)

    assign_S1(slist)
    assign_S2(slist)
    slist.write_csv('25CMC02x_assignments.csv')
    #slist.report()
