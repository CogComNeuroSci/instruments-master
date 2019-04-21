setwd("C:\\Users\\esther\\Documents\\GitHub\\instruments-master\\2018_2019\\Tests\\Test 5 solutions")

data = read.table("IEP scores 20182019 final test.txt", header = F, sep = "\t")

data = data[,c(1,3:56)]
data = data[-37,]

names(data) = c(	"Voornaam", "Gender", 
			"Test1", "Test2", "Test3", "Test4", "test1_4", "Final_test", "rounded_final_test", "Average", "rounded_final", 
			"code_runs", "comments", "structure", "variable_names", "space_key", "welcome", 
			"win", "timing", "arrow_pos", "text", "draw", "flip_wait", 
			"Personal_welcome", 
			"for_trial", "while_response", "pause_screen", "feedback", 
			"keyboard", "fj_key", "clearEvents", "stimulus_clock", "RT", 
			"GUI_show_folder", "check_make folder", "filename", "check_file", "box", "export", "P_info", "T_info", "R_info", "anonym", 
			"3_blocks", "factorial_design", "24_trials", "block_design", "random", "CorResp", "scalability", 
			"frames", "sequence", "unbalanced", "escape",
			"Prior")

# check the calculation of the average across test 1 to 4, overall score and roundings
par(mfrow = c(2,2))
plot(x = data$test1_4, 		y = rowSums(data[,3:6])/4);	abline(a = 0, b = 1)
plot(x = data$Final_test, 	y = data$rounded_final_test);	abline(a = 0, b = 1)
plot(x = data$Average, 		y = rowSums(data[,7:8])/2);	abline(a = 0, b = 1)
plot(x = data$Average, 		y = data$rounded_final);	abline(a = 0, b = 1)

### plots for final test
tiff("Fig 1.1 Test 5.tiff", width = 500, height = 500)
	hist(data$Final_test, breaks = 30, main = "Final test", xlab = "Score on 20", ylab = "number of students", col = "lightblue", xlim = c(0,20))
dev.off()

tiff("Fig 1.2 Test 1 versus Test 5.tiff", width = 500, height = 500)
	par(mar = c(4, 7, 3, 2))
	plot(x = data$Test1, y = data$Final_test, xlim = c(0,20), ylim = c(0,20), xlab = "Test 1", ylab = "Final test")
	abline(h = 10, v = 10)
dev.off()

tiff("Fig 1.3 Test 2 versus Test 5.tiff", width = 500, height = 500)
	par(mar = c(4, 7, 3, 2))
	plot(x = data$Test2, y = data$Final_test, xlim = c(0,20), ylim = c(0,20), xlab = "Test 2", ylab = "Final test")
	abline(h = 10, v = 10)
dev.off()

tiff("Fig 1.4 Test 3 versus Test 5.tiff", width = 500, height = 500)
	par(mar = c(4, 7, 3, 2))
	plot(x = data$Test3, y = data$Final_test, xlim = c(0,20), ylim = c(0,20), xlab = "Test 3", ylab = "Final test")
	abline(h = 10, v = 10)
dev.off()

tiff("Fig 1.5 Test 4 versus Test 5.tiff", width = 500, height = 500)
	par(mar = c(4, 7, 3, 2))
	plot(x = data$Test4, y = data$Final_test, xlim = c(0,20), ylim = c(0,20), xlab = "Test 4", ylab = "Final test")
	abline(h = 10, v = 10)
dev.off()

tiff("Fig 1.6 Test 1to4 versus Test 5.tiff", width = 500, height = 500)
	par(mar = c(4, 7, 3, 2))
	plot(x = data$test1_4, y = data$Final_test, xlim = c(0,20), ylim = c(0,20), xlab = "Test 1 to 4", ylab = "Final test")
	abline(h = 10, v = 10)
dev.off()


### plots for overall score
tiff("Fig 2.1 Final score.tiff", width = 500, height = 500)
	hist(data$Average, breaks = 30, main = "Final score", xlab = "Score on 20", ylab = "number of students", col = "lightblue", xlim = c(0,20))
dev.off()

tiff("Fig 2.2 Test 1 versus Final score.tiff", width = 500, height = 500)
	par(mar = c(4, 7, 3, 2))
	plot(x = data$Test1, y = data$Average, xlim = c(0,20), ylim = c(0,20), xlab = "Test 1", ylab = "Final score")
	abline(h = 10, v = 10)
dev.off()

