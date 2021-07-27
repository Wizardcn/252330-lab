import numpy as np
import matplotlib.pyplot as plt
from ltspice import *


def main():
    filename = './ltspice/1-3.raw'
    rawdata = Ltspice(filename)
    rawdata.parse()

    vout = rawdata.get_data('V(vout)')  # in V
    vin = rawdata.get_data('V(vin)') * 1e3  # in mV
    time = rawdata.get_time() * 1e3  # in ms

    figure, axis1 = plt.subplots()

    axis1.plot(time, vout, color='blue', label='$V_{out}$')
    axis1.set_ylabel('$V_{out}$(V)')
    axis1.set_xlabel('time (ms)')

    axis2 = axis1.twinx()
    ymin, ymax = -100, 100
    axis2.set_ylim((ymin, ymax))
    axis2.plot(time, vin, color='red', label='$V_{in}$')
    axis2.set_ylabel('$V_{in}$(mV)')

    align_yaxis(axis1, 0, axis2, 0)
    plt.title('$V_{in}$ - $V_{out}$ Common Base Configuration')
    axis1.legend(loc='upper left')
    axis2.legend(loc='upper right')

    plt.autoscale(enable=True, axis='x', tight=True)
    axis1.xaxis.grid(True, which="minor", ls="dotted", color='lightgrey')
    axis1.grid(True, which="major", ls="dashed", color='grey')

    plt.tight_layout()
    plt.savefig(f'./figure/{filename[:-4]}.png')
    plt.show()


def align_yaxis(ax1, v1, ax2, v2):
    """adjust ax2 ylimit so that v2 in ax2 is aligned to v1 in ax1"""
    _, y1 = ax1.transData.transform((0, v1))
    _, y2 = ax2.transData.transform((0, v2))
    inv = ax2.transData.inverted()
    _, dy = inv.transform((0, 0)) - inv.transform((0, y1-y2))
    miny, maxy = ax2.get_ylim()
    ax2.set_ylim(miny+dy, maxy+dy)


if __name__ == '__main__':
    main()
