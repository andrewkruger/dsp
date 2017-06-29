[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> 34.2% of men are between 5'10" (177.8cm) and 6'1" (185.42cm) to be eligible to be a Blue Man.

```
from scipy.stats import norm

low = norm.cdf(177.8, loc=178, scale=7.7)
high = norm.cdf(185.42, loc=178, scale=7.7)
p = (high-low)*100
print("Percentage eligible: %.1f%%" % p)
```
