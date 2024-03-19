getwd()
setwd("C:/Users/omkar/OneDrive/Documents/Analytical Tools Folder")

myData <- read.table("credit_card_data-headers.txt", header = TRUE)
data <- as.data.frame(myData)

# Convert the response variable to a factor
data$response <- as.factor(data[,11])

# Split the dataset into scaled features and labels
features <- scale(data[, 1:10])
labels <- data$response


for (i in 1:nrow(features)) {
  # Split the data into training and testing sets
  
  train_indices <- setdiff(1:nrow(features), i)
  train_data <- features[train_indices, ]
  test_data <- features[i, ]
  # Build the k-nearest neighbors model
  knn_model <- kknn(response ~ ., train_data, test_data, k = 5)
  
  # Make predictions on the test data
  predictions <- predict(knn_model, test_data)
  
  # Calculate accuracy
  accuracy <- sum(predictions == labels[i]) / length(predictions)
  cat("Accuracy:", accuracy, "\n")
  

  
}