# genome-analysis-pipeline
A curated repository of my bioinformatics work: genome assembly, annotation, AMR analysis, and data visualization

---
# Genome Analysis of *Proteus mirabilis* Clinical Isolates

This repository contains a complete workflow for analyzing *Proteus mirabilis* clinical isolates obtained from catheterized urine samples. The pipeline includes species identification, MLST typing, genome assembly, annotation, pangenome analysis, phylogenetic reconstruction, and antimicrobial resistance (AMR) gene profiling.

---

# Project Overview

*Proteus mirabilis* is a common uropathogen associated with catheter-associated urinary tract infections (CAUTIs). In this study, we analyzed the genomic diversity, pangenome structure, phylogenetic relationships, and resistance gene profiles of clinical isolates using a modular bioinformatics pipeline.

---

# Pipeline Components

# 1. **Species Identification**
- **Tool**: [Kraken2 v2.1.2](https://ccb.jhu.edu/software/kraken2/)
- **Command**:
  ```bash
  kraken2 --db kraken2-db --threads 8 --paired sample_R1.fastq.gz sample_R2.fastq.gz --report kraken_report.txt --output kraken_output.txt
  ```
---

# 3. **Genome Assembly**
- **Tool**: [SPAdes v3.15.5](https://cab.spbu.ru/software/spades/)
- **Command**:

  ```bash
  spades.py -1 sample_R1.fastq.gz -2 sample_R2.fastq.gz -o spades_output
  ```
  ---

# 3. **MLST Typing**
- **Tool**: [mlst](https://github.com/tseemann/mlst)
- **Command**:
  ```bash
  mlst contigs.fasta
  ```
---

# 4. **Genome Annotation**

- **Tool**: [Prokka v1.14.6](https://github.com/tseemann/prokka)
- **Command**:

  ```bash
  prokka --outdir prokka_output --prefix sample spades_output/contigs.fasta
  ```
---

# 5. **Pangenome Analysis**

- **Tool**: [Roary v3.13.0](https://sanger-pathogens.github.io/Roary/)
- **Command**:

  ```bash
  roary -e --mafft -p 8 *.gff
  ```
  
  ---
 
# 6. **Phylogenetic Tree Construction**
- **Tool**: [RAxML v8.2.12](https://cme.h-its.org/exelixis/web/software/raxml/)
- **Command**:

  ```bash
  raxmlHPC -s core_gene_alignment.aln -n tree -m GTRGAMMA -p 12345 -# 100
  ```
 ---
 
# 7. **AMR Gene Detection**

- **Tool**: [AMRFinderPlus v3.10.23](https://github.com/ncbi/amr)
- **Command**:

  ```bash
  amrfinder -n contigs.fasta -o amrfinder_output.tsv --organism Proteus_mirabilis
  ```
  
---

##  Example Outputs

- Kraken-based species ID report confirming *P. mirabilis*
- MLST distribution across isolates
- Core genome phylogenetic tree
- AMR gene presence-absence heatmap

---

## Reproducibility

You can recreate the analysis environment using:

```bash
conda env create -f environment.yml
conda activate proteus_env
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

