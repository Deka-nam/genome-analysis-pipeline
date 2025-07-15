# Genome Analysis Pipeline for *Proteus mirabilis*
This repository hosts a reproducible workflow for analyzing *P. mirabilis* clinical isolates from catheterized urine samples. The pipeline spans assembly, annotation, AMR detection, pan-genome, phylogeny, and genomic plasticity.

---

# Project Overview

*Proteus mirabilis* is a leading cause of catheter-associated urinary tract infections (CAUTIs), exhibiting:
- High genomic plasticity
- Complex antimicrobial resistance (AMR) profiles
- Distinct phylogenetic clusters in clinical settings

This pipeline was developed to characterize clinical isolates from catheterized urine samples, revealing:
- Strain diversity patterns
- Mobile genetic elements
- Resistance gene associations

---

## Overview of Steps

| Step | Module | Description |
|------|--------|-------------|
| 1 | [Species ID](docs/phylogenetics_workflow.md) | Kraken2 taxonomic classification |
| 2 | [Assembly](#2-genome-assembly) | SPAdes for de novo assembly |
| 3 | [Annotation](#3-genome-annotation) | Prokka functional annotation |
| 4 | [MLST](#4-mlst-typing) | Multi-locus sequence typing |
| 5 | [Pan-genome](#5-pangenome-analysis) | Roary & Panaroo |
| 6 | [Phylogeny](#6-phylogenetic-tree-construction) | RAxML tree building |
| 7 | [AMR](#7-amr-gene-detection) | AMRFinderPlus profiling |
| 8 | [Genomic Plasticity](docs/Genomic_Plasticity_Analysis.md) | MGEs, prophages, SVs, HGT |


## Reproducibility/Quick Start

You can recreate the analysis environment using:

```bash
conda env create -f environment.yml
conda activate proteus_env
jupyter notebook one_isolate_workflow.ipynb
```

---

## References

Please cite the tools listed above if using this pipeline in your own work.

---

## Author

**Namrata Deka**
PhD Candidate | Department of Microbiology and Immunology |
University at Buffalo |
GitHub: [github.com/Deka-nam](https://github.com/Deka-nam)


---

