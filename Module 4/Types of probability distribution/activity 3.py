
import scipy.stats as stats

prob1 = 1-stats.poisson.cdf(20, 15)

print(prob1)

prob2 = stats.poisson.cdf(21, 15) - stats.poisson.cdf(16, 15)

print(prob2)
