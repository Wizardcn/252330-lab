import matplotlib.pyplot as plt
from ltspice import *
from matplotlib.ticker import EngFormatter


def main():
    filename = './ltspice/1-3(2nd).raw'
    rawdata = Ltspice(filename)
    rawdata.parse()

    raw_vout = np.absolute(rawdata.get_data('V(vout)'))
    vout = []
    for data in raw_vout:
        vout.append(20 * np.log10(data))

    vout = np.array(vout)
    freq = rawdata.get_frequency()

    figure, axis1 = plt.subplots(figsize=(8, 4))
    axis1.set_xscale('log')
    axis1.set_title('CB Amplifier Frequency Characteristic')
    formatter1 = EngFormatter(unit='Hz')
    formatter2 = EngFormatter(unit='dB')
    axis1.xaxis.set_major_formatter(formatter1)
    axis1.yaxis.set_major_formatter(formatter2)
    axis1.plot(freq, vout)
    axis1.set_xlabel('Frequency')
    axis1.set_ylabel('Amplifier Gain')
    plt.autoscale(enable=True, axis='x', tight=True)
    axis1.xaxis.grid(True, which='minor', ls='dotted', color='lightgrey')
    axis1.grid(True, which='major', ls='dashed', color='grey')

    plt.tight_layout()
    plt.savefig(f'./figure/{filename[:-4]}-freq.png')
    plt.show()


if __name__ == '__main__':
    main()
