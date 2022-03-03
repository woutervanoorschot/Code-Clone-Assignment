from xmlrpc.client import FastParser
import seaborn as sns; 
import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt
sns.set_theme()

# df = pd.read_csv('file.csv', header=None)


# sns.heatmap(df)

fpaths = glob.glob("../out/jquery-versions/*.js")
n = lambda x: x.split('-')[2]


filelens = list()
for file in fpaths: 
    num_lines = sum(1 for line in open(file))
    filelens.append(num_lines)

pathnames = [n(p) for p in fpaths]
s = lambda x: int(x.replace('.', "").replace('js',""))
# pathsorted = sorted(pathnames, key=s)
keystosort = np.argsort([s(p) for p in pathnames])

fig, ax = plt.subplots()

p1 = ax.bar(np.arange(len(filelens)), [filelens[i] for i in keystosort])

ax.axhline(0, color='grey', linewidth=0.8)
ax.set_ylabel('Lines')
plt.xticks(rotation=90)
ax.set_xticks(np.arange(len(filelens)), labels=[n(f) for f in [fpaths[i] for i in keystosort]])
ax.legend()

ax.bar_label(p1, label_type='center')

plt.show()
