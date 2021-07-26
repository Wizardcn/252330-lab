import matplotlib.pyplot as plt
from ltspice import *
from matplotlib.ticker import EngFormatter


def main():
    filename = '1-3(2nd).raw'
    rawdata = Ltspice(filename)
    rawdata.parse()

    vout = np.real(rawdata.get_data('V(vout)'))
    freq = rawdata.get_frequency() *


if __name__ == '__main__':
    main()
