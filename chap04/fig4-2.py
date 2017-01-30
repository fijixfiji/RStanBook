import numpy as np
import matplotlib.pyplot as plt

# library(ggplot2)

# d <- read.csv(file='input/data-salary.txt')
# p <- ggplot(data=d, aes(x=X, y=Y))
# p <- p + theme_bw(base_size=18)
# p <- p + geom_point(shape=1, size=3)
# ggsave(file='output/fig4-2.png', plot=p, dpi=300, w=4, h=3)

d = np.genfromtxt(fname='input/data-salary.txt', delimiter=',', names=True, dtype=np.float)
plt.scatter(d['X'], d['Y'])
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('output/fig4-2-py.png')
