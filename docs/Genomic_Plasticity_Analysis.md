# Genomic Plasticity Analysis - Full Protocol

## 1. Mobile Genetic Elements (MGEs)

### Tools
- [ABRicate](https://github.com/tseemann/abricate)
- [ISEScan](https://github.com/xiezhq/ISEScan)
- [PHASTER](http://phaster.ca)

### Commands
```bash
abricate --db plasmidfinder,resfinder,vfdb genome.fasta > mge_results.tsv
isescan.py --seqfile genome.fasta --output IS_results --nthread 4
curl -F 'file=@genome.fasta' 'http://phaster.ca/submissions' > phaster.json

### Interpretation Table

| File              | Key Features                  | Significance           |
| ----------------- | ----------------------------- | ---------------------- |
| `mge_results.tsv` | rep genes, AMR markers        | Plasmid content        |
| `IS_results/`     | IS1, IS3, IS5 families        | Recombination hotspots |
| `phaster.json`    | Intact/questionable prophages | HGT events             |
