getwd()
setwd("C:/Users/omkar/OneDrive/Documents/Analytical Tools Folder")

library('qcc')
library('smooth')
library('stats')

myData <- read.table("temps.txt", header = TRUE)

data <- data.frame(myData)

vector_dates_all <- vector("list", length = 0)

vector_dates_all <- unlist(data[, 2:21])

dates_1996_2015 <- ts(vector_dates_all, start = c(1), frequency = 123)

exp_model <- es(dates_1996_2015, model = "AMA", loss = "MSE", initial = "optimal")

print(exp_model)

forecasts <- forecast(exp_model, h = 123)

forecast_var <- as.vector(forecasts$mean)

mu_forecasts <- mean(forecast_var[1:20])  # Use year_temps directly
std_forecasts <- sd(forecast_var[1:20])    # Use year_temps directly
cusum_forecasts <- cusum(forecast_var, center = mu_forecasts, std.dev = std_forecasts, head.start = 0, decision.interval = 10)

forecast_endofsummer <- as.numeric(0)

found = TRUE
for (i in 1:length(cusum_forecasts$neg)){
  if (cusum_forecasts$neg[i] < - 10 && found == TRUE){
    forecast_endofsummer <- i
    found = FALSE
  }
}

print(forecast_endofsummer)

