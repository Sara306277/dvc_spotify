import io
import sys
import xml.etree.ElementTree
import random
import re
import os
import yaml
import json
import networkx as nx
from networkx.readwrite import json_graph
import networkx.algorithms.community as nxComm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from random import choice

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython prepare.py data-file\n")
    sys.exit(1)

os.makedirs(os.path.join('data', 'sna_graph'), exist_ok=True)

with open(sys.argv[1]) as f:
    js_graph = json.load(f)

g = nx.Graph(json_graph.node_link_graph(js_graph))

options = {
    'node_color': 'b',
    'with_labels': False,
    'node_size': 50
}

nx.draw(g, **options)

plt.savefig(os.path.join('data/sna_graph/sna_graph.png'))