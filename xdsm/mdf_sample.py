from XDSM import XDSM

opt = 'Optimization'
anl = 'Analysis'
dat = 'DataInter'

x = XDSM()
x.addComp('Optimizer', opt, 'Optimizer')
x.addComp('Solver', 'MDA', 'Solver')
x.addComp('A', anl, 'A')
x.addComp('B', anl, 'B')


x.addDep('A', 'Optimizer', dat, 'x', True)
x.addDep('Solver', 'B', dat, 'y2')
x.addDep('Solver', 'A', dat, 'y1')
x.addDep('A', 'Solver', dat, 'y2')
x.addDep('B', 'Solver', dat, 'y1')
x.addDep('Optimizer','B', dat, 'z')


x.write('mdf_sample',True)
