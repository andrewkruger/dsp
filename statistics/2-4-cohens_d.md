[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> Non-first born babies have a mean total weight that is 0.12lbs higher than first born babies.  However, the Cohen's *d* for this comparison is 0.089.  This is 3.1x greater than the Cohen's *d* for the pregnancy length difference between these two groups, which was 0.029.  While this is an increase in effect size, there still isn't a significant difference between first born and non-first born babies as this is still a small value.  Visual inspection of the histograms indicates this is a reasonable Cohen's *d* as there is no obvious difference between the histograms of the two data sets.  

Code used to get answer:

```
import thinkplot
import nsfg
import thinkstats2
import math
import first 

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

firsts_hist = thinkstats2.Hist(firsts.totalwgt_lb)
others_hist = thinkstats2.Hist(others.totalwgt_lb)

#Inspect data
wd = 0.0225
thinkplot.PrePlot(2)
thinkplot.Hist(firsts_hist, align='right', width=wd)
thinkplot.Hist(others_hist, align='left', width=wd)
thinkplot.Show(xlabel='Pounds', ylabel='Frequency')


def CohenEffectSize(group1, group2):
    diff = abs(group1.mean() - group2.mean())
    var1, var2 = group1.var(), group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    return diff / math.sqrt(pooled_var)

print 'Total Weight, First born:',firsts.totalwgt_lb.mean()
print 'Total Weight, Non-first born:',others.totalwgt_lb.mean()
print 'Diff( First - Non-first ):',firsts.totalwgt_lb.mean() - others.totalwgt_lb.mean()
    
tw_cohens = CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
print 'Total Weight Cohen\'s d:',tw_cohens

pl_cohens = CohenEffectSize(firsts.prglngth, others.prglngth)
print 'Pregnancy Length Cohen\'s d:',pl_cohens

print 'totalwgt / prglngth:',tw_cohens/pl_cohens
```
