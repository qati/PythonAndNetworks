#random generalo modul importalasa
import random

# lista generalasa kulonobozo N-ekkel: N =[10, 30, 100, 300, ...]
N=sorted([10**i for i in range(1,6)]+[3*10**i for i in range(1,6)])

#sample number
ns=10

#ezekben fogom tarolni a mean-t es median-t
mean_range   = []
median_range = []

#vegigmegyek az N-eken
for i in range(len(N)):
    #ezekben lesznek az atlagok es medianok (ns darab)
    means   = []
    medians = []
    #adott N-re ns db. sample-t generalok
    for k in range(ns):
        #legeneralom az N db random szamot
        rnds = sorted([random.random() for j in range(N[i])])
        #kiszamolom az atlagot
        means.append(sum(rnds)/N[i])
        #kiszamolom a mediant
        if N[i]%2==0:
            medians.append((rnds[int(N[i]/2)]+rnds[int(N[i]/2)+1])/2)
        else:
            medians.append(rnds[int(N[i]/2)])
    # mean and median range
    mean_range.append(max(means)-min(means))
    median_range.append(max(medians)-min(medians))

#matplotlib importalasa a plotolashoz
import matplotlib.pyplot as plt

#plotolas
plt.loglog()
plt.plot(N, mean_range, 'o', label="Mean range")
plt.plot(N, median_range, 'x', label="Median range")
plt.xlabel("N")
plt.legend(loc=3)
plt.savefig("fig.pdf")