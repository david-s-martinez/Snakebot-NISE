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
amps = pd.read_csv(os.path.join('data', 'ex_3_2.csv')).to_numpy()
amps

# %%
plt.figure()
plt.plot(amps[700:, 0], label='Neuron 1')
plt.plot(amps[700:, 1], label='Neuron 2')
plt.xlabel('Index')
plt.ylabel('Amplitude (a.u.)')
plt.legend(
    loc='upper center',
    bbox_to_anchor=(0.5, -0.1),
    fancybox=True,
    shadow=True,
    ncol=2,
    frameon=True,
)
plt.savefig(os.path.join('figures', 'ex_3_2.pdf'), format='pdf', bbox_inches='tight')
plt.show()
# %%
