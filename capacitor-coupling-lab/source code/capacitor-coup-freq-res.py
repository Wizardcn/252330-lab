import matplotlib.pyplot as plt
from ltspice import *
from matplotlib.ticker import EngFormatter


def main():
    # read rawdata
    filename = './ltspice/3-1.raw'
    rawdata = Ltspice(filename)
    rawdata.parse()

    # prepare data
    raw_vout = np.absolute(rawdata.get_data('V(vout)'))
    print(raw_vout)
    vout = []
    for data in raw_vout:
        vout.append(20 * np.log10(data))

    vout = np.array(vout)
    freq = rawdata.get_frequency()
    max_vout = np.max(vout)
    max_vout = np.max(vout)
    vout_3dB = np.max(vout) - 3
    freq_cutoff_index = np.where(np.around(vout_3dB, decimals=0)
                                 == np.around(vout, decimals=0))
    print(freq_cutoff_index)
    low_cutoff_freq = freq[freq_cutoff_index[0][0]]
    high_cutoff_freq = freq[freq_cutoff_index[0][1]]
    print(
        f'Bandwidth: {np.around((high_cutoff_freq - low_cutoff_freq) / 1000000, decimals=2)} MHz')
    print(
        f'Amplifier gain at midband: {np.around(np.max(raw_vout), decimals=2)}')

    # vitualize data
    figure, axis1 = plt.subplots(figsize=(8, 4))
    axis1.set_xscale('log')
    # axis1.set_title('Capacitor Coupling Frequency Response')
    formatter1 = EngFormatter(unit='Hz')
    formatter2 = EngFormatter(unit='dB')
    axis1.xaxis.set_major_formatter(formatter1)
    axis1.yaxis.set_major_formatter(formatter2)
    axis1.plot(freq, vout)
    axis1.set_xlabel('Frequency')
    axis1.set_ylabel('Amplifier Gain')
    plt.autoscale(enable=True, axis='x', tight=True)
    axis1.xaxis.grid(True, which="minor", ls="dotted", color='lightgrey')
    axis1.grid(True, which="major", ls="dashed", color='grey')

    # display data
    # plt.axhline(y=np.around(1/np.sqrt(2)*max_vout, decimals=3),
    #             color='gray', linestyle='--')
    # plt.axvline(x=)
    plt.axhline(y=vout_3dB, color='gray', linestyle='--')
    plt.axvline(x=low_cutoff_freq, color='gray', linestyle='--')
    plt.axvline(x=high_cutoff_freq, color='gray', linestyle='--')
    plt.tight_layout()
    plt.savefig(f'./figure/{filename[10:][:-4]}-freq.png')
    plt.show()


if __name__ == '__main__':
    main()
