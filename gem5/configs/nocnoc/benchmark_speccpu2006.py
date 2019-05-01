
benchmark_speccpu2006_path = '../spec2006/'
binary = '_base.x86_64_sse'

# perlbench
def add_perlbench(options):
    print("Adding Spec CPU 2006 benchmark: perlbench")
    # perlbench -I./lib checkspam.pl 2500 5 25 11 150 1 1 1 1
    benchmark_name = 'perlbench'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_arg = benchmark_path + 'checkspam.pl'
    benchmark_args = "-I./lib " + benchmark_arg + " 2500 5 25 11 150 1 1 1 1"
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.options) == 0:
        setattr(options, 'options', benchmark_args)
    else:
        setattr(options, 'options', getattr(options, 'options') + ';' + benchmark_args)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# bzip2
def add_bzip2(options):
    print("Adding Spec CPU 2006 benchmark: bzip2")
    # bzip2 input/input.source 280
    benchmark_name = 'bzip2'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_arg = benchmark_path + 'input/input.source'
    benchmark_args = benchmark_arg + " 280"
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.options) == 0:
        setattr(options, 'options', benchmark_args)
    else:
        setattr(options, 'options', getattr(options, 'options') + ';' + benchmark_args)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# gcc
def add_gcc(options):
    print("Adding Spec CPU 2006 benchmark: gcc")
    # gcc input/scilab.i -o scilab.s
    benchmark_name = 'gcc'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_arg = benchmark_path + 'input/scilab.i'
    benchmark_opt = benchmark_path + 'scilab.s'
    benchmark_args = benchmark_arg + " -o " + benchmark_opt
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.options) == 0:
        setattr(options, 'options', benchmark_args)
    else:
        setattr(options, 'options', getattr(options, 'options') + ';' + benchmark_args)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# bwaves
def add_bwaves(options):
    print("Adding Spec CPU 2006 benchmark: bwaves")
    # bwaves 
    benchmark_name = 'bwaves'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# gamess
def add_gamess(options):
    print("Adding Spec CPU 2006 benchmark: gamess")
    # gamess < input/triazolium.config
    benchmark_name = 'gamess'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_input = benchmark_path + 'input/triazolium.config'
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.input) == 0:
        setattr(options, 'input', benchmark_input)
    else:
        setattr(options, 'input', getattr(options, 'input') + ';' + benchmark_input)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# mcf
def add_mcf(options):
    print("Adding Spec CPU 2006 benchmark: mcf")
    # mcf inp.in
    benchmark_name = 'mcf'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_arg = benchmark_path + 'inp.in'
    benchmark_args = benchmark_arg
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.options) == 0:
        setattr(options, 'options', benchmark_args)
    else:
        setattr(options, 'options', getattr(options, 'options') + ';' + benchmark_args)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# milc
def add_milc(options):
    print("Adding Spec CPU 2006 benchmark: milc")
    # milc < input/su3imp.in
    benchmark_name = 'milc'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_speccpu2006_path+benchmark_name+'/'+benchmark_name+binary
    benchmark_input = benchmark_path + 'input/su3imp.in'
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.input) == 0:
        setattr(options, 'input', benchmark_input)
    else:
        setattr(options, 'input', getattr(options, 'input') + ';' + benchmark_input)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# zeusmp
def add_zeusmp(options):
    print("Adding Spec CPU 2006 benchmark: zeusmp")
    # zeusmp 
    benchmark_name = 'zeusmp'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# gromacs
def add_gromacs(options):
    print("Adding Spec CPU 2006 benchmark: gromacs")
    # gromacs -silent -deffnm input/gromacs -nice 0
    benchmark_name = 'gromacs'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_arg = benchmark_path + 'input/gromacs'
    benchmark_args = "-silent -deffnm " + benchmark_arg + " -nice 0"
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.options) == 0:
        setattr(options, 'options', benchmark_args)
    else:
        setattr(options, 'options', getattr(options, 'options') + ';' + benchmark_args)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# cactusADM
def add_cactusADM(options):
    print("Adding Spec CPU 2006 benchmark: cactusADM")
    # cactusADM benchADM.par
    benchmark_name = 'cactusADM'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_arg = benchmark_path + 'benchADM.par'
    benchmark_args = benchmark_arg
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.options) == 0:
        setattr(options, 'options', benchmark_args)
    else:
        setattr(options, 'options', getattr(options, 'options') + ';' + benchmark_args)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# leslie3d
def add_leslie3d(options):
    print("Adding Spec CPU 2006 benchmark: leslie3d")
    # leslie3d < leslie3d.in
    benchmark_name = 'leslie3d'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_input = benchmark_path + 'leslie3d.in'
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.input) == 0:
        setattr(options, 'input', benchmark_input)
    else:
        setattr(options, 'input', getattr(options, 'input') + ';' + benchmark_input)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# namd
