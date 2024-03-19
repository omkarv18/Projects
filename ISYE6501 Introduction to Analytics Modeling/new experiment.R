getwd()
setwd("C:/Users/omkar/OneDrive/Documents/Analytical Tools Folder")

# Load required libraries
library(caret)

# Read the data
myData <- read.table("iris.txt", header = TRUE, row.names = NULL)

# Remove the row number column
data <- myData[, -1]

# Set seed for reproducibility
set.seed(200)

# Perform k-means clustering with k clusters
k <- 3
result <- kmeans(data[, 1:4], centers = k)

# Get cluster assignments
cluster_assignments <- result$cluster

# Extract the true species labels (response variable)
true_species <- myData$Species

# Create a confusion matrix to evaluate classification
confusion <- table(cluster_assignments, true_species)

# Calculate accuracy (sum of diagonal elements / total)
accuracy <- sum(diag(confusion)) / sum(confusion)

# Print the confusion matrix and accuracy
print(confusion)
print(paste("Accuracy:", accuracy))
