"""Script containing plotting functions for driving scripts.

Author
------
Gregory Munday (Met Office, UK)
"""

import iris.plot as iplt
import iris.quickplot as qplt
import matplotlib.pyplot as plt
import numpy as np
import sub_functions as sf


def ebm_plots(yrs, temp_global, tas_delta, temp_global_126, tas_126_delta, plot_path):
    """Plots the regression between tas and rtmt, as well as the resultant
    forcing timeseries.

    Parameters
    ----------
    reg (obj): linear regression outputs with attributes of tas_4x_cube and
        rtmt_4x_cube
    avg_list (arr): array of variable anomaly timeseries
    yrs (arr): array of timeseries years for plotting
    forcing (arr): derived effective forcing
    forcing_126 (arr): effective forcing timeseries, SSP126
    lambda_c (float): derived climate sensitivity, from reg.slope
    temp_global (arr): EBM predicted global near-surface air temperature
    tas_delta (cube): near-surface air temperature anomaly
    temp_global_126 (cube): EBM predicted global near-surface
        air temperature, SSP126
    tas_126_delta (cube): near-surface air temperature anomaly, SSP126
    plot_path (path): path to plot_dir

    Returns
    -------
    None
    """

    # regression line

    fig, ax = plt.subplots(1, 1, figsize=(8, 8))

    # plotting ebm prediction
    ax.plot(yrs,
               temp_global,
               color='black',
               zorder=10,
               linewidth=1.5,
               label='EBM Prediction SSP585')
    ax.plot(yrs,
               temp_global_126,
               color='purple',
               zorder=10,
               linewidth=1.5,
               label='EBM Prediction SSP126')
    ax.plot(yrs, tas_delta, color='red', label='Model SSP585')
    ax.plot(yrs, tas_126_delta, color='blue', label='Model SSP126')
    ax.legend(loc='upper left')
    ax.set_xlabel("Time")
    ax.set_ylabel("Air Surface Temperature (K)")

    fig.savefig(plot_path + 'ebm_test_plots', dpi=400)
    plt.close(fig)
