# -*- coding: utf-8 -*-
# Essa classe SameValue é utilizada quando um valor de um parâmetro é igual a outro, devendo os dois ter
# o mesmo valor, como é o caso da altura do peitoril da janela, que nesse caso vão ser iguais, de ambas
# as janelas. 

import random
import math

class SameValue(object):

    def __init__(self, parameters):
        self.newValue = parameters
        if 'text' in parameters:
            self.text = parameters['text']
        else:
            self.text = ''  

    def getNewValue(self):
        value = str(self.newValue)
        if not self.text:
            return value
        return self.text + value
