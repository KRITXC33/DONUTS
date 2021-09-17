
file = open("/Desktop/EX.txt")
file.read()
//Add file.readline() 
//To let pyshell read line by line

file.write("More examples") //Use this to write more text 
file.close

//When done, the code should look like this:

file = open("/Desktop/EX.txt")
file.readline()

file.write("More examples")
file.close()