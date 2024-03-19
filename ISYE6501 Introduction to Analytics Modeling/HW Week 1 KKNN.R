getwd()
setwd("C:/Users/omkar/OneDrive/Documents/Analytical Tools Folder")

library(kknn)

myData <- read.table("credit_card_data-headers.txt", header = TRUE)
data <- as.data.frame(myData)

# Convert the response variable to a factor
#data$response <- as.factor(data[,11])

# Split the dataset into features and labels
#features <- data[, 1:10]
#labels <- data$response

# Split the data into training and testing sets
train_indices <- sample(1:nrow(data), size = 0.8 * nrow(data))
train_data <- data[train_indices, ]
test_data <- data[-train_indices, ]

colnames(train_data[, 1:10])

k_values <- c(1, 3, 5, 7, 9)

# Build the k-nearest neighbors model
#cv_results <- cv.kknn(train_data[, 1:10], train_data$response, kmax = 20, kmin = 3, kernel = "optimal", distance = 2, scale = TRUE, folds = 10)
#cv_results <- cv.kknn(formula = train_data$response ~ ., data = train_data, kmax = max(k_values), kernel = "optimal", distance = 2, scale = TRUE, kcv = 10)
#cv_results <- cv.kknn(formula = data[,11] ~ ., data = train_data, kmax = max(k_values), kernel = "optimal", distance = 2, scale = TRUE, kcv = 10)
cv_results <- cv.kknn(formula = train_data$R1 ~ ., data = train_data, kcv = 10)
#performance_metrics <- cv_results$performance
#performance_metrics
