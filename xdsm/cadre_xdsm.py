from XDSM import XDSM

opt = 'Optimization'
dat = 'DataInter'

x = XDSM()
x.addComp('Optimizer', 'Analysis', 'Optimizer')
x.addComp('Orbit', opt, 'Orbit Dynamics')
x.addComp('Attitude', opt, 'Attitude Dynamics')
x.addComp('Solar', opt, 'Cell Illumination')
x.addComp('Thermal', opt, 'Temperature')
x.addComp('Electrical', opt, 'Solar Power')
x.addComp('Battery', opt, 'Energy Storage')
x.addComp('Comm', opt, 'Communication')

x.addDep('Optimizer', 'Battery', dat, 'Constraints')
x.addDep('Optimizer', 'Comm', dat, 'Data downloaded')
x.addDep('Attitude', 'Optimizer', dat, 'Roll angle')
x.addDep('Solar', 'Attitude', dat, 'Attitude')
x.addDep('Solar', 'Orbit', dat, 'Position')
x.addDep('Thermal', 'Solar', dat, 'Exp. area')
x.addDep('Thermal', 'Optimizer', dat, 'Comm power')
x.addDep('Electrical', 'Solar', dat, 'Exp. area')
x.addDep('Electrical', 'Optimizer', dat, 'Panel current')
x.addDep('Electrical', 'Thermal', dat, 'Temperature')
x.addDep('Battery', 'Electrical', dat, 'Solar power')
x.addDep('Battery', 'Thermal', dat, 'Temperature')
x.addDep('Battery', 'Attitude', dat, 'Actuator power')
x.addDep('Battery', 'Optimizer', dat, 'Comm power')
x.addDep('Comm', 'Attitude', dat, 'Attitude')
x.addDep('Comm', 'Orbit', dat, 'Position')
x.addDep('Comm', 'Optimizer', dat, 'Comm power')

x.write('cadre_xdsm',True)