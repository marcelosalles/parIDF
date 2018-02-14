# -*- coding: utf-8 -*-
# Essa classe SameValue é utilizada quando um valor de um parâmetro é igual a outro, devendo os dois ter
# o mesmo valor, como é o caso da altura do peitoril da janela, que nesse caso vão ser iguais, de ambas
# as janelas.

import random
import math

class Mathematical(object):

    def __init__(self, parameters):
        a = float(parameters['Shading:Overhang:Projection:Zn1_par1_brise:Depth as Fraction of Window/Door Height {dimensionless}']);
        h = float(parameters['value'])
        self.newValue = ((h - 0.75) * a)/4.9

    def getNewValue(self):
        return str(self.newValue)
