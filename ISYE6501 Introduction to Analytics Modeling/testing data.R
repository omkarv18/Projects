getwd()
setwd("C:/Users/omkar/OneDrive/Documents/Analytical Tools Folder")

library(kknn)

myData <- read.table("credit_card_data-headers.txt", header = TRUE)

data <- data.frame(myData)

set.seed(200)

train_indices <- sample(1:nrow(data), size = 0.8 * nrow(data))

train_data <- data[train_indices, ]
test_data <- data[-train_indices, ]

train_data$R1 <- as.factor(train_data$R1)
test_data$R1 <- as.factor(test_data$R1)

formula <- as.formula("R1 ~ .")

model_final <- kknn(formula, data = train_data, kernel = "rectangular", k = 11, scale = TRUE)

# Specify the columns for prediction, excluding the target variable
predictions <- predict(model_final, newdata = test_data[, -11])

accuracy <- sum(predictions == test_data$R1) / nrow(test_data)
