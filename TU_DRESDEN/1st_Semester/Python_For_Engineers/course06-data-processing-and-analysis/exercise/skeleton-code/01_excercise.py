import numpy as np
import scipy as sc
from scipy.interpolate import griddata, interp2d
import sys

import matplotlib.pyplot as plt



# replace `XYZ` by some meaningful code

# to avoid runtime errors use `sys.exit()`
# (and do not forget to move that line further down as you proceed)



######## task 1

data = np.loadtxt('../data/measurementdata.dat')
tt, xx1, uu, ii = data.T # unpack 2d array with 4 collumns

# preview data
if 0: #( 0 -> do not execute; 1 -> execute this block then exit program)
    plt.plot(tt, xx)
    plt.title("displacement")
    plt.figure()
    plt.plot(tt, uu)
    plt.title("voltage")
    plt.figure()
    plt.plot(tt, ii)
    plt.title("current")
    plt.show()
    sys.exit()


######## task 2

# adapt the sign of the current
ii = ii*np.sign(uu)

# Note: if voltage == 0 then sign = 0, thus current is also set to 0


# Visualize data
if 0: #( 0 -> dont execute this block, 1 -> execute this block)
    plt.plot(tt, ii)
    plt.title("current")
    plt.show()
    sys.exit()


######## task 3

# goal: find out indices of voltage pulses

# calculate the derivative
udiff = np.diff(uu)

# create array for all indices
all_indices = np.arange(len(uu) - 1)


# select those indices where the derivative does not vanish (using boolean indexing)
# (if this is hard to understand have a look to the array idcs = (udiff != 0)
idcs = (udiff != 0)
change_indices = all_indices[XYZ]

if 0:
    # plot the derivative (x-axis: all_indices, automatically chosen)
    plt.plot(udiff)
    # plot red circles at those index values which are in `change_indices`
    plt.plot(change_indices, change_indices*0, "ro")
    plt.title("voltage diff")
    plt.show()
    sys.exit()


# Prevent the possibility that a "half pulse" at the end is also detected.
# if the length is an odd number (modulo-two calculation != 0), then drop the last value
if len(change_indices) % 2 == 1:
    change_indices = change_indices[XYZ]  # omit last value



# Until now the indices are one after the other
# We always want two in one line
# first column: pulse start index, second column: pulse end index)
XYZ = XYZ.reshape(-1, 2) # -1  means: "choose the row number such that it fits"

# increase all values in the first column by one, because the index refers to the
# last value before the jump.

XYZ[XYZ, XYZ] += 1

print(XYZ)


######### task 4

# Create histogram from 4 "current block" (index=3):
if 0:
    # unpack the 4. row into two scalar values
    idx1, idx2 = change_indices[3, :]

    plt.hist(XYZ[XYZ])
    plt.show()
    sys.exit()


######### task 5

# Take the average of the current

ii_mean = 0*ii # # create new ('empty') array


# Iterate over change_indices line by line
for XYZ, XYZ in change_indices:
    XYZ[XYZ] = np.mean(XYZ) # Calculate mean values (and save them)


if 0:

    plt.plot(tt, XYZ) # current-values with noise
    plt.plot(tt, XYZ) # mean values of the current

    plt.show()
    sys.exit()

####### task 6

if 0:
    plt.figure()

    start_idcs = XYZ[:, 0] # first column: indices where a block (ore section) starts

    # Determine a voltage-current value pair for each current block:
    ii2 = ii_mean[XYZ]
    uu2 = uu[XYZ]

    plt.plot(uu2, ii2, 'bx', ms=7)  # big blue crosses (x)

    a1, a0 =  sc.polyfit(XYZ, XYZ, XYZ)  # lineare regression

    plt.plot(XYZ, XYZ, 'g-')  # Evaluate and plot polynomial (straight line equation)
    # alternatively use: sc.polyval [a1, a0]

    print("conductivity (inverse resistance):", a1)
    print("current offset", a0)

    plt.show()
    sys.exit()



######### task 7

# step size of the time array (assuming it starts at 0)
dt = tt[1]

# calc velocity and acceleration via np.diff
xd = XYZ
xdd = XYZ


