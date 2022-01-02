data=read.csv('data_new.csv')

plot(x = data$y,y = data$x,
     xlab = "Versuch",
     ylab = "q",
     main = "Millikan-Versuch"
)