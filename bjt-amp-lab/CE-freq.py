import matplotlib.pyplot as plt
from ltspice import *
from matplotlib.ticker import EngFormatter


def main():
    # read rawdata
    filename = '1-1.raw'
    rawdata = Ltspice(filename)
    rawdata.parse()

    # prepare data
    raw_vout = np.real(rawdata.get_data('V(vout)'))
    print(raw_vout)
    vout = []
    for data in raw_vout:
        pos_data = -1 * data
        vout.append(20 * np.log10(pos_data))

    vout = np.array(vout)
    freq = rawdata.get_frequency() * 1e2

    # vitualize data
    figure, axis1 = plt.subplots(figsize=(8, 4))
    axis1.set_xscale('log')
    axis1.set_title('CE Amplifier Frequency Characteristic')
    formatter1 = EngFormatter(unit='Hz')
    formatter2 = EngFormatter(unit='dB')
    axis1.xaxis.set_major_formatter(formatter1)
    axis1.yaxis.set_major_formatter(formatter2)
    axis1.plot(freq, vout)
    axis1.set_xlabel('Frequency')
    # axis1.set_ylabel('')
    plt.autoscale(enable=True, axis='x', tight=True)
    axis1.xaxis.grid(True, which="minor", ls="dotted", color='lightgrey')
    axis1.grid(True, which="major", ls="dashed", color='grey')

    # display data
    plt.tight_layout()
    plt.savefig(f'{filename[:-4]}-freq.png')
    plt.show()


if __name__ == '__main__':
    main()
