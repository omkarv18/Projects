getwd()
setwd("C:/Users/omkar/OneDrive/Documents/Analytical Tools Folder")

library('outliers')
library('ggplot2')
library('dplyr')

myData <- read.table("uscrime.txt", header = TRUE)

data <- data.frame(myData)

outlier_result <- grubbs.test(x = data$Crime, type = 10, opposite = FALSE, two.sided = FALSE)

outlier_result

sorted_df <- data[order(data$Crime), ]
head(sorted_df)

mean_value <- mean(data$Crime)

mean_value

std_value <- sd(data$Crime)

std_value