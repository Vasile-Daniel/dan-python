'''
Signal Processing - Plotting 
Basics of signal plot generation using Python, 
including the three most common 'types' of signal: 
waveform, spectrum and live (interactive) plot.
Author: Vasile-Daniel DAN, Edinburgh, Data: 23.02.2021 
'''



import matplotlib.pyplot as plot 
import math
import numpy 

# Generate pure sign signal 
lenght = 0.05 # time [ms]
sampleRate = 48000.0 # frecvency [Hz]
f1 = 1000.0 # [Hz]
omega = 2.0 * math.pi * f1

waveform = [math.sin( omega * i / sampleRate) for i in range(int(lenght * sampleRate))  ]

timeBins = [1000.0* i / sampleRate for i in range(len(waveform))] 
# calculate the spectrum 

spectrum = numpy.fft.rfft(waveform) # "rfft" asume the input is real  
# Spectrum Module 
spectrumMod = 20.0 * numpy.log10(numpy.abs(spectrum))
spectrumPha = 180.0 / numpy.pi * numpy.angle(spectrum)
frequencyBins = [i/ len(spectrum) * sampleRate / 2.0 for i in range(len(spectrum))]

# Waveform Plot 

plot.plot(timeBins, waveform, 'o-' , label='Sine wave',linewidth=2)
plot.xlim(0,2*(1.0/f1)*1000.0)
plot.xlabel('Time [ms]')
plot.ylabel('Aplitude [.]')
plot.grid(1)
plot.legend()
plot.show()

# Spectrum plot 
"""
plot.subplot(2,1,1)
plot.semilogx(frequencyBins, spectrumMod,label = 'Sin wave spectrum')
plot.grid(1)
plot.legend()
plot.xlabel('Power [dB]')
plot.ylabel('Phase [degrees]')
plot.title('Spectrum of a sin wave')
plot.subplot(2,1,2)
plot.semilogx(frequencyBins, spectrumPha, label = 'Sine wave spectrum')
plot.grid(1)
plot.legend()
plot.xlabel('Frequency [Hz]')
plot.ylabel('Phase [degrees]')
plot.show()
"""

def plotWindowClosedEvent(event):
	global STOP_FLAG
	STOP_FLAG = True 

fig = plot.figure(1)
fig.canvas.mpl_connect('close_event', plotWindowClosedEvent)

STOP_FLAG  = False 
f1 = 1000.0
while not STOP_FLAG:
	f1 *= 1.1
	waveform = [math.sin(2.0*math.pi*f1*i/sampleRate) for i in range(int(lenght*sampleRate))]
	timeBins = [1000.0 * i / sampleRate for i in range(len(waveform))]



	plot.cla()
	plot.plot(timeBins, waveform, label='Sine of %.1f Hz' % f1)
	plot.xlim([0,3])
	plot.grid(1)
	plot.xlabel('Time [ms]')
	plot.ylabel('Aplitude [.]')
	plot.legend(loc='upper right')
	plot.draw()
	try: plot.pause(0.2)
	except: pass 



