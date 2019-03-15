setwd("C:\\Users\\esther\\Documents\\GitHub\\instruments-master\\2018_2019\\Tests\\Test 4 solutions")

#data = read.table("IEP scores 20182019 test 4.txt", header = T, sep = "\t")
data = read.table("Test4.txt", header = T, sep = "\t")

data = data[,c(1,3:45)]
data = data[-c(1:2),]
                    
names(data) = c(	"name", "Test1", "Test2", "Test3", "Test4",
			"comments", "structure", "push_key", "messages",
			"window", "units", "text_pos", "texts", "draw", "flip_wait",
			"hi_name", "trial_loop",
			"keyboard", "respKeys", "clearEvents", "RT",
			"GUI_make", "GUI_show", "folder_name", "folder_check", "folder_make", "file_name", "file_check", "file_again", 
			"file_export", "info_participant", "info_trial", "info_response", "anonimity",
			"blocks_12", "design_3x2", "trials_16", "blockDesign", "congruence", "random", "blocks_8+4", "CorResp",
			"randomBlocks", "crossTable")

tiff("Test 4.tiff", width = 500, height = 500)
	hist(data$Test4, breaks = 30, main = "Test 4", xlab = "Score on 20", ylab = "number of students", col = "lightblue")
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







tiff("Test 3.1 General items.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(8:5)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "darkgray", main = "General items", xlab = "percentage")
dev.off()

tiff("Test 3.2 Basic participant interaction.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(19,31,39,38,18,17,13,12,11,10,9)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "darkgray", main = "Basic participant interaction", xlab = "percentage")
dev.off()

tiff("Test 3.3 Implement a minimal trial.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(34,33,43,42,41,40,32,14)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "darkgray", main = "Implement a minimal trial", xlab = "percentage")
dev.off()

tiff("Test 3.4 Verify presentation time.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(47:44)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "darkgray", main = "Verify presentation time", xlab = "percentage")
dev.off()

tiff("Test 3.5 Trial and block structure.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(36,35,21,20,16,15)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "darkgray", main = "Trial and block structure", xlab = "percentage")
dev.off()

tiff("Test 3.6 Verify response accuracy.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(49,48,37,22)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "darkgray", main = "Verify response accuracy", xlab = "percentage")
dev.off()

tiff("Test 3.7 Challenge.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(30:23)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "darkgray", main = "Challenge", xlab = "percentage")
dev.off()
