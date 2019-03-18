setwd("C:\\Users\\esther\\Documents\\GitHub\\instruments-master\\2018_2019\\Tests\\Test 4 solutions")

data = read.table("IEP scores 20182019 test 4.txt", header = T, sep = "\t")

data = data[,c(1,4:46)]
data = data[-c(1),]
                    
names(data) = c(	"name", "Test1", "Test2", "Test3", "Test4",
			"comments", "structure", "push_key", "messages",
			"window", "units", "text_pos", "texts", "draw", "flip_wait", "hi_name", "trial_loop",
			"keyboard", "respKeys", "clearEvents", "RT",
			"GUI_make", "GUI_show", "folder_name", "folder_check", "folder_make", "file_name", "file_check", "file_again", 
			"file_export", "info_participant", "info_trial", "info_response", "anonymity",
			"blocks_12", "design_3x2", "trials_16", "blockDesign", "congruence", "random", "blocks_8+4", "CorResp",
			"randomBlocks", "crossTable")

tiff("Test 4.tiff", width = 500, height = 500)
	hist(data$Test4, breaks = 30, main = "Test 4", xlab = "Score on 20", ylab = "number of students", col = "lightblue", xlim = c(0,20))
dev.off()

tiff("Test 1 verus Test 4.tiff", width = 500, height = 500)
	par(mar = c(4, 7, 3, 2))
	plot(x = data$Test1, y = data$Test4, xlim = c(0,20), ylim = c(0,20), xlab = "Test 1", ylab = "Test 4")
	abline(h = 10, v = 10)
dev.off()

tiff("Test 2 verus Test 4.tiff", width = 500, height = 500)
	par(mar = c(4, 7, 3, 2))
	plot(x = data$Test2, y = data$Test4, xlim = c(0,20), ylim = c(0,20), xlab = "Test 2", ylab = "Test 4")
	abline(h = 10, v = 10)
dev.off()

tiff("Test 3 verus Test 4.tiff", width = 500, height = 500)
	par(mar = c(4, 7, 3, 2))
	plot(x = data$Test3, y = data$Test4, xlim = c(0,20), ylim = c(0,20), xlab = "Test 3", ylab = "Test 4")
	abline(h = 10, v = 10)
dev.off()

tiff("Test 4.1 General items.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(6:9)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "darkgray", main = "General items", xlab = "percentage")
dev.off()

tiff("Test 4.2 Visual presentation.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(10:17)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "darkgray", main = "Visual presentation", xlab = "percentage")
dev.off()

tiff("Test 4.3 Hardware interaction.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(18:21)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "darkgray", main = "Hardware interaction", xlab = "percentage")
dev.off()

tiff("Test 4.4 Data file management.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(22:29)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "darkgray", main = "Data file management", xlab = "percentage")
dev.off()

tiff("Test 4.5 Data file content.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(30:34)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "darkgray", main = "Data file content", xlab = "percentage")
dev.off()

tiff("Test 4.6 Randomization.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(35:42)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "darkgray", main = "Randomization", xlab = "percentage")
dev.off()

tiff("Test 4.7 Challenge.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(43:44)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "darkgray", main = "Challenge", xlab = "percentage")
dev.off()
