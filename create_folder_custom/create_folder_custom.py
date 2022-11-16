from typing_extensions import Self
from datetime import datetime
import os
import pathlib
import anchorpoint
import apsync

apc = anchorpoint.Context.instance()  # setup anchorpoint context
ui = anchorpoint.UI()  # setup UI

projectPath = str(pathlib.Path(apc.project_path))
projectName = apsync.get_project(projectPath)
projectName = projectName.name


# DATE AND TIME (YYYY-MM-DD_HH-MM) based folder path calculation for folder creation
def calculate_dateandtime(dialog):
    folder_time = str(datetime.now().strftime("%Y-%m-%d_%H-%M"))

    parent_directory = apc.path

    # grab dialog switch variable "include project name"
    do_project_name = dialog.get_value("do_project_name")

    if do_project_name:
        projectName = pathlib.Path(apc.project_path)
        directory_to_create = (
            parent_directory + "/" + projectName.name + "_" + folder_time
        )
        create_folder(directory_to_create, dialog)
    else:
        directory_to_create = parent_directory + "/" + folder_time
        create_folder(directory_to_create, dialog)


# DATE (YYYY-MM-DD) based folder path calculation for folder creation
def calculate_date(dialog):
    folder_time = str(datetime.now().strftime("%Y-%m-%d"))

    parent_directory = apc.path

    # grab dialog switch variable "include project name"
    do_project_name = dialog.get_value("do_project_name")

    if do_project_name:
        projectName = pathlib.Path(apc.project_path)
        directory_to_create = (
            parent_directory + "/" + projectName.name + "_" + folder_time
        )
        create_folder(directory_to_create, dialog)
    else:
        directory_to_create = parent_directory + "/" + folder_time
        create_folder(directory_to_create, dialog)


# create folders
def create_folder(directory_to_create, dialog):

    print(directory_to_create)

    mode = 0o666
    exist_ok = True
    os.makedirs(directory_to_create, mode, exist_ok)
    print("Directory " + directory_to_create + " created")

    dialog.close()
    ui.show_info("Folder successfully created.", "", 2500)


# Build GUI
dialog = anchorpoint.Dialog()

dialog.title = "Create Custom Folder"
dialog.add_text("<b>What kind of folder do you want to create?</b>")
dialog.add_button("Date", callback=calculate_date).add_info("YYYY-MM-DD")
dialog.add_button("Date and Time", callback=calculate_dateandtime).add_info(
    "YYYY-MM-DD_HH-MM"
)
dialog.add_empty()
dialog.add_switch(False, var="do_project_name").add_text("Include project name")
dialog.add_info("Enable to include the project name in the folder name.")

dialog.show()
