#! -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pystan

# library(rstan)
# library(ggplot2)

# d <- read.csv(file='input/data-salary.txt')
# X_new <- 23:60
# data <- list(N=nrow(d), X=d$X, Y=d$Y, N_new=length(X_new), X_new=X_new)
# fit <- stan(file='model/model4-4.stan', data=data, seed=1234)
# ms <- rstan::extract(fit)

d = np.genfromtxt(fname='input/data-salary.txt', delimiter=',', names=True, dtype=np.float)
X_new = np.arange(23, 61)
data = {'N': d.size, 'X': d['X'], 'Y': d['Y'], 'N_new': X_new.size, 'X_new': X_new}
fit = pystan.stan(file='model/model4-4.stan', data=data, seed=1234)

# data.frame.quantile.mcmc <- function(x, y_mcmc,
#   probs=c(2.5, 25, 50, 75, 97.5)/100) {
#   qua <- apply(y_mcmc, 2, quantile, probs=probs)
#   d <- data.frame(X=x, t(qua))
#   colnames(d) <- c('X', paste0('p', probs*100))
#   return(d)
# }

# ggplot.5quantile <- function(data) {
#   p <- ggplot(data=data, aes(x=X, y=p50))
#   p <- p + theme_bw(base_size=18)
#   p <- p + geom_ribbon(aes(ymin=p2.5, ymax=p97.5), fill='black', alpha=1/6)
#   p <- p + geom_ribbon(aes(ymin=p25, ymax=p75), fill='black', alpha=2/6)
#   p <- p + geom_line(size=1)
#   return(p)
# }

# customize.ggplot.axis <- function(p) {
#   p <- p + labs(x='X', y='Y')
#   p <- p + scale_y_continuous(breaks=seq(from=200, to=1400, by=400))
#   p <- p + coord_cartesian(xlim=c(22, 61), ylim=c(200, 1400))
#   return(p)
# }

confidence_interval = fit.summary()['summary'][23:23 + 38][:, 3:8]
prediction_interval = fit.summary()['summary'][23 + 38:23 + 38 + 38][:, 3:8]

# d_est <- data.frame.quantile.mcmc(x=X_new, y_mcmc=ms$y_base_new)
# p <- ggplot.5quantile(data=d_est)
# p <- p + geom_point(data=d, aes(x=X, y=Y), shape=1, size=3)
# p <- customize.ggplot.axis(p)
# ggsave(file='output/fig4-8-left-2.png', plot=p, dpi=300, w=4, h=3)

plt.fill_between(X_new, confidence_interval[:, 0], confidence_interval[:, 4], alpha=0.1, facecolor='black')
plt.fill_between(X_new, confidence_interval[:, 1], confidence_interval[:, 3], alpha=0.2, facecolor='black')
plt.plot(X_new, confidence_interval[:, 2])
plt.xlabel('X')
plt.ylabel('Y')
plt.ylim(200, 1400)
plt.xlim(22, 61)
plt.savefig('output/fig4-8-left-py.png')

# d_est <- data.frame.quantile.mcmc(x=X_new, y_mcmc=ms$y_new)
# p <- ggplot.5quantile(data=d_est)
# p <- p + geom_point(data=d, aes(x=X, y=Y), shape=1, size=3)
# p <- customize.ggplot.axis(p)
# ggsave(file='output/fig4-8-right-2.png', plot=p, dpi=300, w=4, h=3)

plt.fill_between(X_new, prediction_interval[:, 0], prediction_interval[:, 4], alpha=0.1, facecolor='black')
plt.fill_between(X_new, prediction_interval[:, 1], prediction_interval[:, 3], alpha=0.2, facecolor='black')
plt.plot(X_new, confidence_interval[:, 2])
plt.xlabel('X')
plt.ylabel('Y')
plt.ylim(200, 1400)
plt.xlim(22, 61)
plt.savefig('output/fig4-8-right-py.png')
