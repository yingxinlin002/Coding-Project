library(animation)
## it takes several seconds if 'redraw = TRUE'
ani.options(nmax = 400, 1)
par(mar = c(3, 2.5, 0.5, 0.2), pch = 20, mgp = c(1.5, 0.5, 0))
buffon.needle()
## this will be faster
ani.options(nmax = 400, 1)
buffon.needle(redraw = FALSE)
new <- c(42.1, 41.3, 42.4, 43.2, 41.8, 41.0, 41.8, 42.8, 42.3, 42.7)
old <- c(42.7, 43.8, 42.5, 43.1, 44.0, 43.6, 43.3, 43.5, 41.7, 44.1)
sd(new)^2
