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
amps = pd.read_csv(os.path.join('data', 'ex_5.csv')).to_numpy()
amps

# %%
fig, axs = plt.subplots(10, 2)
for i in range(2):
    for j in range(10):
        j_idx = j - 2 if i == 1 else j
        color = 'blue' if i == 0 else 'red'
        axs[j, i].plot(amps[:, j_idx], color=color)
        axs[j, i].set_yticklabels([])
        if j != 9:
            axs[j, i].set_xticklabels([])

        # Creating a twin axes for the ylabel on the right
        ax2 = axs[j, i].twinx()
        ax2.set_yticklabels([])
        ax2.set_ylabel(f'N{10 * i + j + 1}')

axs[4, 0].set_ylabel('Amplitude (a.u.)')
axs[4, 0].yaxis.set_label_coords(-0.04, -0.3)

axs[9, 0].set_xlabel('Index')
axs[9, 1].set_xlabel('Index')

# plt.tight_layout()
plt.savefig(os.path.join('figures', 'ex_5.pdf'), format='pdf', bbox_inches='tight')
plt.show()
# %%
