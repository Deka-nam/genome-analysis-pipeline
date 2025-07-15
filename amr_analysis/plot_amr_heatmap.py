import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("amrfinder_summary.csv", index_col=0)
binary_df = df.applymap(lambda x: 0 if str(x).strip() in ["-", "–"] else 1)

plt.figure(figsize=(6, 4))
sns.heatmap(binary_df, cmap="OrRd", cbar=False, annot=df, fmt='', linewidths=0.5)
plt.title("AMR Gene Presence Across Isolates")
plt.xlabel("Isolates")
plt.ylabel("AMR Genes")
plt.tight_layout()
plt.savefig("amr_heatmap.png", dpi=300)
plt.show()
