from openmdao.main.api import Component
from openmdao.main.datatypes.api import Float
from math import sin, cos
from numpy import array

class ExampleComp(Component):

    # Inputs
    x = Float(0., iotype="in")
    y = Float(0., iotype="in")

    # Outputs
    f = Float(0., iotype="out")
    g = Float(0., iotype="out")

    def list_deriv_vars(self):
        return (('x', 'y',), ('f', 'g'))

    def provideJ(self):
        # return array([[2*self.x, cos(self.y)],
        #               [3*self.x**2, 0.0]])
        pass

    def apply_deriv(self, arg, result):
        result["f"] += 2*self.x*arg["x"]
        result["f"] += cos(self.y)*arg["y"]
        result["g"] += 3*self.x**2 * arg["x"]

    def apply_derivT(self, arg, result):
        result["x"] += 2*self.x*arg["f"]
        result["x"] += 3*self.x**2 * arg["g"]
        result["y"] += cos(self.y)*arg["f"]

    def execute(self):
        self.f = self.x**2 + sin(self.y)
        self.g = self.x**3

if __name__ == "__main__":

    c = ExampleComp()
    c.check_gradient(mode="adjoint")
    c.run()