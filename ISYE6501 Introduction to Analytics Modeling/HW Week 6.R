getwd()
setwd("C:/Users/omkar/OneDrive/Documents/Analytical Tools Folder")

myData3 <- read.table("uscrime.txt", header = TRUE)

myData <- myData3[, 1:15]

pca_result <- prcomp(myData, center = TRUE, scale. = TRUE)

summary(pca_result)

loadings_pc1 <- pca_result$rotation[, 1]
loadings_pc2 <- pca_result$rotation[, 2]
print(loadings_pc1)
print(loadings_pc2)

new_myData <- myData[, -which(names(myData) == "Po2")]

pca_result2 <- prcomp(new_myData, center = TRUE, scale. = TRUE)

summary(pca_result2)

loadings_pc1_2 <- pca_result2$rotation[, 1]
loadings_pc2_2 <- pca_result2$rotation[, 2]
print(loadings_pc1_2)
print(loadings_pc2_2)