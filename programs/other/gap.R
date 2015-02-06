file <- "0000_chr1.gap"
v <- 1:90
v <- formatC(v, width=4, format="d", flag="0")
file <- append(file, paste(v, "_chr1.gap", sep=""))
#for (i in 1:90) {
#    file <- append(file, paste("00", i, "_chr1.gap", sep=""))
#}
file[1]
file[91]
for (i in 1:91) {
  infile <- read.table(paste("all/", file[i], sep=""), sep=",", header=T)

  head(infile)
  sort <- infile[order(-infile$gap),]
  h.sort <- head(sort, n=1000)
  write.table(h.sort, file=paste("out/p1_", file[i], sep=""), sep=",", col.names=F, row.names=F, quote=F, append=F)
}
