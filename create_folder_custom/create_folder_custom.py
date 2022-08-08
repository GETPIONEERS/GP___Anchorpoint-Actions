from pickle import FALSE
from typing_extensions import Self
from datetime import datetime
import os
import pathlib
import anchorpoint as ap

apc = ap.Context.instance() # setup anchorpoint context
ui = ap.UI() # setup UI


# DATE AND TIME (YYYY-MM-DD_HH-MM) based folder path calculation for folder creation
def calculate_dateandtime(dialog):
    folder_time = str(datetime.now().strftime("%Y-%m-%d_%H-%M"))

    parentDirectory = apc.path

    doProjectName = dialog.get_value("doProjectName")

    if doProjectName:
        projectName = pathlib.Path(apc.project_path)
        print(doProjectName)
        directoryToCreate = parentDirectory + "/" + projectName.name + "_" + folder_time
        create_folder(directoryToCreate, dialog)
    else:
        directoryToCreate = parentDirectory + "/" + folder_time
        create_folder(directoryToCreate, dialog)


# DATE (YYYY-MM-DD) based folder path calculation for folder creation
def calculate_date(dialog):
    folder_time = str(datetime.now().strftime("%Y-%m-%d"))
    
    parentDirectory = apc.path

    doProjectName = dialog.get_value("doProjectName")

    if doProjectName:
        projectName = pathlib.Path(apc.project_path)
        print(doProjectName)
        directoryToCreate = parentDirectory + "/" + projectName.name + "_" + folder_time
        create_folder(directoryToCreate, dialog)
    else:
        directoryToCreate = parentDirectory + "/" + folder_time
        create_folder(directoryToCreate, dialog)
    

# create folders
def create_folder(directoryToCreate, dialog):

    print(directoryToCreate)
    
    mode = 0o666
    exist_ok = True
    os.makedirs(directoryToCreate, mode, exist_ok)
    print("Directory " + directoryToCreate + " created")
    
    dialog.close()
    ui.show_info("Folder successfully created.", "", 2500)
    


dialog = ap.Dialog()

dialog.title ="Create custom folder"
dialog.add_text("<b>What kind of folder do you want to create?</b>")
dialog.add_button("Date", callback = calculate_date).add_info("YYYY-MM-DD")
dialog.add_button("Date and Time", callback = calculate_dateandtime).add_info("YYYY-MM-DD_HH-MM")
dialog.add_empty()
dialog.add_switch(False, var = "doProjectName").add_text("Include project name")
dialog.add_info("Enable to include the project name in the folder name.")

dialog.show()

projectName = pathlib.Path(apc.project_path)

