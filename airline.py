import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


# plt.figure(figsize=(12,8))
# nx.draw_networkx(df, with_labels=True)
dp = pd.read_csv('data.csv')
print(dp)

df = nx.from_pandas_edgelist(data, source='Origin', target='Dest', edge_attr=True)
# df.nodes()
# df.edges()
# # % matplotlib inline
# shortest_path_distance = nx.dijkstra_path(df, source='AMA', target='PBI', weight='Distance')
# Shortest_path_distance

# shortest_path_airtime = nx.dijkstra_path(df, source='AMA', target='PBI', weight='AirTime')
# shortest_path_airtime
