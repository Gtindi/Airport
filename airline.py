import matplotlib
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

dp = pd.read_csv('data.csv')
# print(dp)

df = nx.from_pandas_edgelist(dp, source='Origin', target='Dest', edge_attr=True)
print(df.nodes)
print(df.edges)
# df.edges()


plt.figure(figsize=(12,8))
x = nx.draw_networkx(df, with_labels=True)
print(plt.show())
# shortest_path_distance = nx.dijkstra_path(df, source='AMA', target='PBI', weight='Distance')
# Shortest_path_distance

# shortest_path_airtime = nx.dijkstra_path(df, source='AMA', target='PBI', weight='AirTime')
# shortest_path_airtime
