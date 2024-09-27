import scanpy as sc
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import scipy

def load_data(adata_path, zscore_path):
    adata = sc.read_h5ad(adata_path)
    zscore_df = pd.read_csv(zscore_path, sep='\t')
    return adata, zscore_df

def calculate_disease_score(adata, zscore_df):
    common_genes = list(set(zscore_df['GENE']) & set(adata.var_names))
    
    if len(common_genes) == 0:
        raise ValueError("No matching genes found. Please check that the gene names are consistent")
    
    gene_to_mi = dict(zip(zscore_df['GENE'], zscore_df['MI']))
    weights = np.array([gene_to_mi[gene] for gene in common_genes])
    
    expr_matrix = adata[:, common_genes].X
    if scipy.sparse.issparse(expr_matrix):
        expr_matrix = expr_matrix.toarray()
    
    disease_scores = np.dot(expr_matrix, weights)
    
    # Normalize the disease score to a range of 0-10 for simplicity
    disease_scores_normalized = (disease_scores - np.min(disease_scores)) / (np.max(disease_scores) - np.min(disease_scores)) * 10
    adata.obs['disease_score'] = disease_scores_normalized
    
    print(f"Disease score calculation is complete. Using {len(common_genes)} common genes。")
    return adata

def plot_umap(adata, color, title, save_path, figsize=(12, 10), dpi=300, point_size=20, cmap='viridis'):
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    sc.pl.umap(adata, color=color, title=title, ax=ax, show=False, size=point_size, cmap=cmap)
    plt.tight_layout()
    plt.savefig(save_path, dpi=dpi, bbox_inches='tight')
    plt.close()

def plot_violin(adata, groupby, values, title, save_path, figsize=(15, 10), dpi=300):
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    sc.pl.violin(adata, groupby=groupby, keys=values, ax=ax, show=False)
    ax.set_title(title)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(save_path, dpi=dpi, bbox_inches='tight')
    plt.close()

def plot_dotplot(adata, groupby, var_names, title, save_path, figsize=(20, 15), dpi=300):
    sc.pl.dotplot(
        adata,
        var_names=var_names,
        groupby=groupby,
        show=False,
        figsize=figsize,
        dot_min=0.1,
        dot_max=1,
        cmap='Reds',
        standard_scale='var'
    )
    
    plt.title(title, fontsize=16)
    
    plt.savefig(save_path, dpi=dpi, bbox_inches='tight')
    plt.close()

def main():
    plt.style.use('seaborn')
    sc.set_figure_params(dpi_save=300, facecolor='white')

    print("Step 1: Loading data and preprocessing")
    adata_path = 'file.h5ad'
    zscore_path = 'geneset.zscore.tsv'
    adata, zscore_df = load_data(adata_path, zscore_path)
    
    adata = calculate_disease_score(adata, zscore_df)
    
    sc.pp.highly_variable_genes(adata, n_top_genes=2000)
    adata = adata[:, adata.var.highly_variable]
    sc.tl.pca(adata, svd_solver='arpack')
    sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)
    sc.tl.umap(adata)
    
    print("Step 2: Drawing cell_types_umap.png")
    plot_umap(adata, color='cell_type', title='Cell Types in Heart Global Dataset', save_path='cell_types_umap.png')
    
    print("Step 3: Drawing disease_score_umap.png")
    plot_umap(adata, color='disease_score', title='Disease Relevance Score', save_path='disease_score_umap.png')
    
    print("Step 4: Drawing disease_score_violin.png")
    plot_violin(adata, groupby='cell_type', values='disease_score', title='Disease Relevance Score by Cell Type', save_path='disease_score_violin.png')
    
    print("Step 5: Drawing top_genes_dotplot.png")
    gene_means = adata.X.mean(axis=0).A1  
    top_genes = adata.var_names[np.argsort(gene_means)[-20:]]  
    top_genes_in_adata = [gene for gene in top_genes if gene in adata.var_names]
    
    missing_genes = set(top_genes) - set(top_genes_in_adata)
    if missing_genes:
        print(f"These genes are not found in adata.var_names and will be ignored: {missing_genes}")
    
    if top_genes_in_adata:
        plot_dotplot(adata, groupby='cell_type', var_names=top_genes_in_adata, title='Expression of Top Genes in Cell Types', save_path='top_genes_dotplot.png')
    else:
        print("No genes can be drawn Dotplot, check the data")

if __name__ == "__main__":
    main()
