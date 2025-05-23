#!/usr/bin/env python3
"""
Extract data from an OpenMolcas computation on Europium.
"""

# This could be done as user input
iname='molcas.log'
refstate = 50
oscfac = 1.E7
xmax = 2.9
xmin = 2.0
xshift = 0.0 #0.4
width = 0.015
oformat='% 10.5f'
prop_list = ['J', 'f', 'f_ED', 'f_VD', 'f_sec', 'r_V', 'r_mix', 'f_ex']
do_plot = True
###

def parse_tprop(prop, rfile, states, fac=1):
    for i in range(15):
        line = next(rfile)
    while(True):
        line = next(rfile)
        if '---' in line:
            break
        elif 'tensor' in line:
            continue
        words = line.split()
        ind2 = int(words[1])
        if ind2 == refstate:
            ind = int(words[0]) - 1
            try:
                states[ind][prop] = float(words[2]) * fac
            except ValueError:
                states[ind][prop] = -1.

states = [{} for ind in range(refstate)]
for state in states:
    state['f']     = 0.
    state['f_ED']  = 0.
    state['f_VD']  = 0.
    state['f_sec'] = 0.
    state['f_ex']  = 0.
    state['r_V']   = 0.
    state['r_mix'] = 0.

rfile = open(iname, 'r')

while(True):
    line = next(rfile)

    if 'Eigenvalues of complex Hamiltonian' in line:
        for i in range(5):
            line = next(rfile)
        for i in range(refstate-1):
            line = next(rfile)
            words = line.split()
            ind = int(words[0]) - 1
            states[ind]['en'] = float(words[2])
            try:
                states[ind]['J'] = float(words[4])
            except:
                states[ind]['J'] = -1.
        refen = float(next(rfile).split()[2])

    elif 'Dipole transition strengths (SO states)' in line:
        parse_tprop('f_ED', rfile, states, oscfac)

    elif 'Velocity transition strengths (SO states)' in line:
        parse_tprop('f_VD', rfile, states, oscfac)

    elif '++ Circular Dichroism - velocity' in line and 'SO states' in line:
        parse_tprop('r_V', rfile, states, 1.E3)

    elif '++ Circular Dichroism - mixed' in line and 'SO states' in line:
        parse_tprop('r_mix', rfile, states, 1.E3)

    elif 'Total transition strengths for the second-order expansion of the wave vector (SO states)' in line:
        parse_tprop('f_sec', rfile, states, oscfac)

    elif 'Isotropic transition moment strengths (SO states)' in line:
        parse_tprop('f_ex', rfile, states, oscfac)

    elif 'I/O STATISTICS' in line:
        break

# Write the file in TheoDORE format

hstr = 'state    dE(eV)'
for prop in prop_list:
    hstr += '%8s  '%prop
ostr  = hstr + "\n"
ostr += len(hstr) * '-' + "-\n"    

J = 0
mJ = 0
for state in states[:refstate-1]:
    ostr += "J%i%+i  "%(J, mJ)
    dE = refen - state['en'] - xshift
    ostr += " % 9.5f"%dE
    state['f'] = state['f_ED'] + state['f_sec']

    for prop in prop_list:
        ostr += oformat%(state[prop])
    ostr += '\n'

    if mJ == J:
        J +=  1
        mJ = -J
    else:
        mJ += 1

open('gMEu_summ.txt', 'w').write(ostr)


# Run TheoDORE for the plots
if do_plot:
    from theodore.actions import spectrum
    import matplotlib

    matplotlib.use('Agg')

    sopt = spectrum.spec_options('spectrum.in')
    sopt['ana_files'] = ['gMEu_summ.txt']
    sopt.spec = spectrum.spectrum(200,xmax,xmin,width,1,2,['gMEu_summ.txt'])
    sopt['weight'] = 1
    sopt['restr'] = False
    sopt['normalize'] = False

    sopt.make_spec(ylabel = 'Osc. strength x $10^7$')
