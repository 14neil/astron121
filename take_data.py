import ugradio; import matplotlib.pyplot as plt; import numpy as np
fir = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2047]) 
fr_sr = 2048*4
def get_plot(data):
    plt.plot(data[0])
    plt.xlim(0,100)
    plt.show()

def get_fft(data, sr):
    y = np.fft.fft(np.array(data[0]))
    freq = np.fft.fftfreq(fr_sr, 1/float(sr))
    plt.plot(np.fft.fftshift(freq)/1e6,np.fft.fftshift(np.abs(y)**2))
    plt.ylabel('Power')
    plt.xlabel('Frequency (MHz)')
    #plt.xlim(-0., 0.1)
    plt.show()

if __name__ == "__main__":
    #sr = input('Enter the sample rate you want to use (Hz): ')
    #nb = input('Enter the nblocks you want: ') 
    sdr = ugradio.sdr.SDR(sample_rate=3.2e6 , fir_coeffs=fir)
    data = sdr.capture_data(nblocks=1, nsamples=fr_sr)
    get_plot(data)
    get_fft(data, 3.2e6)
    proceed = input('Does the data look good: ')
    if proceed == 'yes':
        name = input('Name of .npz file: ')
        np.savez(name, data=data)
    

