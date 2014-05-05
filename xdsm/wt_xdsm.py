from XDSM import XDSM

opt = 'Optimization'
dat = 'DataInter'

x = XDSM()
x.addComp('Optimizer', 'Analysis', 'Optimizer')
x.addComp('rotor', opt, 'Rotor')
x.addComp('hub', opt, 'Hub')
x.addComp('nacelle', opt, 'Nacelle')
x.addComp('tower', opt, 'Tower')
x.addComp('deflection', opt, 'Tower Strike')
x.addComp('aep_a', opt, 'Annual Energy Prod.')
x.addComp('opex_a', opt, 'Op. Expenses')
x.addComp('tcc_a', opt, 'Turb. Capital Cost')
x.addComp('bos_a', opt, 'Balance of Station')
x.addComp('fin_a', opt, 'Financial')


x.addDep('tcc_a', 'rotor', dat, '$m_{blade}$, $P_{rated}$')
x.addDep('tcc_a', 'hub', dat, '$m_{hub}$')
x.addDep('tcc_a', 'nacelle', dat, '$m_{nacelle}$')
x.addDep('tcc_a', 'tower', dat, '$m_{tower}$')

x.addDep('bos_a', 'rotor', dat, '\TwolineComponent{2.5cm}{$m_{blade}$, $P_{rated}$}{$d_{rotor}$}')
x.addDep('bos_a', 'tcc_a', dat, "$\$_{tcc}$")

x.addDep('opex_a', 'rotor', dat, '$P_{rated}$')
x.addDep('opex_a', 'aep_a', dat, '$AEP_{net}$')

x.addDep('aep_a', 'rotor', dat, '$AEP$')

x.addDep('hub', 'rotor', dat, '$m_{blade}$, $d_{rotor}$, $M_{root}$')

x.addDep('nacelle', 'rotor', dat, '\ThreelineComponent{2.3cm}{$m_{blade}, P_{rated}}{d_{rotor}, Q_{rotor}$}{$T_{rotor}, \Omega_{rated}$}')

x.addDep('tower', 'rotor', dat, '\ThreelineComponent{3.2cm}{$V_{rated}, V_{extreme}$}{$H, tilt, m_{rotor}, I_{rotor}$}{$Q_{rotor}, T_{rotor}$}')
x.addDep('tower', 'hub', dat, '$m_{hub}, I_{hub}$')

x.addDep('tower', 'nacelle', dat, '$m_{nacelle}, I_{nacelle}$')

x.addDep('deflection', 'rotor', dat, '$L_{blade}, precone, tilt$')
x.addDep('deflection', 'nacelle', dat, '$L_{nac}, H_{nac}$')
x.addDep('deflection', 'tower', dat, '$z_{waist}, d_{tower}$')

x.addDep('fin_a', 'tcc_a', dat, "$\$_{tcc}$")
x.addDep('fin_a', 'bos_a', dat, "$\$_{bos}$")
x.addDep('fin_a', 'opex_a', dat, "$\$_{opex}$")
x.addDep('fin_a', 'aep_a', dat, "$AEP$")



x.addDep('rotor', 'Optimizer', dat, "\TwolineComponent{3.0cm}{$c,\\theta, t_{sc}, t_{te}, \lambda_2$}{$\lambda_{max}, L_{blade}, H$}")
x.addDep('nacelle', 'Optimizer', dat, "$L_{shaft}, h_{beam}$")
x.addDep('tower', 'Optimizer', dat, "$d, t, z_{waist}$")


x.addDep('Optimizer', 'rotor', dat, "\TwolineComponent{2.8cm}{$\\delta_{rotor}, \epsilon, \Omega, \epsilon^*_{rotor}$}{$damage_{rotor}$}")
x.addDep('Optimizer', 'nacelle', dat, "$\\sigma_{nacelle}, \epsilon, \\theta_{lss}$")
x.addDep('Optimizer', 'deflection', dat, "$\\delta_{max}$")
x.addDep('Optimizer', 'tower', dat, "\TwolineComponent{3.0cm}{$d_{top}, d_{base}, \sigma_{tower}$}{$\sigma^*_{tower}, damage_{tower}$}")
x.addDep('Optimizer', 'fin_a', dat, "$COE$")


x.write('wt_xdsm',True)