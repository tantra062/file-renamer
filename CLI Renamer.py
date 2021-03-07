import os
import fnmatch

def get_directory():
  result = input("Directory: ")
  if isValidDirectory(result): 
    result.replace("\\","/")
    if result[len(result)-1] != "/":
      result+= "/"
    return result
  else: return get_directory()

def isValidDirectory(path):
  if not os.path.exists(os.path.dirname(path)): return False
  else: return True

def get_user_input():
  directory = get_directory()
  if directory[len(directory)-1] != "/":
    directory+= "/"
  title = input("Title: ")
  return directory, title

def get_file_extension(filename):
  result = ""
  for i in range(len(filename), 0, -1):
    result = filename[i-1]+ result
    if filename[i-1] == ".": break
  return result

def isFormatValid(file_format):
  if (".WEBM" == file_format or ".MPG" == file_format or ".MP2" == file_format or ".MPEG" == file_format or 
      ".MPE" == file_format or ".MPV" == file_format or ".OGG" == file_format or ".MP4" == file_format or 
      ".MP4" == file_format or ".M4V" == file_format or ".AVI" == file_format or ".WMV" == file_format or 
      ".MOV" == file_format or ".QT" == file_format or ".FLV" == file_format or ".SWF" == file_format or 
      ".AVCHD" == file_format or ".txt" == file_format):
    return True
  else: return False

def get_ep_number(filename):
  result = ''.join(filter(lambda x : x.isdigit(), filename))
  count = len(result)
  while count <= 3:
    result = "0" + result
    count+=1
  return result 
  
def set_file_name(filename, directory, episode_number, title, file_extension , episode_name = ""):
  result = episode_number + " - "+ title + file_extension 
  os.rename(directory+filename, directory+result)
  os.path.dirname(os.path.realpath(__file__))

def main():
  user_input = get_user_input()
  files = []
  print(user_input)
  for filename in os.listdir(user_input[0]):
    file_extension = get_file_extension(filename)
    a = isFormatValid(file_extension)
    if a == True:
      files.append(filename)

  for file in files:
    file_extension = get_file_extension(file)
    ep_number = get_ep_number(file)
    set_file_name(file, user_input[0], ep_number,user_input[1],file_extension)










  # for filename in os.listdir(user_input[0]):
  #   file_extension = get_file_extension(filename)
  #   ep_number = get_ep_number(filename)
  #   set_file_name(filename, user_input[0], ep_number,user_input[1],file_extension)
    
if __name__ == "__main__":
  main()
  