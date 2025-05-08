---
    Author: Zeke Vespie
    Topic: Colors of Noise Project
    Course: TN Tech PHYS4130
    Term: Spring 2025
---

# WRITEUP

## ABSTRACT

Noise, often referred to contextually as background for physicists, generally is defined as a signal or process produced by random variations in something. There are many different kinds of noise, and one way to differentiate these noises is by how their power spectrum changes over a range of frequencies. For the case of crudely equal power over this range the frequencys of all sounds are equal in power; this is a signal that is analogous to white light, which is why it's known as white noise. Other colors of noise have different power spectra that are scaled based on the frequency. In this project, I look at different colors of noise and what power spectra they use, along with making audible files of what these colors of noise sound like.

## PROJECT

### WHITE NOISE SIGNAL AND POWER SPECTRUM

The writeup for this project describes the process of creating a white noise signal very simply as taking a random selection of points from a normal or gaussian distribution. This was difficult for me at first, but eventually I found out that Numpy has a function specifically designed to do this exact thing, so when using that this part was trivially simple. Below you can see the first spectrum of white noise that I produced.

<figure>
  <img src=Figures/figure1.png>
    <figcaption>Plot of Amplitude of white noise signal over 5 seconds, with a number of points of N = 1024</figcaption>
</figure>
<p>&nbsp;</p> 

The next thing I needed to do was look at the power spectrum. According to the writeup, the power was described by

```math
P = |\tilde{y}|^2
```

where y is the amplitude of the signal and the tilde refers to the Fourier Transform of it. As it turns out, Fourier Transforms are as simple as functions in Numpy as well, although the one that I use is the Fast Fourier Transform (FFT). I don't know what difference this has other than being fast, but I assume it is fine to use. 

Using these will of course result in real and imaginary components, and before I use these to calculate the power I will do another part of the project, which is to recognize the symmetries with these parts separately. Both of these plotted with frequency are below.

<figure>
  <img src=Figures/figure2.png>
    <figcaption>Real component of the Fourier Transformed Amplitude against frequency</figcaption>
</figure>
<p>&nbsp;</p> 

<figure>
  <img src=Figures/figure3.png>
    <figcaption>Imaginary component of the Fourier Transformed Amplitude against frequency</figcaption>
</figure>
<p>&nbsp;</p> 

Firstly, it is important to note that I believe these frequencies are not correct. I used a special function that I think is supposed to take the number of points N and turn it into the frequencies for those points, but there is obviously some problem because there are negative frequencies, and their scale is very small. This bothers me, but it already took me too long to do this part so I will just move on.

As it pertains to how the symmetries are, it is fairly obvious what they are: for the real component the graph is symmetric across the y axis, and for the imaginary component it is symmetric accross the origin, i.e. the real component is an even function and the imaginary component is an odd function.

Now back to the power. I calculated the power by using the following formula:

```math
P = (Re(\tilde{y}))^2 + (Im(\tilde{y}))^2
```
It took me until the end of the assignment that this is the same as (if not a more inefficient version of) using the Numpy function np.abs() and squaring it. I did not know that this worked with imaginary numbers, so I didn't use it in some parts; I could replace it everywhere, but it shows my learning process so I left it in. Either way, the spectrum below will be produced. Note that I have technically cut off half of the spectrum, but I do this so that I don't worry about negative frequencies.

<figure>
  <img src=Figures/figure4.png>
    <figcaption>Power of the White signal, still with N = 1024</figcaption>
</figure>
<p>&nbsp;</p> 

While it is unsatisfying, it seems like the power is crudely constant on average, as it is supposed to.

### OTHER NOISE SIGNALS AND POWER SPECTRA

Other colors of noise have power spectra that are proportional in some way to the frequency. This proportionality is the only way that I was able to find to actually get signals for different colors of noise: I would take a power spectrum from white noise, scale it based on the relationship it should have with frequency, then use a reverse Fourier Transform to get what the signal should be. For context, here is a table I made of how each scaling manifests, keeping in mind that the amplitude is scaled by the square root of the power scaling for obvious reasons.

| **Noise Color**     | **Power Scaling**        | **Amplitude Scaling**         |
|---------------------|--------------------------|-------------------------------|
| White               |  None                    |  None                         |
| Pink                |  1/f                     |  1/f^(1/2)                    |
| Brown               |  1/f^2                   |  1/f                          |
| Blue                |  f                       |  f^(1/2)                      |
| Purple              |  f^2                     |  f                            |

This scaling is fairly straight forward, with a few things kept in mind. For one, technically this process produces a real and an imaginary component of the signal. The real component is all I care about, because you can't hear imaginary audio. For two, I start normalizing the spectra at this point, which doesn't affect the shape but does effect the size. The was mostly arbitrary at the time, but it actually became important later on when it came to making the audio files. I don't explain why in this report, but an attempt at an explanation is in my workbook.

