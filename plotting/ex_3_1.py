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
amps = pd.read_csv(os.path.join('data', 'ex_3_1.csv')).to_numpy()
amps

# %%
plt.figure()
plt.plot(amps[:, 0], label='$b=0$')
plt.plot(amps[:, 1], label='$b=2.5, T=12$')
plt.plot(amps[:, 2], label='$b=2.5\infty, T=12\infty$')
plt.xlabel('Index')
plt.ylabel('Amplitude (a.u.)')
plt.legend(
    loc='upper center',
    bbox_to_anchor=(0.5, -0.1),
    fancybox=True,
    shadow=True,
    ncol=3,
    frameon=True,
)
plt.savefig(os.path.join('figures', 'ex_3_1.pdf'), format='pdf', bbox_inches='tight')
plt.show()
# %%
