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
amps = pd.read_csv(os.path.join('data', 'ex_1.csv')).to_numpy()
amps

# %%
fig, axs = plt.subplots(4, 1)
axs[0].plot(amps[:, 0], label='Oscillatory')
axs[1].plot(amps[:, 2], label='Almost Oscillatory')
axs[2].plot(amps[:, 1], label='Plateau')
axs[3].plot(amps[:, 3], label='Quiescent')

axs[0].set_xticklabels([])
axs[1].set_xticklabels([])
axs[2].set_xticklabels([])
axs[3].set_xlabel('Index')

axs[1].set_ylabel('Amplitude (a.u.)')
axs[1].yaxis.set_label_coords(-0.08, -0.3)

axs[0].set_title('Oscillatory')
axs[1].set_title('Almost Oscillatory')
axs[2].set_title('Plateau')
axs[3].set_title('Quiescent')

plt.tight_layout()
plt.savefig(os.path.join('figures', 'ex_1.pdf'), format='pdf', bbox_inches='tight')
plt.show()
# %%