I will first show a plot of power vs. frequency, then the log-log plot of that with a linear fit. This fit is supposed to correspond to the relationship that each color of noise has with frequency, in particular the slope of the fitted line is the exponent of f that is being used to scale the power. They are as follows, in the same order as the table above, with N = 1024 in all cases:

<figure>
  <img src=Figures/figure5.png>
    <figcaption>Power of the Pink signal</figcaption>
</figure>
<p>&nbsp;</p> 

<figure>
  <img src=Figures/figure6.png>
    <figcaption>Log-Log Plot of the Power of the Pink signal</figcaption>
</figure>
<p>&nbsp;</p> 

<figure>
  <img src=Figures/figure7.png>
    <figcaption>Power of the Brown signal</figcaption>
</figure>
<p>&nbsp;</p> 

<figure>
  <img src=Figures/figure8.png>
    <figcaption>Log-Log Plot of the Power of the Brown signal</figcaption>
</figure>
<p>&nbsp;</p> 

<figure>
  <img src=Figures/figure9.png>
    <figcaption>Power of the Blue signal</figcaption>
</figure>
<p>&nbsp;</p> 

<figure>
  <img src=Figures/figure10.png>
    <figcaption>Log-Log Plot of the Power of the Blue signal</figcaption>
</figure>
<p>&nbsp;</p> 

<figure>
  <img src=Figures/figure11.png>
    <figcaption>Power of the Purple signal</figcaption>
</figure>
<p>&nbsp;</p> 

<figure>
  <img src=Figures/figure12.png>
    <figcaption>Log-Log Plot of the Power of the Purple signal</figcaption>
</figure>
<p>&nbsp;</p> 

Using these, I was able to produce the signals corresponding to each of these power spectra, and they are as follows, again in the same order as the table above:

<figure>
  <img src=Figures/figure13.png>
    <figcaption>Pink Noise Signal, contructed from relevant Power spectrum</figcaption>
</figure>
<p>&nbsp;</p> 

<figure>
  <img src=Figures/figure14.png>
    <figcaption>Brown Noise Signal, contructed from relevant Power spectrum</figcaption>
</figure>
<p>&nbsp;</p> 

<figure>
  <img src=Figures/figure15.png>
    <figcaption>Blue Noise Signal, contructed from relevant Power spectrum</figcaption>
</figure>
<p>&nbsp;</p> 

<figure>
  <img src=Figures/figure16.png>
    <figcaption>Purple Noise Signal, contructed from relevant Power spectrum</figcaption>
</figure>
<p>&nbsp;</p> 

These are mostly as I expect, with the more sharp spectra being the ones with a higher exponent in the frequency scaling.

### AUDIBLE COLORS OF NOISE

By using primarily the stackoverflow links in my citations and a few other sources that I forgot to write down from the SciPy manual, I eventually came up with a way to convert the files that I produced into .wav files, with a few minor issues. One is that the white and pink noise sound virtually identical to me, and another is that the brown noise unfortunately has blips of loud bass in the middle of the sound that I don't understand and don't know how to remove.

In order to make these work, the only relevant piece of information is that I had to dramatically increase the value of N to 2,097,152 or 2 to the power of 21. The specific choice was arbitrary, but I had to pick a pretty large number for the sounds to be (mostly) smooth. To be honest, anything else about the code I used in this section is mostly lost on me, though I do attempt to explain some of it in the workbook.

Here are the noises that I managed to make as links.

[Click to hear White Noise](Noises/white_noise.wav)

[Click to hear Pink Noise](Noises/pink_noise.wav)

[Click to hear Brown Noise](Noises/brown_noise.wav)

[Click to hear Blue Noise](Noises/blue_noise.wav)

[Click to hear Purple Noise](Noises/purple_noise.wav)

## DISCUSSION OF RESULTS

I think this project actually turned out fairly well; I mangaged to create some fairly good spectra, with my only real complaint being the frequencies being incredibly inaccurate. This didn't disasterously affect the results, at least not that I can see, but it is unfortunate.

The power spectra lining up with slopes like they should have is not really proof of the method working to produce the colors of noise they are supposed too, but by the sound of the links provided I think it's safe to say that the program is doing mostly the correct thing. Considering the fact that the original writeup doesn't even mention the other colors of noise, I'd say this is a good attempt at a thorough analysis of the material.

## CITATIONS

https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html

https://stackoverflow.com/questions/10357992/how-to-generate-audio-from-a-numpy-array

https://stackoverflow.com/questions/40782159/writing-wav-file-using-python-numpy-array-and-wave-module?utm_source=chatgpt.com

https://zeptoblog.com/2024/04/21/colored-noise-frequency-domain-filtering.html

https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html

https://en.wikipedia.org/wiki/Colors_of_noise