import numpy as np

def normal_pdf(x, mu=0, sigma=1):
    deominator = np.sqrt(2*np.pi) * sigma
    numerator = np.exp(-(x-mu)**2/(2*sigma**2))
    return numerator / deominator

print(normal_pdf(0, 1.6, 0.489898))