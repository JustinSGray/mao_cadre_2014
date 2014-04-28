from xdsm import XDSM

sample = XDSM()

sample.addComp('A','Optimization','A')
sample.addComp('B','Analysis','A')


sample.addDep('A','B','DataInter','x')
sample.addDep('B','A','DataIO','y')


sample.write('sample_xdsm', True)