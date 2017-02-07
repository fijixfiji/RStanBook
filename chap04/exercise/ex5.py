#! -*- coding: utf-8 -*-
import numpy as np
import pystan

np.random.seed(123)
N1 = 30
N2 = 20
Y1 = np.random.normal(loc=0.0, scale=5.0, size=N1)
Y2 = np.random.normal(loc=1.0, scale=4.0, size=N2)

data = {'N1': N1, 'N2': N2, 'Y1': Y1, 'Y2': Y2}

stanmodel = pystan.StanModel(file='ex5.stan')
fit = stanmodel.sampling(data=data, seed=1234)
ms = fit.extract()

print(np.mean(ms['mu1'] < ms['mu2']))
# library(rstan)

# source('generate-data.R')

# data <- list(N1=N1, N2=N2, Y1=Y1, Y2=Y2)
# fit <- stan(file='ex5.stan', data=data, seed=1234)

# ms <- extract(fit)
# prob <- mean(ms$mu1 < ms$mu2)  #=> 0.9457
