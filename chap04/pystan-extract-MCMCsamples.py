#! -*- coding: utf-8 -*-
import pickle
import numpy as np

# load('output/result-model4-5.RData')

# ms <- rstan::extract(fit)
# N_mcmc <- length(ms$lp__)
# y50_base <- ms$a + ms$b * 50
# y50 <- rnorm(n=N_mcmc, mean=y50_base, sd=ms$sigma)
# d_mcmc <- data.frame(a=ms$a, b=ms$b, sigma=ms$sigma, y50_base, y50)

with open('output/result-model4-5.pickle', 'rb') as f:
    stanmodel = pickle.load(f)
    fit = pickle.load(f)

ms = fit.extract()
N_mcmc = len(ms['lp__'])
y50_base = ms['a'] + ms['b'] * 50
y50 = np.random.normal(loc=y50_base, scale=ms['sigma'])
