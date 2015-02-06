orfile <- "out/p1_0000_chr1.gap"

#eur.orfile <- "CEU_gap_chr1.gap" 
#eurfile <- "TSI_gap_chr1.gap"
#eurfile <- append(file, "GBR_gap_chr1.gap")
#eurfile <- append(file, "IBS_gap_chr1.gap")
#eurfile <- append(file, "FIN_gap_chr1.gap")

file <- "out/p1_0001_chr1.gap"
v <- 2:90
v <- formatC(v, width=4, format="d", flag="0")
file <- append(file, paste("out/p1_", v, "_chr1.gap", sep=""))

bindfile <- read.table(orfile, sep=",", header=F)
bindfile <- as.data.frame(bindfile)
head(bindfile)
file[1]
file[90]

for (i in 1:90) {
  infile <- read.table(paste(file[i],sep=""), sep=",", header=F)
  infile <- as.data.frame(infile)

  bindfile <- rbind(bindfile, infile)
}
t.bind <- bindfile$V1
ta.bind <- table(t.bind)
head(ta.bind)
ta.bind <- ta.bind[order(ta.bind, decreasing=T)]
write.table(ta.bind, "p2_sort.all.gap", quote=F, col.names=F, row.names=T, append=F, sep=",", )
