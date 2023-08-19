import numpy as np
from scipy.stats import binom
#no of questions
n = 20
#probability for heads  
p = 0.5  
binom_dist = binom(n, p)
k = 11  
cdf_value = binom_dist.cdf(k)
print("Probability of 11 or less questions answered correct:",end=" ")
p = f"CDF at k = {k}: {cdf_value}"
print(p)
print("Probability for 12 or more questions answered correct:",end=" ")
x = float(1) - float(cdf_value)
print(x)
