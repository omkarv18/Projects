getwd()
setwd("C:/Users/omkar/OneDrive/Documents/Analytical Tools Folder")

library(kernlab)

myData <- read.table("credit_card_data-headers.txt", header = TRUE)
data <- as.matrix(myData)

model <- ksvm(data[, 1:10], data[, 11], type = "C-svc", kernel = "vanilladot", C = 100, scaled = TRUE)

# Get the coefficients (a values) for each support vector
support_vector_coefficients <- model@coef[[1]] * model@xmatrix[[1]]

# Summarize the coefficients for each feature
a_values <- colSums(support_vector_coefficients)

# Get the intercept (a0)
a0 <- model@b

print("Coefficients a for each feature:")
print(a_values)

print("Intercept a0:")
print(a0)

# See what the model predicts
pred <- predict(model, data[, 1:10])

# See what fraction of the model’s predictions match the actual classification
frac <- sum(pred == data[, 11]) / nrow(data)
print("Accuracy:")
print(frac)
