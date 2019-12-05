setwd("C:\\Users\\esther\\Documents\\GitHub\\instruments-master\\2019_2020\\Tests\\Test 2 solutions")

data = read.table("IEP scores 20192020 test 2.txt", header = T, sep = "\t")

data = data[,c(4:43)]

names(data) = c(	"Pompoen", "Test1", "Test2", "ingediend", 
			"comments", "structure", 
			"win", "background", "units", "text", "draw", "flip/wait", "close", 
			"circle", "radius", "colored", "gauss", "Red-Blue", "range", 
			"position", "buffer", 
			"10_circles", "10_unique", "10_for", "for_indent", "FB_if", "equal_5%", "FB_color", 
			"8_trials", "for_indent", "break", 
			"2_biases", "arrow", "bias", "speed", "for_movement", "for_indent", "hpos", "reentry", "front_arrow")

data = data[data$ingediend == 1, ]

tiff("Test 2.tiff", width = 500, height = 500)
	hist(data$Test2, breaks = 30, main = "Test 2", xlab = "Score on 20", ylab = "number of students", col = "lightblue", xlim = c(0,20))
dev.off()

tiff("Test 2.1 Leeg experiment.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(13:4)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), main = "Leeg experiment", xlab = "percentage")
dev.off()

tiff("Test 2.2 Eén gekleurde bol.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(19:14)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), main = "Eén gekleurde bol", xlab = "percentage")
dev.off()

tiff("Test 2.3 Random locatie.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(21:20)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), main = "Random locatie", xlab = "percentage")
dev.off()

tiff("Test 2.4 10 bollen.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(28:22)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), main = "10 bollen", xlab = "percentage")
dev.off()

tiff("Test 2.5 8 trials.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(31:29)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100),  main = "8 trials", xlab = "percentage")
dev.off()

tiff("Test 2.6 Advanced.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(40:32)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), main = "Advanced", xlab = "percentage")
dev.off()

tiff("Test 1 verus Test 2.tiff", width = 500, height = 500)
	par(mar = c(4, 7, 3, 2))
	plot(x = data$Test1, y = data$Test2, xlim = c(0,20), ylim = c(0,20), xlab = "Test 1", ylab = "Test 2")
	abline(h = 10, v = 10)
dev.off()










