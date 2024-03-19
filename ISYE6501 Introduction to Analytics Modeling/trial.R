#Code used for Question 3.1

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

k_values <- c(1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25)  # You can specify any range of values

# Define a range of distance metrics to search
distance_metrics <- c(1, 2)  # For example, Euclidean distance (1) and Manhattan distance (2)

# Define a range of kernel types to search
kernel_types <- c("rectangular", "triangular", "epanechnikov", "optimal")  # You can specify other kernels

# Create a tuning parameter grid with the required columns
tune_grid <- expand.grid(kmax = k_values, distance = distance_metrics, kernel = kernel_types)

ctrl <- trainControl(method = "cv", number = 10)

set.seed(75) #set seed for model training

model <- train(R1 ~ ., data = train_data, method = "kknn", trControl = ctrl, tuneGrid = tune_grid)

summary_ordered <- model$results

# Order the rows by Accuracy in descending order
summary_ordered <- summary_ordered[order(-summary_ordered$Accuracy), ]

# Print the ordered summary
print(summary_ordered)
subset_data <- summary_ordered[1:5, ]
subset_data2 <- as.data.frame(subset_data)

table_kable <- kable(subset_data2, format = "html", escape = FALSE) %>%
  kable_styling(full_width = FALSE)

print(table_kable)

predictions <- predict(model, newdata = test_data)

accuracy <- sum(predictions == test_data$R1) / nrow(test_data)