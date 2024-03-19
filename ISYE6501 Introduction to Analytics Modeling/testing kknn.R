getwd()
setwd("C:/Users/omkar/OneDrive/Documents/Analytical Tools Folder")

library(kknn)
library(caret)
library(knitr)
library(kableExtra)

myData <- read.table("credit_card_data-headers.txt", header = TRUE)

data <- data.frame(myData)

set.seed(200) #set seed for the right data selection in test and training sets

train_indices <- sample(1:nrow(data), size = 0.8 * nrow(data))

train_data <- data[train_indices, ]
test_data <- data[-train_indices, ]

train_data$R1 <- as.factor(train_data$R1)
test_data$R1 <- as.factor(test_data$R1)

final_model <- kknn(R1 ~ ., train = train_data, test = test_data[, 1:10], 
                      k = 1, 
                      kernel = "rectangular",  # Use the character string
                      distance = 1, 
                      scale = TRUE)

accuracy2 <- sum(final_model$fitted.values == test_data$R1) / nrow(test_data)