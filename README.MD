[![Build Status](https://www.travis-ci.com/jamiebarker0310/Rational-Histograms.svg?branch=main)](https://www.travis-ci.com/jamiebarker0310/Rational-Histograms) 
# Rational-Histograms
Rational Histograms is a Python package that fits "sensible" bins to histograms as an alternative to the default methods used in MatplotLib and Seaborn.

The library finds the user bin sizes for a data to try and meet the following criteria:

- **Interpretable** - All bins sizes will be values that are easily to combine and multiply (e.g 0.02, 2.5, 100, 5000).
- **Centred** - Bins start at zero to ensure easy reading.
- **Smooth** - The algorithm attempts to find a smooth histogram using cubic splining and bend energy to estimate smoothness.

This is useful for when wanting to present simple findings in an easy to understand manner. Below is an example of how the package can be used in conjunction with the Seaborn package.
<img src="https://user-images.githubusercontent.com/37461124/106815523-e554b600-666b-11eb-9cae-349dfc06df7c.png" width="400"/>