tiff("Fig 2.3 Test 1 versus Final score.tiff", width = 500, height = 500)
	par(mar = c(4, 7, 3, 2))
	plot(x = data$Test2, y = data$Average, xlim = c(0,20), ylim = c(0,20), xlab = "Test 2", ylab = "Final score")
	abline(h = 10, v = 10)
dev.off()

tiff("Fig 2.4 Test 1 versus Final score.tiff", width = 500, height = 500)
	par(mar = c(4, 7, 3, 2))
	plot(x = data$Test3, y = data$Average, xlim = c(0,20), ylim = c(0,20), xlab = "Test 3", ylab = "Final score")
	abline(h = 10, v = 10)
dev.off()

tiff("Fig 2.5 Test 1 versus Final score.tiff", width = 500, height = 500)
	par(mar = c(4, 7, 3, 2))
	plot(x = data$Test4, y = data$Average, xlim = c(0,20), ylim = c(0,20), xlab = "Test 4", ylab = "Final score")
	abline(h = 10, v = 10)
dev.off()

tiff("Fig 2.6 Test 1 versus Final score.tiff", width = 500, height = 500)
	par(mar = c(4, 7, 3, 2))
	plot(x = data$Final_test, y = data$Average, xlim = c(0,20), ylim = c(0,20), xlab = "Test 4", ylab = "Final score")
	abline(h = 10, v = 10)
dev.off()

actualdata = data[-21,]
tiff("Fig 2.7 Final score Gender.tiff", width = 1000, height = 500)
	par(mfrow = c(1,2))
	hist(actualdata[actualdata$Gender==0,"Average"], breaks = 15, main = "Final score - males", xlab = "Score on 20", ylab = "number of students", col = "lightblue", xlim = c(0,20))
	hist(actualdata[actualdata$Gender==1,"Average"], breaks = 15, main = "Final score - females", xlab = "Score on 20", ylab = "number of students", col = "lightblue", xlim = c(0,20))
dev.off()
summary(actualdata[actualdata$Gender==0,"Average"])
summary(actualdata[actualdata$Gender==1,"Average"])

#   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
#  11.02   14.02   16.16   15.69   17.53   19.28 	males
#  12.50   14.68   16.79   16.55   18.33   19.93 	females

tiff("Fig 2.8 Final score Prior.tiff", width = 1000, height = 500)
	par(mfrow = c(1,2))
	hist(actualdata[actualdata$Prior==0,"Average"], breaks = 15, main = "Final score - no prior knowledge", xlab = "Score on 20", ylab = "number of students", col = "lightblue", xlim = c(0,20))
	hist(actualdata[actualdata$Prior==1,"Average"], breaks = 15, main = "Final score - prior knowledge", xlab = "Score on 20", ylab = "number of students", col = "lightblue", xlim = c(0,20))
dev.off()
summary(actualdata[actualdata$Prior==0,"Average"])
summary(actualdata[actualdata$Prior==1,"Average"])

#   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
#  12.50   14.32   16.79   16.43   18.31   19.93 	no prior experience
#  11.02   14.37   16.28   15.90   17.71   19.23 	prior experience

xtabs(~Prior + Gender, actualdata)

#      Gender
# Prior  0  1
#    0   8 23		# even though proportionally more males had prior experience, this didn't translate into the grades
#    1   8  8

data$code_runs = data$code_runs/2

### plots for overall score
tiff("Fig 3.1 General items.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(12:17)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "darkgray", xlab = "percentage", main = "General items")
dev.off()

tiff("Fig 3.2 Visual presentation.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(18:23)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "darkgray", xlab = "percentage", main = "Visual presentation")
dev.off()

tiff("Fig 3.3 Data types.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(24,24)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "darkgray", xlab = "percentage", main = "Data types")
dev.off()

tiff("Fig 3.4 Control structures.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(25:28)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "darkgray", xlab = "percentage", main = "Control structures")
dev.off()

tiff("Fig 3.5 Hardware interaction.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(29:33)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "darkgray", xlab = "percentage", main = "Hardware interaction")
dev.off()

tiff("Fig 3.6 Data file management.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(34:43)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "darkgray", xlab = "percentage", main = "Data file management")
dev.off()

tiff("Fig 3.7 Randomization.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(44:50)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "darkgray", xlab = "percentage", main = "Randomization")
dev.off()

tiff("Fig 3.8 Challenge.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(51:54)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "darkgray", xlab = "percentage", main = "Challenge")
dev.off()