def add_namd(options):
    print("Adding Spec CPU 2006 benchmark: namd")
    # namd --input input/namd.input --iterations 38 --output namd.out
    benchmark_name = 'namd'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_arg = benchmark_path + 'input/namd.input'
    benchmark_opt = benchmark_path+'namd.out'
    benchmark_args = "--input " + benchmark_arg + " --iterations 38 --output " + benchmark_opt
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.options) == 0:
        setattr(options, 'options', benchmark_args)
    else:
        setattr(options, 'options', getattr(options, 'options') + ';' + benchmark_args)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# gobmk
def add_gobmk(options):
    print("Adding Spec CPU 2006 benchmark: gobmk")
    # gobmk --quiet --mode gtp < input/score2.tst
    benchmark_name = 'gobmk'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_args = "--quiet --mode gtp"
    benchmark_input = benchmark_path + 'input/score2.tst'
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.options) == 0:
        setattr(options, 'options', benchmark_args)
    else:
        setattr(options, 'options', getattr(options, 'options') + ';' + benchmark_args)
    if len(options.input) == 0:
        setattr(options, 'input', benchmark_input)
    else:
        setattr(options, 'input', getattr(options, 'input') + ';' + benchmark_input)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# dealII
def add_dealII(options):
    print("Adding Spec CPU 2006 benchmark: dealII")
    # dealII 23
    benchmark_name = 'dealII'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_args = "23"
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.options) == 0:
        setattr(options, 'options', benchmark_args)
    else:
        setattr(options, 'options', getattr(options, 'options') + ';' + benchmark_args)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# soplex
def add_soplex(options):
    print("Adding Spec CPU 2006 benchmark: soplex")
    # soplex -s1 -e -m45000 pds-50.mps
    benchmark_name = 'soplex'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_arg = benchmark_path + 'pds-50.mps'
    benchmark_args = "-s1 -e -m45000 " + benchmark_arg
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.options) == 0:
        setattr(options, 'options', benchmark_args)
    else:
        setattr(options, 'options', getattr(options, 'options') + ';' + benchmark_args)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# povray
def add_povray(options):
    print("Adding Spec CPU 2006 benchmark: povray")
    # povray SPEC-benchmark-ref.ini
    benchmark_name = 'povray'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_arg = benchmark_path + 'SPEC-benchmark-ref.ini'
    benchmark_args = benchmark_arg
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.options) == 0:
        setattr(options, 'options', benchmark_args)
    else:
        setattr(options, 'options', getattr(options, 'options') + ';' + benchmark_args)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# calculix
def add_calculix(options):
    print("Adding Spec CPU 2006 benchmark: calculix")
    # calculix -i hyperviscoplastic
    benchmark_name = 'calculix'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_arg = benchmark_path + 'hyperviscoplastic'
    benchmark_args = "-i " + benchmark_arg
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.options) == 0:
        setattr(options, 'options', benchmark_args)
    else:
        setattr(options, 'options', getattr(options, 'options') + ';' + benchmark_args)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# hmmer
def add_hmmer(options):
    print("Adding Spec CPU 2006 benchmark: hmmer")
    # hmmer input/nph3.hmm input/swiss41
    benchmark_name = 'hmmer'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_arg_1 = benchmark_path + 'input/nph3.hmm'
    benchmark_arg_2 = benchmark_path + 'input/swiss41'
    benchmark_args = benchmark_arg_1 + " " + benchmark_arg_2
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.options) == 0:
        setattr(options, 'options', benchmark_args)
    else:
        setattr(options, 'options', getattr(options, 'options') + ';' + benchmark_args)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# sjeng
def add_sjeng(options):
    print("Adding Spec CPU 2006 benchmark: sjeng")
    # sjeng input/ref.txt
    benchmark_name = 'sjeng'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_arg = benchmark_path + 'input/ref.txt'
    benchmark_args = benchmark_arg
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.options) == 0:
        setattr(options, 'options', benchmark_args)
    else:
        setattr(options, 'options', getattr(options, 'options') + ';' + benchmark_args)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# GemsFDTD
def add_GemsFDTD(options):
    print("Adding Spec CPU 2006 benchmark: GemsFDTD")
    # GemsFDTD 
    benchmark_name = 'GemsFDTD'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# libquantum
def add_libquantum(options):
    print("Adding Spec CPU 2006 benchmark: libquantum")
    # libquantum 1397 8
    benchmark_name = 'libquantum'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_args = "1397 8"
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.options) == 0:
        setattr(options, 'options', benchmark_args)
    else:
        setattr(options, 'options', getattr(options, 'options') + ';' + benchmark_args)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# h264ref
