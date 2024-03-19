getwd()
setwd("C:/Users/omkar/OneDrive/Documents/Analytical Tools Folder")

library('qcc')

myData <- read.table("temps.txt", header = TRUE)

data <- data.frame(myData)

vector_temperatures <- vector("list", length = 0)

change_year <- lapply(data[, -1], function(year_temps) {
  mu <- mean(year_temps[1:20])  # Use year_temps directly
  std <- sd(year_temps[1:20])    # Use year_temps directly
  cusum <- cusum(year_temps, center = mu, std.dev = std, head.start = 0, decision.interval = 10)
  change_dates <- vector("list", length = 0)
  
  
  found = TRUE
  for (i in 1:length(cusum$neg)){
    if (cusum$neg[i] < - 10 && found == TRUE){
      change_dates <- data$DAY[i]
      print(i)
      print(mean(cusum$data[1:i]))
      change_dates <- append(change_dates, mean(cusum$data[1:i]))
      found = FALSE
    }
  }
  return(change_dates)
})

new_change_year <- as.data.frame(change_year)

for (j in 1:length(new_change_year)){
  vector_temperatures <- append(vector_temperatures, new_change_year[2, j])
}
vector_temperatures <- as.numeric(vector_temperatures)

print(vector_temperatures)

mu = mean(vector_temperatures[1:5])
std = sd(vector_temperatures[1:5])

warmer <- cusum(vector_temperatures, center = mu, std.dev = std, head.start = 0, decision.interval = 2)

#mu <- mean(data$X1996[1:20])  # Use year_temps directly
#std <- sd(data$X1996[1:20])

#q <- cusum(data$X1996, center = mu, std.dev = std, head.start = 0, decision.interval = 10)
#print(q$neg)