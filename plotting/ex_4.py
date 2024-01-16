# %%
# !%matplotlib inline
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scienceplots

plt.style.use(['science', 'no-latex', 'notebook'])
# Set the figure dpi to 260
plt.matplotlib.rcParams['figure.dpi'] = 260

# %%
idx = '3b'
n_subplots = int(idx[0])
amps = pd.read_csv(os.path.join('data', f'ex_4_{idx}.csv')).to_numpy()
amps
# %%
titles = {
    '3a': '$a_1 = 2.5, a_2 = 0$',
    '3b': '$a_1 = a_2 = 2.5$',
    '4a': '$a_1 = 2.5, a_2 = a_3 = 0$',
    '4b': '$a_1 = a_2 = 1.5 , a_3=0$',
    '4c': '$a_1 = a_3 = 1.5 , a_2=0$',
    '4d': '$a_1 = a_2 = a_3 = 2.5$',
}

xlims = {
    '3a': (250, 750),
    '3b': (300, 1450),
    '4a': (250, 1500),
    '4b': (300, 700),
    '4c': (100, 1300),
    '4d': (400, 2200),
}

fig, axs = plt.subplots(n_subplots, 1)
for i in range(n_subplots):
    axs[i].plot(amps[:, i], label=f'Neuron {i + 1}')

    axs[i].set_xlim(xlims[idx])
    axs[i].set_xticklabels([]) if i < n_subplots - 1 else axs[i].set_xlabel('Index')

    # Creating a twin axes for the ylabel on the right
    ax2 = axs[i].twinx()
    ax2.set_yticklabels([])
    ax2.set_ylabel(f'Neuron {i + 1}')

axs[0].set_title(titles[idx])
axs[1].set_ylabel('Amplitude (a.u.)')
if n_subplots == 4:
    axs[1].yaxis.set_label_coords(-0.08, -0.3)

plt.savefig(
    os.path.join('figures', f'ex_4_{idx}.pdf'), format='pdf', bbox_inches='tight'
)
plt.show()
# %%
