#! -*- coding:utf-8 -*-
import numpy as np
from sklearn import linear_model

# d <- read.csv(file='input/data-salary.txt')
# res_lm <- lm(Y ~ X, data=d)
# X_new <- data.frame(X=23:60)
# conf_95 <- predict(res_lm, X_new, interval='confidence', level=0.95)
# pred_95 <- predict(res_lm, X_new, interval='prediction', level=0.95)

d = np.genfromtxt(fname='input/data-salary.txt', delimiter=',', names=True, dtype=np.float)
lm = linear_model.LinearRegression()
lm.fit(d['X'].reshape(d.size, 1), d['Y'])

print('Intercept: ' + str(lm.intercept_))
print('Coefficients: ' + str(lm.coef_[0]))
# 一応p.38の1 行目の数値はとは一致した。
# 信頼区間と予測区間については、まだ書いてない
