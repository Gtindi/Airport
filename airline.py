# Install the following modules:   &&   Ensure 'data.csv' file is within the same file directory
# pip install pandas
# pip install networkx
# pip install matplotlib

# Step 1: Import Packages and classes
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Step 2: Provide data from the tables
dp = pd.read_csv('data.csv')
print(dp)

df = nx.from_pandas_edgelist(dp, source='Origin', target='Dest', edge_attr=True)
print(df.nodes)
print(df.edges)

# Step 3: Creating a graph
plt.figure(figsize=(12, 8))
x = nx.draw_networkx(df, with_labels=True)
print(plt.show())
shortest_path_distance = nx.dijkstra_path(df, source='AMA', target='PBI', weight='Distance')
print(shortest_path_distance)   

