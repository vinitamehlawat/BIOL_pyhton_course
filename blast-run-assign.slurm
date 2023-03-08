#!/bin/bash

#SBATCH --job-name=blast-assignment
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=32
#SBATCH --partition condo
#SBATCH --qos condo
#SBATCH --constraint 'xz036'
#SBATCH --time=00:01:00
#SBATCH --output=blast-assignment-results.txt
#SBATCH -e blast-assignment_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=vlamba@uark.edu

# purge modules, then load a blast module
module purge
module load intel/18.0.1 impi/18.0.1 mkl/18.0.1
module load blast

# concatenate all the genomes into a single file called ‘genomes.fas’

cd $SLURM_SUBMIT_DIR
cat *.fasta > genomes.fas

# make a blast database of all the genomes

makeblastdb -in genomes.fas -dbtype nucl

# search the unknown sequence against your database

blastn -query /storage/vlamba/unknown.fa -db genomes.fas > unknown.vs.genomes.blastn


# compelet!
