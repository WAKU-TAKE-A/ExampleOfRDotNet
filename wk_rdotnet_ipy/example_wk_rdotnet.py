# -*- coding: utf-8 -*-

"""
Example of R.Net (for 64bit)

* Set IRONPYTHON_HOME and R_HOME.
"""

import rdotnet as r

#
# Example of NumericMatrix.
#
mat = r.evaluate("mat <- matrix(1:100, nrow=10)", "numeric")
print(type(mat))
#
# Example of NumericVector.
#
vec = r.evaluate("vec <- rnorm(1000)", "numeric")
mean = r.evaluate("mean <- mean(vec)", "numeric")
print("Mean is {0}".format(mean[0]))
hst = r.evaluate("hst<-hist(vec)", "list")
hst_counts = r.asNumeric(hst["counts"])
print("counts : ")
print(list(hst_counts))
raw_input("Push any key.")
r.evaluate("dev.off()")
#
# Example of DataFrame.
#
csv = r.evaluate("csv<-read.csv('sample.csv', stringsAsFactors=F)", "dataframe")
print("Name : ")
print(list(csv["Name"]))
print("Height : ")
print(list(csv["Height"]))
print("csv[0, 'Weight'] : ")
print(csv["Weight"][0])
