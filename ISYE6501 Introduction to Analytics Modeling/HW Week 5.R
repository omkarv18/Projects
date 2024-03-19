getwd()
setwd("C:/Users/omkar/OneDrive/Documents/Analytical Tools Folder")

myData <- read.table("uscrime.txt", header = TRUE)

head(myData)

#myData$So <- as.factor(myData$So)

#levels(myData$So)

model_linear <- lm(Crime ~ M + So + Ed + Po1 + Po2 + LF + M.F + Pop + NW + U1 + U2 + Wealth + Ineq + Prob + Time, data = myData)

data_point <- data.frame(M = c(14.0), So = c(0), Ed = c(10.0), Po1 = c(12.0), Po2 = c(15.5),
                         LF = c(0.640),
                         M.F = c(94.0),
                         Pop = c(150),
                         NW = c(1.1),
                         U1 = c(0.120),
                         U2 = c(3.6),
                         Wealth = c(3200),
                         Ineq = c(20.1),
                         Prob = c(0.04),
                         Time = c(39.0))
summary(model_linear)
prediction <- predict(model_linear, newdata = data_point)
print(prediction)

model_linear2 <- lm(Crime ~ Ed + Ineq, data = myData)

data_point2 <- data.frame(Ed = c(10.0), Ineq = c(20.1))

prediction2 <- predict(model_linear2, newdata = data_point2)

summary(model_linear2)


