library(ggplot2)

infile <- read.table("lwk_overlap_forR.csv", sep=',', header=F)
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

box.plot = ggplot(values, aes(x = legend, y = value, fill = legend)) + geom_boxplot()

# ref. http://d.hatena.ne.jp/aaikmyz/20130115/1358224472
box.plot = box.plot + theme(axis.title.x = element_text(size=13),axis.title.y = element_text(size=13)) 
box.plot = box.plot + theme(axis.text.x = element_text(size=15),axis.text.y = element_text(size=15)) 
box.plot = box.plot + theme(legend.title = element_text(size=15),legend.text = element_text(size=15)) 
box.plot