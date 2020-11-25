# removes the annoying Part Studio 1 from stl files exported from OnShape and adds how many need to be printed to the file name  
import os

# asks user for folder name that contains the files to rename
print('What is the name of the folder?')
folderName = input() # if file name has a space in it, then it must be entered with quotes "" around it

# goes through the files in the folder and renames them
path = '../../../desktop/' + folderName
if len(os.listdir(path)) == 0:
	print("Couldn't find folder")
for filename in os.listdir(path):
  originalFileName = path + '/' + filename
	# removes default text of "Part Studio 1 -" from file's name
	newFileName = originalFileName
	if newFileName.contains("Part Studio 1 - "):
  	newFileName = path + '/' + filename[int(len(filename)-11):int(len(filename))].strip()
  # if needed part quantity is greater than 1, then it adds (x2), (x3), etc.
  print('How many for ' + filename + '?')
  quantity = input()
  if quantity > 1:
  	newFileName = newFileName[:-4] + ' (x' + str(quantity) + ')' + newFileName[len(newFileName)-4:]
  # renames the file
  os.rename(originalFileName, newFileName)
