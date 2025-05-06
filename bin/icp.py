#!/usr/bin/env python3
"""
Take the input directories for a set of jobs (or one job).
"""
import os,sys,shutil,glob

nocopy = ['input', 'JOB_AD', 'JOB_NAD']

def vcopy(src, dst, retcode=0):
    print('Copying %s -> %s'%(src, dst))
    try:
        shutil.copy(src, dst)
    except:
        print("... failed")
        retcode=1

def icp_rec(frdir,todir,maxrec=0,cpfiles=[],irec=0):
    """
    Recursive function that checks if the directory has subdirectories or if it contains the "input" directory.
    """
    sbdirs = os.listdir(frdir)
    if 'input' in sbdirs:
        print('* input found, copying ' + os.path.join(frdir,'input') + ' to ' + todir)
        #if not os.path.isdir(todir):
        # makedirs, cp * ... ?
        #shutil.copytree(os.path.join(frdir,'input'),todir)
        os.makedirs(todir)
        for filn in glob.glob(os.path.join(frdir,'input','*')):
            shutil.copy(filn,todir)

        for cpfile in cpfiles:
              shutil.copy(cpfile,todir)
        if 'tm' in flags:
              print('copying coord and mos')
              shutil.copy(os.path.join(frdir,'coord'),todir)
              shutil.copy(os.path.join(frdir,'mos'),todir)
        if 'col' in flags:
              vcopy(os.path.join(frdir,'MOCOEFS/mocoef_mc.sp'),os.path.join(todir,'mocoef'))
              vcopy(os.path.join(frdir,'geom'),os.path.join(todir,'geom'))
        if 'work' in flags:
              vcopy(os.path.join(frdir,'WORK'),os.path.join(todir,'WORK'))
        if 'molc' in flags:
              vcopy(os.path.join(frdir,'MOLCAS.RasOrb'),os.path.join(todir,'INPORB'))
              for RO in glob.glob(os.path.join(frdir,'*.RasOrb')):
                  vcopy(RO, todir)
        if 'qc' in flags:
              retcode = 0
              vcopy(os.path.join(frdir,'molecule'),os.path.join(todir,'coord.qcin'), retcode)
              if retcode:
                 print('qchem.out -> coord.qcin')
                 from theodore import lib_struc
                 struc = lib_struc.structure()
                 struc.read_file(file_path="%s/qchem.out"%frdir, file_type='qcout')
                 struc.make_coord_file(file_path="%s/coord.qcin"%todir,file_type='qcin')
        if 'sharc' in flags:
               print(' Copying QM ...')
               shutil.copytree(os.path.join(frdir,'QM'),os.path.join(todir,'QM'))
#    else:
#       if not os.path.exists(todir): os.mkdir(todir) # created even if there is no subdirectory input!
              
    for sbdir in sbdirs:
       if os.path.isdir(os.path.join(frdir,sbdir)) and not sbdir in nocopy:
           if irec < maxrec and sbdir!='RUNDIR':
               icp_rec(os.path.join(frdir,sbdir),os.path.join(todir,sbdir),maxrec,cpfiles,irec+1)

if __name__=='__main__':
    src=''
    cpall = False
    flags = []
    cpfiles = []
    maxrec=1

    args = sys.argv[1:]
    while len(args) > 0:
       arg = args.pop(0)
       if arg=='-tm':
          flags.append('tm')
       elif arg=='-col':
          flags.append('col')
       elif arg=='-work':
          flags.append('work')
       elif arg=='-molc':
          flags.append('molc')
       elif arg=='-qc':
          flags.append('qc')
       elif arg=='-sharc':
           flags.append('sharc')
       elif arg=='-cp':
          cpfiles.append(args.pop(0))
       elif arg=='-cpall':
          # copy all files in todir
          cpall = True
       elif arg=='-maxrec':
          maxrec=int(args.pop(0))
       else:
          if src=='':
             src = arg
          else:
             dst = arg

    if cpall:
       for file in os.listdir(dst):
         if not os.path.isdir(os.path.join(dst,file)):
           cpfiles.append(os.path.join(dst,file))
    icp_rec(src,dst,maxrec=maxrec,cpfiles=cpfiles)
