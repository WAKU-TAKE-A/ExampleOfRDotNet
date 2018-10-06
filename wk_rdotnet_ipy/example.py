# -*- coding: utf-8 -*-

"""
Example of R.Net (for 64bit)
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
hst = r.evaluate("hst <- hist(vec)", "list")
hst_counts = r.asNumeric(hst["counts"])
print(list(hst_counts))
raw_input("Push any key.")
r.evaluate("dev.off()")
#
# Example of DataFrame.
#
csv = r.evaluate("csv <- read.csv('example.csv', stringsAsFactors=F)", "dataframe")
print("Name : ")
print(list(csv["Name"]))
print("Height : ")
print(list(csv["Height"]))
#
# Example of Function.
#
func = r.eval("func <- function(var){ var + 10 }", "function")
vec2 = r.eval("vec2 <- c(1, 2, 3, 4, 5, 6, 7, 8, 9)")
ret = r.runFunction(func, [vec2], "numeric")
print(list(ret))
