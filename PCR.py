import numpy as np 
import matplotlib.pyplot as plt
import numpy.linalg 
import wget

url= 'http://ftp.cs.wisc.edu/math-prog/cpo-dataset/machine-learn/cancer/WDBC/WDBC.dat'
datos= wget.dowland(url)

print datos 