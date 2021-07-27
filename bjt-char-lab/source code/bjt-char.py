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

    plt.tight_layout()
    plt.savefig('./figure/graphout.png')
    plt.show()


if __name__ == "__main__":
    main()
