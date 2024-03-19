getwd()
setwd("C:/Users/omkar/OneDrive/Documents/Analytical Tools Folder")

myData=read.table("credit_card_data-headers.txt",header=TRUE)
head(myData)

data <- as.matrix(myData)

model <- ksvm(data[,1:10],data[,11],type="C-svc",kernel="vanilladot",C=100,scaled=TRUE) 

# calculate a1…am
a <- colSums(model@xmatrix[[1]] * model@coef[[1]])

cat(a)

# calculate a0
a0 <- model@b
a0
# see what the model predicts
pred <- predict(model,data[,1:10])
#pred
# see what fraction of the model’s predictions match the actual classification
frac <- sum(pred == data[,11]) / nrow(data)
