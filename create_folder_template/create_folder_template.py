from typing_extensions import Self
import os
import anchorpoint


apc = anchorpoint.Context.instance() # setup anchorpoint context
ui = anchorpoint.UI() # setup UI


# ENTER DIRECTORIES HERE
# Note that the script will generate ALL folders up to the last folder automatically.
# This means that you do not need to create "foo", "foo/bar", "foo/bar/folders" if you want foo/bar/folders structure.
# foo/bar/folders is sufficient to create the entire chain.

directories = [

"Beratung/Konzept", 
"Kundendaten", 
"Produktion/Applikationen/360_2D_Events/3DVista",
"Produktion/Applikationen/360_2D_Events/krpano",
"Produktion/Applikationen/360_2D_Events/PTGui",

"Produktion/Applikationen/Output/WebGL",

"Produktion/Applikationen/Realtime/ThreeJS",
"Produktion/Applikationen/Realtime/UEngine",
"Produktion/Applikationen/Realtime/Unity",

"Produktion/Applikationen/Website_HTML/Bootstrap/HTML",

"Produktion/CGI/previews",
"Produktion/CGI/renderoutput",
"Produktion/CGI/renderpresets",
"Produktion/CGI/sceneassets",
"Produktion/CGI/scenes/xref/objects",

"Produktion/Grafik-Design/Edit",
"Produktion/Grafik-Design/Footage",
"Produktion/Grafik-Design/Output",

"Produktion/Postproduktion/Footage",
"Produktion/Postproduktion/Output/AS1-Final",
"Produktion/Postproduktion/Output/Final",
"Produktion/Postproduktion/Output/Prefinal",
"Produktion/Postproduktion/Output/Preview",
"Produktion/Postproduktion/Videoedit",

"Vorproduktion/Drehbuch",
"Vorproduktion/Inspiration"

]

# --------------------------------------------------------
# Function for creating the folder structure and .gitkeep
# --------------------------------------------------------

def button_clicked_doit(dialog):

    parentDirectory = apc.project_path
    
    for currentDirectory in directories:

        # append paths for folders and .gitkeep
        directoryToCreate = parentDirectory + "/" + currentDirectory
        doGitkeep = dialog.get_value("doGitkeep")
        directoryToCreateFile = parentDirectory + "/" + currentDirectory + "/.gitkeep"

        # create folders
        mode = 0o666
        exist_ok = True
        os.makedirs(directoryToCreate, mode, exist_ok)
        print("Directory " + directoryToCreate + " created")
        
        # check if .gitkeep files should be written
        if doGitkeep == True:   
            open(directoryToCreateFile, "w")
            print("Directory " + directoryToCreateFile + " created")

    # decide which info panel to display (.gitkeep yes / no)
    if doGitkeep == True:
        ui.show_info("Folders & .gitkeep files successfully created.", "", 2500)
    else:
        ui.show_info("Folders successfully created.", "", 2500)
    
    dialog.close()


# ---------------------------------
# Function for closing the dialoge
# ---------------------------------

def button_close(dialog: anchorpoint.Dialog):
    dialog.close()

# ----------
# Debugging
# ----------

def check_gitkeep(dialog):
    print(dialog.get_value("doGitkeep"))

# --------------
# Dialog Window 
# --------------

dialog = anchorpoint.Dialog()

dialog.title ="Create Folder Template"
dialog.add_text("<b>Do you really want to create the entire folder structure in this project?</b>")
dialog.add_text("Path: " + apc.project_path)
dialog.add_empty()
dialog.add_checkbox(True, var = "doGitkeep").add_text("Create .gitkeep files")
dialog.add_info("By default, Git ignores all folders without a file in it. This will create a .gitkeep file in every last folder <br>in a chain to make sure every user gets every folder. This should be enabled in most cases.")
dialog.add_button("Create Folders", callback = button_clicked_doit).add_button("Cancel", callback = button_close)

dialog.show()


