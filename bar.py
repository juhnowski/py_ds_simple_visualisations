from matplotlib import pyplot as plt
import numpy as np

movies = ["Witt-java-1","py_ds_simple_visualisations","Witt-java","eflute"]
num_commits = [4,3,2,1]

xs = [i+0.1 for i,_ in enumerate(movies)]

plt.bar(xs,num_commits)
plt.ylabel("Commits")
plt.yticks(np.arange(min(num_commits), max(num_commits)+1, 1.0))
plt.title("My GitHub February commits")

plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)
plt.show()