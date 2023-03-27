
#! /usr/bin/env python3

#set some variable name
job_name = '<JOB-NAME>'
queue = 'comp01'
walltime = '1'
num_nodes = 1
num_processors = 24


#print bash header

print('#!/bin/bash')

print('#SBATCH --job_name=' + job_name)
print('#SBATCH --nodes=' + str(num_nodes))
print('#SBATCH --ntasks-per-node=1')
print('#SBATCH --cpus-per-task=32')
print('#SBATCH --partition ' + queue)
print('#SBATCH --qos comp')
print('#SBATCH --constraint xz036')
print('#SBATCH --time=' + str(walltime) + ':00:00')
print('#SBATCH --output=blast-assignment-results.txt')
print('#SBATCH -e blast-assignment_%j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=vlamba@uark.edu')


print()
# purge modules, then load a blast module
print('module purge')

print('cd $SLURM_SUBMIT_DIR')
print('# job command here')