def add_h264ref(options):
    print("Adding Spec CPU 2006 benchmark: h264ref")
    # h264ref -d input/sss_encoder_main.cfg
    benchmark_name = 'h264ref'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_arg = benchmark_path + 'input/sss_encoder_main.cfg'
    benchmark_args = "-d " + benchmark_arg
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.options) == 0:
        setattr(options, 'options', benchmark_args)
    else:
        setattr(options, 'options', getattr(options, 'options') + ';' + benchmark_args)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# lbm
def add_lbm(options):
    print("Adding Spec CPU 2006 benchmark: lbm")
    # lbm 3000 reference.dat 0 0 100_100_130_ldc.of
    benchmark_name = 'lbm'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_arg = benchmark_path + '100_100_130_ldc.of'
    benchmark_args = "3000 reference.dat 0 0 " + benchmark_arg
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.options) == 0:
        setattr(options, 'options', benchmark_args)
    else:
        setattr(options, 'options', getattr(options, 'options') + ';' + benchmark_args)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# omnetpp
def add_omnetpp(options):
    print("Adding Spec CPU 2006 benchmark: omnetpp")
    # omnetpp omnetpp.ini
    benchmark_name = 'omnetpp'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_arg = benchmark_path + 'omnetpp.ini'
    benchmark_args = benchmark_arg
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.options) == 0:
        setattr(options, 'options', benchmark_args)
    else:
        setattr(options, 'options', getattr(options, 'options') + ';' + benchmark_args)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# astar
def add_astar(options):
    print("Adding Spec CPU 2006 benchmark: astar")
    # astar rivers.cfg
    benchmark_name = 'astar'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_arg = benchmark_path + 'rivers.cfg'
    benchmark_args = benchmark_arg
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.options) == 0:
        setattr(options, 'options', benchmark_args)
    else:
        setattr(options, 'options', getattr(options, 'options') + ';' + benchmark_args)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# wrf
def add_wrf(options):
    print("Adding Spec CPU 2006 benchmark: wrf")
    # wrf 
    benchmark_name = 'wrf'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# sphinx
def add_sphinx(options):
    print("Adding Spec CPU 2006 benchmark: sphinx")
    # sphinx_livepretend ctlfile . input/args.an4
    benchmark_name = 'sphinx_livepretend'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_arg_1 = benchmark_path + 'ctlfile'
    benchmark_arg_2 = benchmark_path + 'input/args.an4'
    benchmark_args = benchmark_arg_1 + " " + benchmark_path + " " + benchmark_arg_2
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.options) == 0:
        setattr(options, 'options', benchmark_args)
    else:
        setattr(options, 'options', getattr(options, 'options') + ';' + benchmark_args)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# xalancbmk
def add_xalancbmk(options):
    print("Adding Spec CPU 2006 benchmark: xalancbmk")
    # xalancbmk -v t5.xml xalanc.xsl
    benchmark_name = 'Xalan'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_arg_1 = benchmark_path + 't5.xml'
    benchmark_arg_2 = benchmark_path + 'xalanc.xsl'
    benchmark_args = "-v " + benchmark_arg_1 + " " +  benchmark_arg_2
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.options) == 0:
        setattr(options, 'options', benchmark_args)
    else:
        setattr(options, 'options', getattr(options, 'options') + ';' + benchmark_args)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# tonto
def add_tonto(options):
    print("Adding Spec CPU 2006 benchmark: tonto")
    # tonto 
    benchmark_name = 'tonto'
    benchmark_path = benchmark_speccpu2006_path + benchmark_name + '/'
    benchmark_exec = benchmark_path + benchmark_name + binary
    benchmark_output = benchmark_path + 'ece752project.out'
    if len(options.cmd) == 0:
        setattr(options, 'cmd', benchmark_exec)
    else:
        setattr(options, 'cmd', getattr(options, 'cmd') + ';' + benchmark_exec)
    if len(options.output) == 0:
        setattr(options, 'output', benchmark_output)
    else:
        setattr(options, 'output', getattr(options, 'output') + ';' + benchmark_output)

# All
def add_all(options):
    print("Adding all Spec CPU 2006 benchmarks")
    add_perlbench(options)
    add_bzip2(options)
    add_gcc(options)
    add_bwaves(options)
    add_gamess(options)
    add_mcf(options)
    add_milc(options)
    add_zeusmp(options)
    add_gromacs(options)
    add_cactusADM(options)
    add_leslie3d(options)
    add_namd(options)
    add_gobmk(options)
    add_dealII(options)
    add_soplex(options)
    add_povray(options)
    add_calculix(options)
    add_hmmer(options)
    add_sjeng(options)
    add_GemsFDTD(options)
    add_libquantum(options)
    add_h264ref(options)
    add_lbm(options)
    add_omnetpp(options)
    add_astar(options)
    add_wrf(options)
    add_sphinx(options)
    add_xalancbmk(options)
    add_tonto(options)

