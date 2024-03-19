getwd()
setwd("C:/Users/omkar/OneDrive/Documents/Analytical Tools Folder")

myData <- read.table("credit_card_data-headers.txt", header = TRUE)
data <- as.matrix(myData)

# Assigning the response variable
labels <- data[,11]

# Scaling the data using standardization
features <- scale(data[, 1:10])

#Building the custom knn model

k <- 12

num_rows <- nrow(features)
distances <- numeric(num_rows)

for (i in 1:nrow(features)) {
  current_row <- features[i, ]
  
  # Calculates the distance between the current row and all other rows
  current_distances <- sqrt(rowSums((current_row - features[-i, ])^2))
  
  # Store the distances in the 'distances' vector
  distances <- current_distances
  #distances <- sqrt(rowSums((as.matrix(features[-i, 1:10]) - as.numeric(features[i, 1:10]))^2))
  neighbor_indices <- order(distances)[1:k]
  neighbor_labels <- labels[neighbor_indices + 1]
  #Finding the majority of values with nearest distance
  mean_val <- mean(as.numeric(neighbor_labels))
  classification <- round(mean_val, 0)
  predictions[i] <- classification
  print(mean_val)
  print(round(mean_val))
  print(classification)
  
  #print(as.matrix(neighbor_labels))
  
  
}
print(predictions)
print(labels)
accuracy <- sum(predictions == labels)  / length(predictions)


head(data)
head(features)
#cat(labels)
#cat(predictions)
#cat(predictions == labels)
cat("Accuracy:", accuracy, "\n")
