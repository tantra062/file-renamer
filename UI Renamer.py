# img_viewer.py

import PySimpleGUI as sg
import os.path

# First the window layout in 2 columns

file_list_column = [
    [
        sg.Text("Folder "), # just a text beside it.
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"), #key means ID on HTML
        sg.FolderBrowse(),
    ],
    [
        sg.Text("Title "),
        sg.InputText(
          enable_events=True, size=(40, 20), key="-FILE TITLE-"
        ),
        sg.Button("ok", key="-INITIATE-")

    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
            
        )
    ],
]

# For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Text("Choose an image from list on left:")], #
    [sg.Text(size=(40, 1), key="-TOUT-")], #displays the name of the selected file
    [sg.Image(key="-IMAGE-")], #display the image()
]

# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        # sg.Column(image_viewer_column),
    ]
]

window = sg.Window("Renamer", layout) 

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
  return [result]

folder_files = []
newFiles = []

while True:
    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"] # checks the folder element values to folder.
        
        try:
            # Get list of files in folder
            file_list = os.listdir(folder) # reads the folder variable.
        except:
            file_list = [] 
        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((
              ".png", ".gif",".webm", ".mpg", ".mp2", ".mpeg", 
              ".mpe", ".mpv", ".ogg", ".mp4", ".mp4", ".m4v", 
              ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", 
              ".avchd", ".txt"))
        ]
        folder_files =  fnames
        window["-FILE LIST-"].update(fnames)
    if event == "-INITIATE-":
      for file in folder_files:
        filename = os.path.join(
                  values["-FOLDER-"], file
              )
        file_name, file_extension = os.path.splitext(filename)
        epnumber = get_ep_number(filename)
        returned = set_file_name(file, values["-FOLDER-"]+"/", epnumber, values["-FILE TITLE-"], file_extension)
        newFiles.append(returned)
        window["-FILE LIST-"].update(newFiles)
window.close()