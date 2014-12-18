from numpy import *
from scipy import loadtxt, optimize, constants
from scipy.odr import *
import matplotlib.pyplot as plt

data = loadtxt('scripttsv.tsv', skiprows=1)
