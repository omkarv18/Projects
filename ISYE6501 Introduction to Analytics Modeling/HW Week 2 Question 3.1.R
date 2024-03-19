getwd()
setwd("C:/Users/omkar/OneDrive/Documents/Analytical Tools Folder")

myData <- read.table("credit_card_data-headers.txt", header = TRUE)

data <- data.frame(myData)



train_indices <- sample(1:nrow(data), size = 0.8 * nrow(data))

train_data <- data[train_indices, ]
test_data <- data[-train_indices, ]

train_data$R1 <- as.factor(train_data$R1)
test_data$R1 <- as.factor(test_data$R1)

set.seed(238)

loocv_results <- train.kknn(formula = R1 ~ ., data = train_data, kmax = 60, distance = 2, kernel = "optimal", scale = TRUE)

#str(loocv_results)

print(loocv_results$MISCLASS)
print(loocv_results$best.parameters)

