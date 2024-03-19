myData <- read.table("credit_card_data-headers.txt", header = TRUE)
data <- as.data.frame(myData)

# Convert the response variable to a factor
data$response <- as.factor(data[,11])

# Split the dataset into features and labels
features <- data[, 1:10]
labels <- data$response

# Split the data into training and testing sets

train_indices <- sample(1:nrow(data), size = 0.8 * nrow(data))
train_data <- data[train_indices, ]
test_data <- data[-train_indices, ]

#Building the custom knn model

k <- 7

for (i in 1:nrow(test_data)) {
  distances <- sqrt(rowSums((as.matrix(train_data[, 1:10]) - as.numeric(test_data[i, 1:10]))^2))
  nearest_points <- order(distances)[1:k]
}