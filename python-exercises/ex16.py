from sys import argv
script,filename=argv
print(f"we're going to erase {filename}.")
print("if you don't want that,hit CTRL-C (^C).")
print("if you do wnat that,hit RETURN.")
print("if you do want that ,hit RETURN.")
input("?")
print("opening the file...")
target=open(filename,'w')
print("truncating the file,goodbye!")
target.truncate()
print("now i'am going to ask you for three llines.")
line1=input("line 1:")
line2=input("line 2:")
line3=input("line 3:")
print("i'am going towrite these to the jfile.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

target.write("\n")
print("and finally, we close it.")
target.close()

