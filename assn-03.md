# Assignment-3

## 1. Use rsync to upload the mt_genomes directory onto the AHPCC in `/storage/username`. So the final path is `/storage/username/mt_genomes`

`rsync -avh mt_genomes vlamba@hpc-portal2.hpc.uark.edu:/storage/vlamba`

## 2. Use scp or rsync to upload `unknown.fa`, which contains an unknown sequence

`scp unknown.fa vlamba@hpc-portal2.hpc.uark.edu:/storage/vlamba`

## 3. Slurm script

[blast-run-assign.slurm](https://github.com/vinitamehlawat/BIOL_pyhton_course/blob/main/blast-run-assign.slurm)

## 4. Use rsync to synchronize the remote mt_genomes, which contains your new output file, and your local version of mt_genomes.

From your local computer run `rsync -avh vlamba@hpc-portal2.hpc.uark.edu:/storage/vlamba/mt_genomes /home/vinita/Downloads/Spring2023-course/watermelon_files/`


## Answer following based on above script you ran:

###### How long did it take your job to complete

`00:00:06`

###### Closest match in the database

`Cucurbita`

###### Gene we got from blast hit is

`cox1`
