#! /usr/bin/env python3

# import module
import argparse

# create an ArgumentParser object
parser = argparse.ArgumentParser(description="This script create a SLURM file fo jobs on the AHPCC cluster")

# add positional(required) arguments

parser.add_argument("job_name",help="Name of the job", type = str)

# add optional arguments
# the default for 'store true is . . . "False"
# if 'store_true', then assign 'True' with -v or --verbose
parser.add_argument("-n", "--num_nodes", help="Number of nodes requested", default = '1', type=int)
parser.add_argument("-p", "--num_processor", help="Number of processor requested", default = '24', type=int)
parser.add_argument("-w", "--walltime", help="Length of job", default = '24', type=int)
parser.add_argument("-q", "--queue", help="Requested queue (comp01, comp06, comp72)", default = 'comp72', type = str)

# parse the actual arggument
# access argument values via 'args' variable
args = parser.parse_args()
 
#set some variable name
job_name = '<JOB-NAME>'
queue = 'comp01'
walltime = '1'
num_nodes = 1
num_processors = 24


#print bash header

print('#!/bin/bash')

print('#SBATCH --job_name=' + job_name + args.job_name)
print('#SBATCH --nodes=' + str(num_nodes))
print('#SBATCH --ntasks-per-node=1')
print('#SBATCH --cpus-per-task=32')
print('#SBATCH --partition ' + queue + args.queue)
print('#SBATCH --qos comp')
print('#SBATCH --constraint xz036')
print('#SBATCH --time=' + str(args.walltime) + ':00:00')
print('#SBATCH --output=blast-assignment-results.txt')
print('#SBATCH -e blast-assignment_%j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=vlamba@uark.edu')


print()
# purge modules, then load a blast module
print('module purge')

print('cd $SLURM_SUBMIT_DIR')
print('# job command here')
