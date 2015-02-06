library(amap)

infile <- read.table("test.chr1.csv", sep=',')
head(infile)
#infile$sum <- rowSums(infile[1:14])
#infile <- (infile[,1:14] / infile[,15]) * 100
#infile
#fc <- factor(head(infile,n=1))
matrix <- as.data.frame(t(infile[-1,]))
factor.t <- as.data.frame(t(infile[1,]))
fc <- factor(factor.t[[1]])
levels(fc)
#P <- c(1:14)[unclass(matrix[,14])]
#C <- unclass(matrix[,14])
#matrix <- na.omit(matrix)
#matrix <- big.matrix(t(infile[1:500000,]))
#matrix.d <- kmeans(matrix, 1)
matrix.d <- Dist(matrix, method="pearson")
#matrix.d <- na.omit(matrix)
#hc.d <- hclust(matrix.d)
mat.cmd<-cmdscale(matrix.d)
#mat.cmd<-matrix.d
#mat.cmd<-cmdscale(matrix.d)
#png(family="sans", width=20000, height=2000)
pdf(family="sans", paper="a4r", width=9.5, height=7)
#plot(hc.d)
plot(mat.cmd, col=unclass(fc))
#text(mat.cmd,labels=fc, col=unclass(fc))
dev.off()
