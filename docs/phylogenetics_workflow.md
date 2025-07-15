# Pipeline Components
This pipeline encompasses the complete workflow for bacterial genome analysis, spanning from raw sequencing reads to phylogenetic inference, and integrating quality control, trimming, de novo assembly, annotation, and core-genome phylogeny using established tools.

---

## 1. **Quality Control**

### Tool: [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/)
FastQC evaluates raw read quality by analyzing per-base sequence quality, GC content, and adapter contamination

**Command**:
```bash
fastqc -t 4 sample_R1.fastq.gz sample_R2.fastq.gz
```
### Tool: [MultiQC](https://seqera.io/multiqc/)
Aggregates all FastQC reports into one combined summary.

**Command**:
```bash
multiqc .
```
---

## 2. **Read Trimming**

### Tool: [Trimmomatic](http://www.usadellab.org/cms/?page=trimmomatic)
Trimmomatic removes adapter sequences and trims low-quality bases to improve assembly quality.

**Command**:
```bash
trimmomatic PE -threads 4 \
  sample_R1.fastq.gz sample_R2.fastq.gz \
  sample_R1_trimmed.fastq.gz sample_R1_unpaired.fastq.gz \
  sample_R2_trimmed.fastq.gz sample_R2_unpaired.fastq.gz \
  ILLUMINACLIP:TruSeq3-PE.fa:2:30:10 \
  SLIDINGWINDOW:4:20 MINLEN:50
```

## 3. **Species Identification**
### Tool: [Kraken2 v2.1.2](https://ccb.jhu.edu/software/kraken2/)

**Command**:
  ```bash
  kraken2 --db kraken2-db --threads 8 --paired sample_R1.fastq.gz sample_R2.fastq.gz --report kraken_report.txt --output kraken_output.txt
  ```
---

## 4. **Genome Assembly**

### Tool: [SPAdes v3.15.5](https://cab.spbu.ru/software/spades/)
SPAdes performs de novo genome assembly optimized for bacterial isolates.

**Command**:
  ```bash
  spades.py -1 sample_R1.fastq.gz -2 sample_R2.fastq.gz -o spades_output
  ```
  ---

## 5. **MLST Typing**
### Tool: [mlst](https://github.com/tseemann/mlst)
MLST stands for Multi-Locus Sequence Typing. 
It is a method used to identify and classify bacteria and other microorganisms based on the DNA sequences of several housekeeping genes. 
By analyzing variations in these genes, MLST can differentiate between bacterial strains, track outbreaks, and study bacterial evolution.

**Command**:
  ```bash
  mlst contigs.fasta --scheme proteus_spp
  ```
The MLST scheme for *P. mirabilis* includes the following six housekeeping genes:
| Gene   | Function                                           |
|--------|----------------------------------------------------|
| atpD   | ATP synthase β-subunit                             |
| dnaJ   | Codes for a chaperone protein of the Hsp40 family  |
| mdh    | Malate dehydrogenase                               |
| pyrC   | Biosynthesis of pyrimidine nucleotides             |
| recA   | DNA recombination and repair                       |
| rpoD   | Codes for the primary sigma factor, σ70            |


---


## 6. **Genome Annotation**
### Tool: [Prokka v1.14.6](https://github.com/tseemann/prokka)
Prokka annotates assembled genomes by predicting coding sequences, rRNAs, tRNAs, and functional annotations.

**Command**:
  ```bash
  prokka --outdir prokka_output --prefix sample spades_output/contigs.fasta
  ```
---

## 7. **Pangenome Analysis**

### Tool: [Roary v3.13.0](https://sanger-pathogens.github.io/Roary/)
Roary calculates the core and accessory genome using annotated .gff files. It requires GFF3 output from Prokka.

**Command**:

  ```bash
  roary -e --mafft -p 8 *.gff
  ```
  - Core genes (present in ≥99% of isolates) are used for phylogeny.
  - Accessory genes vary across strains and inform on genetic diversity.
  ---
 
## 8. **Phylogenetic Tree Construction**
### Tool A: [RAxML v8.2.12](https://cme.h-its.org/exelixis/web/software/raxml/)
RAxML builds a maximum likelihood tree using the core gene alignment produced by Roary.

**Command**:
  ```bash
  raxmlHPC -s core_gene_alignment.aln -n tree -m GTRGAMMA -p 12345 -# 100
  ```
### Tool B: [FastTree](https://morgannprice.github.io/fasttree/)
FastTree is a fast, approximate ML tree builder for large alignments. 

**Command**:
```bash
FastTree -gtr -nt core_gene_alignment.aln >tree.nwk
```
---

## 9. Tree Visualization
### Tool: [iTOL](https://itol.embl.de/)
Upload the .nwk tree file to iTOL for an interactive and annotated tree display.

```text
1. Go to https://itol.embl.de
2. Upload tree.nwk
3. Annotate with metadata (e.g., ST, AMR, source)
```

----

##  Example Outputs

- Kraken-based species ID report confirming *P. mirabilis*
- MLST distribution across isolates
- Core genome phylogenetic tree

---

## References
- Andrews S. FastQC.
- Bolger AM et al. (2014) Trimmomatic. Bioinformatics 30(15):2114–20
- Bankevich A et al. (2012) SPAdes. J Comp Biol 19(5):455–77
- Seemann T. Prokka. Bioinformatics 30(14):2068–69
- Page AJ et al. (2015) Roary. Bioinformatics 31(22):3691–93
- Stamatakis A. (2014) RAxML. Bioinformatics 30(9):1312–13

