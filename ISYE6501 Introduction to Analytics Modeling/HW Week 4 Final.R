getwd()
setwd("C:/Users/omkar/OneDrive/Documents/Analytical Tools Folder")

library('qcc')
library('smooth')
library('stats')

myData <- read.table("temps.txt", header = TRUE)

data <- data.frame(myData)

vector_dates <- vector("list", length = 0)

change_year <- lapply(data[, -1], function(year_temps) {
  mu <- mean(year_temps[1:20])  # Use year_temps directly
  std <- sd(year_temps[1:20])    # Use year_temps directly
  cusum <- cusum(year_temps, center = mu, std.dev = std, head.start = 0, decision.interval = 10)
  change_dates <- as.numeric(0)
  
  
  found = TRUE
  for (i in 1:length(cusum$neg)){
    if (cusum$neg[i] < - 10 && found == TRUE){
      change_dates <- i
      found = FALSE
    }
  }
  return(change_dates)
})

new_change_year <- as.data.frame(change_year)

for (j in 1:length(new_change_year)){
  vector_dates <- append(vector_dates, new_change_year[1, j])
}
vector_dates <- as.numeric(vector_dates)

mean_vector_dates <- mean(vector_dates)
print(mean_vector_dates)

dates_1996_2015 <- ts(vector_dates, frequency = 1)

exp_model <- es(dates_1996_2015, model = c("ANN", "AAN", "AAA", "MAA", "MMM", "AMA", "MNN", "MMN"), loss = "MSE", initial = "optimal")

summary(exp_model)

forecasts <- forecast(exp_model, h = 10)

dates_forecasts <- c(vector_dates, as.vector(forecasts$mean))

x <- 1:30

y_limits <- c(0, 150)

threshold_x <- 20

# Create a vector to store colors
point_colors <- ifelse(x > threshold_x, "red", "blue")
plot(x, dates_forecasts, type = "b", col = point_colors, pch = 19,
     xlab = "Time (years)", ylab = "Date of End of Unofficial Summer", main = "End of unofficial summer 1995-2015 with forecasts")

