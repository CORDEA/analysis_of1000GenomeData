library(bigmemory)
library(doSNOW)
library(amap)
library(cluster)

##infile <- read.table("sample_cluster.chr1.csv", sep=',')
infile <- read.table("sample_cluster.chr1.csv", sep=',')
#cl     <- makeCluster(4, type="SOCK")
#head(infile)
#infile$sum <- rowSums(infile[1:14])
#infile <- (infile[,1:14] / infile[,15]) * 100
infile <- infile[1:100001,]
#infile <- infile
#fc <- factor(head(infile,n=1))
#infile.t <- t(infile)
factor.t[1]

colnames(factor.t[1]) <- c("C")
#infile.t[grep("JPT", infile.t),]
#infile.t   <- infile.t[grep("(JPT|CHS)", infile.t$C),]
#subset(infile.t, 1=='JPT')
#registerDoSNOW(cl)
matrix <- as.data.frame(t(infile[-1,]))
origin <- as.data.frame(t(infile))
#head(matrix)
##factor.t <- as.data.frame(t(infile[1,]))
#head(factor.t)
matrix   <- matrix[grep("(JPT|CHS)", factor.t$C),]
factor.t <- origin[grep("(JPT|CHS)", factor.t$C),]

#matrix.d <- as.matrix(matrix)

#matrix <- infile.t[,-1]
#factor.t <- infile.t[,1]

#factor.t[grep("(JPT|CHB)", factor.t$C),]


fc <- factor(factor.t[[1]])
#fc
levels(fc)
#P <- c(1:14)[unclass(matrix[,14])]
#C <- unclass(matrix[,14])
#matrix <- na.omit(matrix)
#matrix <- big.matrix(t(infile[1:500000,]))
#matrix.d <- kmeans(matrix, 1)
##head(matrix)
matrix.d <- Dist(matrix, method="euclidean")
#matrix.d <- na.omit(matrix)
#hc.d <- hclust(matrix.d)
##cluster <- kmeans(matrix.d, 1)
###mat.cmd<-cmdscale(matrix.d)
#stopCluster(cl)
#mat.cmd<-matrix.d
mat.cmd<-cmdscale(matrix.d)
#fit <- kmeans(mat.cmd, 4)
#png(family="sans", width=20000, height=2000)
#pdf(family="sans", paper="a4r", width=9.5, height=7)
png(family="sans", paper="a4r", width=9.5, height=7)
#plot(hc.d)
#clusplot(matrix.d, cluster$cluster, color=T, shade=T, labels=2, lines=0)
plot(mat.cmd, pch=unclass(fc), col=unclass(fc)*2)
#text(mat.cmd,labels=fc, col=unclass(fc))
dev.off()
#x <- big.matrix()

#cl <- makeCluster(3, type="SOCK")
#ans <- bigkmeans(x, 2, nstart=5)

#head(ans)
