# 🧬 GZSper: Illuminating Single-Cell Landscapes with GWAS Insights

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

GZSper (GWAS Z-score to Single-cell Phenotypes for Expression Research) is a Python toolkit designed to bridge the gap between GWAS and single-cell RNA sequencing analysis. By ingeniously translating GWAS Z-scores into single-cell phenotypes, GZSper empowers researchers to unravel the cellular intricacies of complex traits and diseases with unprecedented resolution.

## ✨ Key Features

- 🔗 Integration of GWAS Z-scores with scRNA-seq data
- 🧬 Translation of genetic associations to single-cell phenotypes
- 🎨 Visualizations of GWAS-informed single-cell landscapes
- 🚀 Processing of large-scale genomic and transcriptomic datasets
- 🔍 Exploration of trait-associated gene expression patterns at single-cell resolution
- 📊 Robust statistical analysis and data normalization
- 🔄 Adaptable to a wide spectrum of traits and diseases studied in GWAS

## 🛠️ Installation

```bash
git clone https://github.com/Benjamin-JHou/GZSper.git
cd GZSper
pip install -r requirements.txt
```

## 🚀 Usage

Embark on your GZSper journey with these simple steps:

### 1. 📥 Data Fusion

```python
adata, zscore_df = load_data(adata_path, zscore_path)
```

**Problem Solved:** Seamlessly merges single-cell RNA-seq data with GWAS Z-scores, laying the foundation for integrated analysis.

### 2. 🧮 Phenotype Inference

```python
adata = calculate_phenotype_score(adata, zscore_df)
```

**Problem Solved:** Translates GWAS signals into meaningful single-cell phenotypes, revealing cells most influenced by trait-associated genetic variations.

### 3. 🌈 Phenotypic Landscape Visualization

```python
plot_umap(adata, color='cell_type', title='Cellular Diversity', save_path='cell_types_umap.png')
plot_umap(adata, color='gwas_phenotype', title='GWAS-Informed Cellular Phenotype', save_path='gwas_phenotype_umap.png')
```

**Problem Solved:** Crafts intuitive visualizations of cell type distributions and GWAS-informed phenotypes, unveiling trait-relevant cellular populations.

### 4. 🎻 Phenotypic Distribution Analysis

```python
plot_violin(adata, groupby='cell_type', values='gwas_phenotype', title='GWAS-Informed Phenotype by Cell Type', save_path='gwas_phenotype_violin.png')
```

**Problem Solved:** Compares GWAS-informed phenotypes across cell types, highlighting cellular populations most relevant to the studied trait or disease.

### 5. 🔵 Gene-Phenotype Interplay

```python
plot_dotplot(adata, groupby='cell_type', var_names=top_genes_in_adata, title='Expression of Top GWAS-Identified Genes Across Cell Types', save_path='top_genes_dotplot.png')
```

**Problem Solved:** Visualizes expression patterns of key GWAS-identified genes across cell types, revealing cell-specific contributions to complex traits and diseases.

## 📊 Example Output

![Cellular Diversity UMAP](https://private-user-images.githubusercontent.com/147773802/371460038-6c446fe8-7302-46d6-941d-aff0cb10467f.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mjc0MjY5MjAsIm5iZiI6MTcyNzQyNjYyMCwicGF0aCI6Ii8xNDc3NzM4MDIvMzcxNDYwMDM4LTZjNDQ2ZmU4LTczMDItNDZkNi05NDFkLWFmZjBjYjEwNDY3Zi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwOTI3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDkyN1QwODQzNDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zNGZlMjE0YjA0NDVlNjU2MjZjYWRjMzk3NzU0MmMwMDY5M2I0NzllOGE3NjcwMmI1MDZlNWM3YzI5ZmNiNTRjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.hd1Ni89Wwz18YIAqHzXMELdNu2VDql2z8SiN-7IwF4c)

## 🧪 Versatility Across Traits and Diseases

GZSper's adaptability spans the entire spectrum of GWAS-studied phenomena. By simply swapping GWAS Z-scores and single-cell datasets, researchers can illuminate cellular mechanisms underlying:

- Complex diseases (e.g., cardiovascular disorders, autoimmune conditions, neuropsychiatric illnesses)
- Quantitative traits (e.g., anthropometric measures, physiological parameters)
- Molecular phenotypes (e.g., gene expression variability, metabolomic profiles)


## 📄 License

GZSper is released under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html), which allows you to:

- Use the code for any purpose, including research and commercial projects.
- Modify and distribute the code, provided that derivative works are also released under the GPL-3.0 license.

For more information about the GPL-3.0 license and its permissions and restrictions, please refer to the [official GNU GPL-3.0 page](https://www.gnu.org/licenses/gpl-3.0.en.html).

## 📚 Citation

If GZSper empowers your research, please cite:

```
Junyu Zhou (2024). GZSper: Illuminating Single-Cell Landscapes with GWAS Insights. GitHub. https://github.com/Benjamin-JHou/GZSper
```

## 🌟 Star Us!

If GZSper sparks your scientific curiosity, star our repository to help fellow researchers discover this powerful tool!

