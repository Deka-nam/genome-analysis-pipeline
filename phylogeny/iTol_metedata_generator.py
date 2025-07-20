import pandas as pd

# Load your sample metadata. To create a new file you can use the "Dataset color strip" or "Dataset binary" format with a legend section. 
df = pd.read_csv("mlst.csv")

# Map status to color to specific hex codes
color_map = {'Known': '#1f77b4', 'Novel': '#ff7f0e'}
df['Color'] = df['MLST'].map(color_map)

# Start building the iTOL file
with open("itol_mlst.itol.txt", "w") as f:
    f.write("DATASET_COLORSTRIP\n")     #DATASET_COLORSTRIP: This tells iTOL that we are adding a color strip next to the tree.
    f.write("SEPARATOR TAB\n")
    f.write("DATASET_LABEL\tMLST_Status\n")
    f.write("COLOR\t#000000\n\n")
    f.write("LEGEND_TITLE\tMLST Classification\n")
    f.write("LEGEND_SHAPES\t1\t1\n")       #LEGEND_SHAPES: Shape of legend symbols. Use 1 for squares.
    f.write("LEGEND_COLORS\t#1f77b4\t#ff7f0e\n")     #LEGEND_COLORS: Colors used. Make sure these match your DATA entries.
    f.write("LEGEND_LABELS\tKnown MLST\tNovel/Untyped\n\n")     #LEGEND_LABELS: Labels that will appear in the iTOL legend.
    f.write("DATA\n")                  #DATA section: Each line is a taxon name (must match exactly with your tree tip labels), followed by the color.
    for _, row in df.iterrows():
        f.write(f"{row['SampleID']}\t{row['Color']}\n")   #your sample ID column  
      #SEE example_metadata.itol.txt file for reference to see file format
