import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from ltspice import *


def main():

    rawdata = Ltspice(
        input("Please type your file name(in ltspice directory): "))
    rawdata.parse()

    fig = plt.figure(figsize=(8, 4))
    char_fig = fig.add_subplot(111)
    for i in range(rawdata.case_count):
        icq = rawdata.get_data('Ic(Q1)', i)/1e-3
        vce = rawdata.get_data('vce', i)
        plt.plot(vce, icq, label='$I_B$ = ' +
                 str((rawdata.get_data('I(Ib)', i)/1e-06)[0]) + ' uA')

    plt.autoscale(enable=True, axis='x', tight=True)
    char_fig.xaxis.grid(True, which="minor", ls="dotted", color='lightgrey')
    char_fig.grid(True, which="major", ls="dashed", color='grey')
    char_fig.set_ylabel('$I_{C}$ [mA]')
    char_fig.set_xlabel('$V_{CE}$ [V]')
    plt.title('$I_{C}$ - $V_{CE}$ characteristics')
    plt.legend(loc='upper left')

    plt.axvline(x=0.3, color='gray', linestyle='--')
    plt.tight_layout()
    plt.savefig('./figure/graphout.png')
    plt.show()


def find_early_voltage():
    filename = './ltspice/bjt-lab.raw'
    rawdata = Ltspice(filename)
    rawdata.parse()

    fig = plt.figure(figsize=(8, 4))
    char_fig = fig.add_subplot(111)
    x_intercept = []
    for i in range(rawdata.case_count):
        icq = rawdata.get_data('Ic(Q1)', i)
        vce = rawdata.get_data('vce', i)
        icq_active = (rawdata.get_data('Ic(Q1)', i))[40:]
        vce_active = (rawdata.get_data('vce', i))[40:]
        if i == 0:
            continue
        g = (np.max(icq_active) - np.min(icq_active)) / \
            (np.max(vce_active) - np.min(vce_active))
        x_intercept.append(- ((np.min(icq_active) -
                           g * np.min(vce_active)) / g))
        y_intercept = np.min(icq_active) - g * np.min(vce_active)
        x = np.linspace(-100, 8, 100)
        y = g * x + y_intercept
        char_fig.plot(x, y, linestyle='--')
        char_fig.plot(vce, icq)
    early_voltage = np.mean(x_intercept)
    print(f'Early Voltage: {early_voltage:.2f}')

    plt.xlim(-100, 100)
    plt.autoscale(enable=True, axis='x', tight=True)
    char_fig.xaxis.grid(True, which="minor", ls="dotted", color='lightgrey')
    char_fig.grid(True, which="major", ls="dashed", color='grey')
    plt.axvline(x=0.3, color='gray', linestyle='--')
    plt.show()


if __name__ == "__main__":
    # main()
    find_early_voltage()
