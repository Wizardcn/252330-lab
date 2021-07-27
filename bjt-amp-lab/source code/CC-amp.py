import numpy as np
import matplotlib.pyplot as plt
from ltspice import *


def main():
    filename = './ltspice/1-2.raw'
    rawdata = Ltspice(filename)
    rawdata.parse()

    # for i in range(rawdata.case_count):
    #     vout = rawdata.get_data('V(vout)', i)  # in V
    #     vin = rawdata.get_data('V(vin)', i)  # in V
    #     time = rawdata.get_data('time', i) * 1e3  # in ms

    vin = rawdata.get_data('V(vin)') * 1e3  # in mV
    vout = rawdata.get_data('V(vout)') * 1e3  # in mV
    time = rawdata.get_time() * 1e3  # in ms

    fig = plt.figure(figsize=(6, 4.5))
    amp_fig = fig.add_subplot(111)
    plt.plot(time, vout, color='blue', label='$V_{out}$', linewidth=1.5)
    plt.plot(time, vin, color='grey',
             label='$V_{in}$', linewidth=1)

    plt.autoscale(enable=True, axis='x', tight=True)
    amp_fig.xaxis.grid(True, which="minor", ls="dotted", color='lightgrey')
    amp_fig.grid(True, which="major", ls="dashed", color='grey')
    amp_fig.set_ylabel('Voltage (mV)')
    amp_fig.set_xlabel('time (ms)')

    plt.title('$V_{in}$ - $V_{out}$ Common Collector Configuration')
    plt.legend(loc='upper left')

    plt.tight_layout()
    plt.savefig(f'./figure/{filename[10:][:-4]}.png')
    plt.show()


if __name__ == '__main__':
    main()
