library(ggplot2)

infile <- read.table("yri_overlap_forR.csv", sep=',', header=F)
max(infile$V2)

summary(infile$V3)

pu  <- data.frame(infile$V2)
cps <- data.frame(infile$V3)

colnames(pu)  <- 'value'
colnames(cps) <- 'value'

pu$legend  <- 'population peculiar SNPs'
cps$legend <- 'cpsSNPs'

values <- rbind(cps, pu)

ggplot(values, aes(value, fill = legend)) + xlim(c(min(cps$value), max(pu$value))) + geom_density(alpha = 0.5)

ggplot(values, aes(x = legend, y = value, fill = legend)) + geom_boxplot()