######### task 8
if 0:
    for idx1, idx2 in change_indices:

        # now we want only positive voltage pulses
        # if u< 0: continue with next loop cycle
        if uu[idx1] < 0:
            continue  # this continues with the next iteration (omitting the plot)

        plt.plot(XYZ[idx1:idx2-1], XYZ[XYZ])

    plt.show()
    sys.exit()


######### task 9

# see
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.griddata.html

# We need the input data in the following format:

# points (Shape = (N, 2)) Each line is a point in the velocity vs. speed diagram.
# voltage (len = N), the voltage value belonging to each point

# We work first with lists (can be concatenated more easily).
# At the end we convert the lists into arrays.


points_vel = []
points_acc = []
voltage = []

for idx1, XYZ in change_indices:

    # ignore negative values
    if uu[idx1] < 0:
        continue

    points_vel += list(XYZ)
    points_acc += list(XYZ)

    # List of the appropriate length in which all elements have the same value.
    # namely the matching voltage value
    length = (idx2-1-idx1)
    voltage += [XYZ[XYZ]]*length


# Workaround for interpolation:
# Add pseudo-measurement values at the boundary to avoid nan-values ("not-a-number").
# Assumption: at 3V still (almost) nothing moves.
points_vel = [0, 0,  0,  7,  7] + points_vel
points_acc = [0, 3, 14,  0, 14] + points_acc
voltage =    [3, 3, 12, 12, 12] + voltage


# Pack lists together as arrays:
points = np.array([points_vel, points_acc]).T
voltage = np.array(voltage)


xd_max = max(points[:, 0])
xdd_max = max(points[:, 1])
N_grid = 100

# Create regular grid
grid_v_arr1d = np.linspace(0, xd_max, N_grid)
grid_a_arr1d = np.linspace(0, xdd_max, N_grid)

# create 2d arrays, see https://docs.scipy.org/doc/numpy/reference/generated/numpy.meshgrid.html
vv, aa = np.meshgrid(grid_v_arr1d, grid_a_arr1d)


# Perform interpolation
interp_voltage = griddata(points, voltage, (vv, aa) )

# eleminate nan values at the boundary
interp_voltage[:, 0] = interp_voltage[:, 1]  # first column := second column
interp_voltage[0, :] = interp_voltage[1, :]  # first row:= second row

if 0:
    # Display 2d array graphically, see https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html
    plt.figure()
    plt.imshow(interp_voltage,
               extent=(0, xd_max, 0, xdd_max), origin='lower', interpolation='nearest')
    plt.xlabel("velocity")
    plt.ylabel("acceleration")
    plt.colorbar(label="voltage")
    plt.title("Relationship between velocity and acceleration \n"
              "as a function of voltage.")

    # Draw the curves again
    for idx1, idx2 in change_indices:

        if uu[idx1] < 0:
            continue

        plt.plot(xd[idx1:idx2-1], xdd[idx1:idx2-1], 'k-')

    # Explanation: Each curve corresponds to a series of measurements.
    # When the car is at a standstill (speed 0), the complete
    # engine power is available for acceleration.
    # The faster the car is, the more engine power is needed for
    # maintaining the speed -> acceleration decreases.

    plt.show()
    sys.exit()

##### 10

def calc_voltage(v, a):
    """

    :param v:   float; velocity
    :param a:   float; acceleration
    """
    s = np.sign(a)
    a = np.abs(a)
    v = np.abs(v)

    # calculate the indices corresponding to v and a
    idx_v = int( v/xd_max*N_grid )
    idx_a= int( a/xdd_max*N_grid )

    # evaluate the 2d array containing the interpolated values at those indices
    return interp_voltage[XYZ, XYZ]*s

###### task 11

# load swingup data
data = np.load('XYZ')

tt, x1, x2, x3, x4, acc = XYZ

uu_s = acc*0

# calculate the required motor voltage from the values of velocity and acceleration
for idx in range(len(acc)):
    a = acc[idx]
    v = x2[idx]

    uu_s[idx] = calc_voltage(XYZ, XYZ)

if 1:
    plt.figure()
    plt.plot(tt, acc, label="a(t)")
    plt.plot(tt, uu_s, label="u(t)")
    plt.legend()

    plt.show()
    sys.exit()

