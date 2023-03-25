import matplotlib.pyplot as plt
import numpy as np
import sys

filename = sys.argv[1]        # Stores ARG1 in filename, as in: $ python plot.py ARG1 ARG2 
data = np.loadtxt(filename, comments='"')   # Attempts to load filename into local variable data.

## Part 0
# Figure out what arguments to add to the loadtxt function call
# so that numbers are loaded into the local function 'data'.
# Hint: look for arguments like 'skiprows' and 'delimiter'
# Check by running:
#   $ python plot.py raw-data/Sp22_245L_sec-001_tensiletest-pekk_bulk.raw
# at the command line.


## Part 1
# Figure out what columns and rows of data we need to plot
# Stress (y-axis) vs Strain (x-axis)
# plot raw-data/Sp22_245L_sec-001_tensiletest-pekk_bulk.raw
# Make sure to include axis labels and units!
# plt.plot(xdata, ydata, arguments-to-make-plot-pretty)
stress=data[:,1]
strain=data[:,-1]
name=filename.split('-')[-1][:-4]

plt.plot(strain, stress, 'o', markersize=1)
plt.xlabel('Strain (%)')
plt.ylabel('Stress (Pa)')
plt.title(f'{name} stress vs strain')
plt.show()


## Part 2
# Check to see if your code in part 1 will plot all of the files in raw-data/
# Edit the files (use git liberally here!) to make them more usable
# Don't worry about deleting parts you might need later -- that's why we use git!


## Part 3
# Use linear regression to calculate the slope of the linear part of
# the stress-strain data. Plot your line against the data to make 
# sure it makes sense! Use the slope of this line to calculate and print
# the Young's modulus (with units!)
# $ git ls-files | grep "raw_data/" | xargs -I{} sh -c 'python plot.py {}'
if 'pekk' in name:
    cutoff=3.1
else:
    cutoff=1.8

idx=np.where(strain <cutoff)
linear_strain=strain[idx]
linear_stress=stress[idx]

plt.plot(strain, stress, 'o', markersize=1, label='Original')
plt.plot(linear_strain, linear_stress, markersize=1, label='Linear')
plt.xlabel('Strain (%)')
plt.ylabel('Stress (Pa)')
plt.title(f'{name} stress vs strain')
plt.legend()
plt.show()

A=np.vstack([np.ones(len(linear_strain)),linear_strain]).T

c, m=np.linalg.lstsq(A, linear_stress, rcond=None)[0]

print(f'Young\'s Modulus: {m} Pa')


## Part 4
# Modify your code to save your plots to a file and see if you can generate
# plots and Young's moduli for all of the cleaned up files in your data 
# directory. If you haven't already, this is a good time to add text to 
# your .gitignore file so you're not committing the figures to your repository.
plt.plot(strain, stress, 'o', markersize=1, label='Original')
plt.plot(linear_strain, linear_stress, markersize=1, label='Linear')
plt.xlabel('Strain (%)')
plt.ylabel('Stress (Pa)')
plt.title(f'{name} Young\'s Modulus: {m:.2f} Pa ')
plt.legend()
plt.savefig(f'{name}.png')
