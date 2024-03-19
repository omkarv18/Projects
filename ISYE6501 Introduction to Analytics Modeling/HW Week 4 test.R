getwd()
setwd("C:/Users/omkar/OneDrive/Documents/Analytical Tools Folder")

library('qcc')
library('smooth')
library('stats')

myData <- read.table("temps.txt", header = TRUE)

data <- data.frame(myData)

head(data)

temps_1996 <- ts(data$X1996, frequency = 1)

data_smooth <- lapply(data[, -1], function(year_temps){
  year_temps_ts <- ts(year_temps, frequency = 1)
  exp_model <- HoltWinters(year_temps_ts, gamma = FALSE, l.start = year_temps_ts[0], b.start = 0, seasonal = "additive")
  #exp_model <- es(year_temps_ts, model = "AAN", loss = "MSE", initial = "backcasting")
  #print(year_temps_ts)
  #print(exp_model$states)
  return(exp_model)
})

print(data_smooth)