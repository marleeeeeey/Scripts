
# coding: utf-8

from IPython import get_ipython
get_ipython().magic('matplotlib inline')

import sys
sys.path
sys.path.append('C:\\Users\\k22\\Documents\\YandexShcool\\shared')
import imp
import my_imports
imp.reload(my_imports)   # перезагрузка модуля в любом случае
from my_imports import *

my_module.run_experiment()



