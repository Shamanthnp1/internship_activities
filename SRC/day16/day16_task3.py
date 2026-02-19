import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
original_data = np.random.exponential(scale=2, size=10000)

plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
sns.histplot(original_data, kde=True)
plt.title("Original Data (Right-Skewed)")

sample_means = []
for i in range(1000):
    sample = np.random.choice(original_data, size=30)
    sample_means.append(np.mean(sample))

sample_means = pd.Series(sample_means)
plt.subplot(1,2,2)
sns.histplot(sample_means, kde=True)
plt.title("Distribution of Sample Means (n=30)")
plt.tight_layout()
plt.show()
print("\nOriginal Data Mean:", np.mean(original_data))
print("\nMean of Sample Means:", np.mean(sample_means))
print("\nStandard Deviation of Sample Means:", np.std(sample_means))