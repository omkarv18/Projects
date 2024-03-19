getwd()
setwd("C:/Users/omkar/OneDrive/Documents/Analytical Tools Folder")

library(kknn)
library(caret)
library(knitr)
library(kableExtra)

myData <- read.table("credit_card_data-headers.txt", header = TRUE)

data <- data.frame(myData)

set.seed(123)

# Percentage split for train, validation, and test
train_percent <- 0.7
validation_percent <- 0.15
test_percent <- 0.15

# Create an index vector for the split
index <- createDataPartition(data$R1, p = train_percent, list = FALSE, times = 1)

# Split the data into train_data and temp_data
train_data <- data[index, ]
train_data <- as.data.frame(train_data)
temp_data <- data[-index, ]

# Create another index vector for the second split
index <- createDataPartition(temp_data$R1, p = validation_percent / (1 - train_percent), 
                             list = FALSE, 
                             times = 1)

# Split the temp_data into validation_data and test_data
validation_data <- temp_data[index, ]
test_data <- temp_data[-index, ]
validation_data <- as.data.frame(validation_data)
test_data <- as.data.frame(test_data)

# Define a grid of hyperparameters
hyperparameters_grid <- expand.grid(k = c(1, 3, 5, 7, 9, 11, 13, 15, 17, 19), kernel = c("rectangular", "triangular", "epanechnikov", "optimal"), distance = c(1, 2))

# Initialize variables to store the best model and its accuracy
best_model <- NULL
best_accuracy <- 0
best_kernel <- NULL
best_k <- 0
best_dist <- NULL

for (i in 1:nrow(hyperparameters_grid)) {
  # Convert the kernel from the grid to a character string
  current_kernel <- as.character(hyperparameters_grid$kernel[i])
  
  # Train a kknn model with the current hyperparameters on the training set
  current_model <- kknn(R1 ~ ., train = train_data, test = validation_data, 
                        k = hyperparameters_grid$k[i], 
                        kernel = current_kernel,  # Use the character string
                        distance = hyperparameters_grid$distance[i], 
                        scale = TRUE)
  
  # Calculate accuracy
  accuracy <- sum(current_model$fitted.values == validation_data$R1) / nrow(validation_data)
  
  # Check if this model has the highest accuracy
  if (accuracy > best_accuracy) {
    best_accuracy <- accuracy
    best_model <- current_model
    best_kernel <- current_kernel
    best_k <- hyperparameters_grid$k[i]
    best_dist <- hyperparameters_grid$distance[i]
  }
}

# ...
str(best_model)

# Use the best model for predictions on the test set
test_predictions <- predict(best_model, newdata = test_data[, 1:10])

accuracy2 <- sum(test_predictions == test_data$R1) / nrow(test_data)
