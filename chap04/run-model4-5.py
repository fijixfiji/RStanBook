#! -*- coding: utf-8 -*-
import pickle
import numpy as np
import pystan

# library(rstan)

# d <- read.csv(file='input/data-salary.txt')
# data <- list(N=nrow(d), X=d$X, Y=d$Y)
# fit <- stan(file='model/model4-5.stan', data=data, seed=1234)

# save.image(file='output/result-model4-5.RData')

d = np.genfromtxt(fname='input/data-salary.txt', delimiter=',', names=True, dtype=np.float)
data = {'N': d.size, 'X': d['X'], 'Y': d['Y']}
fit = pystan.stan(file='model/model4-5.stan', data=data, seed=1234)

with open('output/result-model4-5.pickle', 'wb') as f:
    # fitではなくて、stanmodelとfit.extract()を保存すべき？
    pickle.dump(fit, f, protocol=2)

# print(fit) # 4.4.7の出力
# seedを同じにしてるけど、微妙に値が違う。
