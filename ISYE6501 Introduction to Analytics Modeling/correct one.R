getwd()
setwd("C:/Users/omkar/OneDrive/Documents/Analytical Tools Folder")

myData <- read.table("credit_card_data-headers.txt", header = TRUE)
data <- as.data.frame(myData)

# Convert the response variable to a factor, so that it is a categorical variable
data$response <- as.factor(data[, 11])

# Split the dataset into scaled standardized features and labels (I found out later that
#kknn has the option to scale)
features <- scale(data[, 1:10])
labels <- data$response

library(kknn)

num_rows <- nrow(features)
accuracy_matrix <- matrix(NA, nrow = num_rows, ncol = 1)  # Matrix to store accuracy values

for (i in 1:num_rows) {
  # Split the data into training and testing sets, where the training set is all the values except
  #the current value, and the test set is the current value. Both sets have to be dataframes in
  #order to be inputted into the kknn model, so I couldn't use the syntax given in the question. 
  
  train_indices <- setdiff(1:num_rows, i)
  train_data <- data[train_indices, ]
  test_data <- data[i, ]
  
  # Build the k-nearest neighbors model, I found out later that 
  knn_model <- kknn(response ~ ., train_data, test_data, k = 5, scale = TRUE)
  
  # Make predictions on the test data
  predictions <- fitted(knn_model)
  
  # Calculate accuracy (should be either 1 or 0, since there's only 1 data point)
  accuracy <- sum(predictions == test_data$response) / length(predictions)
  
  # Store accuracy in the matrix
  accuracy_matrix[i, ] <- accuracy
}

# Print the accuracy matrix
total_accuracy <- sum(accuracy_matrix) / length(accuracy_matrix)
print(total_accuracy)

