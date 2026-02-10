import numpy as np
scores=np.random.randint(50,101,size=(5,3))
mean_scores=scores.mean(axis=0)
print("original scores:\n",scores)
print("mean of each subject::\n",mean_scores)
print(" centered normalized scores :\n",scores-mean_scores)
