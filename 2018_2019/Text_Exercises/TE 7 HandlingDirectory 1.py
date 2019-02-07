import os
my_home_directory = os.getcwd()
print(my_home_directory)

my_home_directory = "C:/Users/esther/Downloads"

os.chdir(my_home_directory)

Subject_code = "G1S2"
Session = 3
my_directory = my_home_directory + "/" + Subject_code + "/" + str(Session)
 
# This of course only works when my_directory exists in your directory system
os.chdir(my_directory)
