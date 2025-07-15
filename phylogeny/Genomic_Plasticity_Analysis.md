# Genomic Plasticity Analysis - Full Protocol

*Proteus mirabilis* exhibits high genomic plasticity through mobile genetic elements (MGEs) and horizontal gene transfer. Key analyses include:

## Mobile Genetic Elements (MGEs)

### Tools
- [ABRicate](https://github.com/tseemann/abricate) : Plasmids/Integrons
- [ISEScan](https://github.com/xiezhq/ISEScan) : IS
- [PHASTER](http://phaster.ca) : Prophages

### Commands
```bash
abricate --db plasmidfinder,resfinder,vfdb genome.fasta > mge_results.tsv
isescan.py --seqfile genome.fasta --output IS_results --nthread 4
curl -F 'file=@genome.fasta' 'http://phaster.ca/submissions' > phaster.json
```
## ISEScan Fails Troubleshooting
```bash
repeatmasker -species bacteria genome.fasta
```

### Interpretation Table

| File              | Key Features                  | Significance           |
| ----------------- | ----------------------------- | ---------------------- |
| `mge_results.tsv` | rep genes, AMR markers        | Plasmid content        |
| `IS_results/`     | IS1, IS3, IS5 families        | Recombination hotspots |
| `phaster.json`    | Intact/questionable prophages | HGT events             |
