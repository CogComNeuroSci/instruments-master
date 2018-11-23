setwd("C:\\Users\\esther\\Documents\\GitHub\\instruments-master\\2018_2019\\Tests\\Test 2 solutions")

data = read.table("IEP scores 20182019 test 2.txt", header = T, sep = "\t")

data = data[,c(3,6,8,38:39,9:37)]

data = data[,c(1:8,10:13,17:18,14:15,19,26,28:30,9,32:34,16,20,27,31,21:25)]

names(data) = c(	"name", "Test1", "Test2", 
			"comments", "structure",
			"win", "background", "units", "circle", "radius", "color", "pos", "draw", "flip/wait", 
			".col", ".radius", "lessgreen", "for_loop", "for.indent", "col.loop", "radius.loop",        
			"text", "overlap", "collision.end", "message",
			".pos", "moonpos", "rotation.for", "pos.loop", 
			"ellipsoid", "circular", "AnglePlanet1", "AngleMoon6", "own_rotation") 

tiff("Test 2.tiff", width = 500, height = 500)
	hist(data$Test2, breaks = 30, main = "Test 2", xlab = "Score on 20", ylab = "number of students", col = "lightblue")
dev.off()

tiff("Test 2.1 Stationair zonnestelsel.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(14:4)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "dark green", main = "Stationary solar system", xlab = "percentage")
dev.off()

tiff("Test 2.2 Van gele zon tot rode reus.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(21:15)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "dark blue", main = "Expansion to a red giant", xlab = "percentage")
dev.off()

tiff("Test 2.3 Botsing.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(25:22)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "dark red", main = "Collision", xlab = "percentage")
dev.off()

tiff("Test 2.4 Hemellichamen laten roteren basisversie.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(29:26)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "gold", main = "Rotating the celestial objects (basic)", xlab = "percentage")
dev.off()

tiff("Test 2.5 Hemellichamen laten roteren advanced.tiff", width = 700, height = 500)
	par(mar = c(4, 7, 3, 2))
	barplot(colMeans(data[,c(34:30)], na.rm = T)*100, horiz = T, las = 2, xlim = c(0,100), col = "purple", main = "Rotating the celestial objects (advanced)", xlab = "percentage")
dev.off()











