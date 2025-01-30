#!/bin/bash

#SBATCH --partition=general-gpu               # Name of Partition
#SBATCH --gres=gpu:2                          # Request 2 GPU cards for the job
#SBATCH --constraint=epyc64
#SBATCH --constraint=a100
#SBATCH --output=R-%x_%j.out

module purge

source /gpfs/homefs1/ych22001/miniconda3/etc/profile.d/conda.sh

conda activate HF_LLM

python Second_Append_RFLX_noExplicit.py
