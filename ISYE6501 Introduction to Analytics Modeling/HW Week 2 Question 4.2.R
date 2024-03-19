getwd()
setwd("C:/Users/omkar/OneDrive/Documents/Analytical Tools Folder")

myData <- read.table("iris.txt", header = TRUE, row.names = NULL)

data <- data.frame(myData)
data <- data[, -1]

str(data[, 1:4])

set.seed(200) #set seed for replication

data$Species <- as.factor(data$Species)

data[, 1:4] <- scale(data[, 1:4])

k <- 3
result <- kmeans(data[, c(1, 2, 3, 4)], centers = k, iter.max = 500)

# Get cluster centers
cluster_centers <- result$centers

# Create a vector of species names
species_names <- c("virginica", "versicolor", "setosa")

# Map cluster numbers to species names
cluster_assignments <- species_names[result$cluster]
cluster_assignments <- as.factor(cluster_assignments)

# Print the results
print(cluster_assignments)
print(data$Species)
print(cluster_centers)
accuracy <- sum(cluster_assignments == data$Species) / nrow(data)

