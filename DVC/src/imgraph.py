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
    sys.stderr.write("\tpython imgraph.py data-file\n")
    sys.exit(1)

os.makedirs(os.path.join('data', 'described'), exist_ok=True)

data = pd.read_csv(sys.argv[1])

data_describe = data.describe()

data_describe.to_csv(os.path.join('data/described/outputdesc.csv'))
