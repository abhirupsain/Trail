"""
Example script for the topics
 * regression and interpolation
 * splines
"""

import numpy as np
import scipy as sc
import pylab as pl

# adapted from source: http://www.scipy.org/Cookbook/LinearRegression

#####################################################

# Regression

#####################################################

# Generation of sample data (linear function with noise)
n = 10
t = np.linspace(-5, 5, n) # independent variable

# parameters of nominal data
a = 0.02
b = 0.8
c = -1

# Calculate nominal data
# x = np.polyval([a, b, c], t) # alternatively: x = a*t+b
x = a*t**2 + b*t + c # alternativ: np.polyval([a, b, c], t)

# Initialize random number generator -> Cause "reproducible randomness".
np.random.seed(3)
# add noise to nominal data
x_noise = x + 0.6*np.random.randn(n)

# linear regressison with polyfit (polynomial of degree 1 -> 2 coefficients: c1, c0)
(c1, c0) = np.polyfit(t, x_noise, 1)
xr = np.polyval([c1, c0], t) # Evaluation of the polynomial with respective coefficients

# quadratic regression (polynomial of degree 2 -> 3 coefficients: c2, c1, c0)
c2, c1, c0 = np.polyfit(t, x_noise, 2)
xqr = np.polyval([c2, c1, c0], t)


# 1st visualization:

# image size is expected in inches -> scaling factor
mm = 1./25.4 # mm to inch
fs = [90*mm, 60*mm]
pl.figure(figsize=fs) # force custom image size

pl.plot(t, x_noise, 'ro') # data
pl.savefig('bsp3_1.pdf')
pl.plot(t, xr, lw=2) # lw = linewidth
pl.savefig('bsp3_2.pdf')
pl.plot(t, xqr, 'g--', lw=2)
pl.savefig('bsp3_3.pdf')


#####################################################

# Interpolation

#####################################################



# see also:
# - http://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html
# https://docs.scipy.org/doc/scipy/reference/reference/generated/scipy.interpolate.interp1d.html#scipy.interpolate.interp1d

# Normally all imports should be at the beginning of a .py file.
# From this is deviated here, so that one sees that one needs this not until here:

from scipy.interpolate import interp1d

func1 = interp1d(t, x_noise) # `kind='linear'` is default
func0 = interp1d(t, x_noise, kind='nearest') # order 0 is 'nearest' (neighbor)
func3 = interp1d(t, x_noise, kind=3) # cubic spline

t_highres = np.linspace(t[0], t[-1], 100)

xi0 = func0(t_highres)
xi1 = func1(t_highres)
xi3 = func3(t_highres)

# 2nd visualization (new figure):
pl.figure(figsize=fs) # # force custom image size

pl.plot(t, x_noise, 'ro',) # data
pl.plot(t_highres, xi0, 'bo', ms=2)
pl.plot(t_highres, xi1, 'g', lw=1.3)
pl.savefig('bsp3_4.pdf')
pl.plot(t_highres, xi3, 'k-', lw=2)
pl.savefig('bsp3_5.pdf')


#####################################################

# "Smoothing Spline" (smoothed spline, i.e. piecewise polynomial function)
# see also:
# - http://www.scipy.org/Cookbook/Interpolation
# - https://docs.scipy.org/doc/scipy/reference/reference/generated/scipy.interpolate.splrep.html#scipy.interpolate.splrep

#####################################################


from scipy.interpolate import splrep, splev
# spline parameters:
s = 0.4 # Smoothing parameter
k = 2 # spline order

# create spline objects
splobj1 = splrep(t, x_noise, s=s, k=k) # smoothed
splobj2 = splrep(t, x_noise, s=0.0, k=k) # unsmoothed (s=0)

# Determine values of the independent variables with high resolution
t_highres = np.linspace(t[0], t[-1], 100)

# evaluate spline objects for high resolution t-values
xspline = splev(t_highres, splobj1)
xspline2 = splev(t_highres, splobj2)


# 3rd. visualization (new figure):
pl.figure(figsize=fs) # # force custom image size:

pl.plot(t, x_noise, 'ro') # data
pl.plot(t_highres, xspline, lw=1.5)
pl.savefig('bsp3_6.pdf')
pl.plot(t_highres, xspline2, 'g--', lw=2)
pl.savefig('bsp3_7.pdf')

pl.show()
