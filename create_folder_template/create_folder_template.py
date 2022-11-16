from typing_extensions import Self
import os
import pathlib
import anchorpoint
import apsync

apc = anchorpoint.Context.instance()  # setup anchorpoint context
ui = anchorpoint.UI()  # setup UI

projectPath = str(pathlib.Path(apc.project_path))

# Default Anchorpoint colors
c_grey_light = "EEEEEE"
c_grey = "9E9E9E"
c_grey_dark = "1F2125"

c_purple_bright = "#DCC9F6"
c_purple = "#7937d4"
c_purple_dark = "#491393"

c_red_bright = "#F27979"
c_red = "#D33434"
c_red_dark = "#6A1414"

c_turk_bright = "#BAFBF0"
c_turk = "#37D4BB"
c_turk_dark = "#07705F"

c_yellow_bright = "#F3D582"
c_yellow = "#D4AA37"
c_yellow_dark = "#72570E"

c_orange_light = "#FBBC9F"
c_orange = "#FE7C3F"
c_orange_dark = "#9F3C0D"

c_green_light = "#D7F5B0"
c_green = "#9DDB4A"
c_green_dark = "#447602"

c_blue_light = "#90CAF9"
c_blue = "#1E88E5"
c_blue_dark = "#0D47A1"

# Misc Variables
doGitkeep = None
doSetIcon = None

# fmt: off
# FOLDER DIRECTORIES
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
    "Vorproduktion/Inspiration",
]

# DIRECTORIES ICONS AND COLORS
iconDirectories = [
    # Folders with Icons
    {   
        "path": "Kundendaten", 
        "icon": "emoticons/skull", 
        "color": c_red_bright
    },
    {   
        "path": "Beratung", 
        "icon": "music-audio/gramophone", 
        "color": c_blue_light
    },
    {   
        "path": "Beratung/Konzept", 
        "icon": "design/guides", 
        "color": c_blue_light
    },
    {   
        "path": "Produktion", 
        "icon": "design/paint-brush", 
        "color": c_green_light
    },
    {
        "path": "Produktion/Applikationen",
        "icon": "design/layers",
        "color": c_green_light,
    },
    {   "path": "Produktion/CGI", 
        "icon": "design/3d", 
        "color": c_green_light
    },
    {
        "path": "Produktion/Grafik-Design",
        "icon": "design/brush",
        "color": c_green_light,
    },
    {
        "path": "Produktion/Postproduktion",
        "icon": "design/paper-cutter",
        "color": c_green_light,
    },
    {
        "path": "Vorproduktion", 
        "icon": "design/palette", 
        "color": c_orange_light
    },
    {
        "path": "Vorproduktion/Drehbuch",
        "icon": "multimedia/album",
        "color": c_orange_light,
    },
    {
        "path": "Vorproduktion/Inspiration",
        "icon": "feedback/feedback-9",
        "color": c_orange_light,
    },
    
    # Folders with just colors
    {
        "path": "Produktion/Applikationen/360_2D_Events",
        "icon": "",
        "color": c_green_light,
    },
    {
        "path": "Produktion/Applikationen/360_2D_Events/3DVista",
        "icon": "",
        "color": c_green_light,
    },
    {
        "path": "Produktion/Applikationen/360_2D_Events/krpano",
        "icon": "",
        "color": c_green_light,
    },
    {
        "path": "Produktion/Applikationen/360_2D_Events/PTGui",
        "icon": "",
        "color": c_green_light,
    },
    {
        "path": "Produktion/Applikationen/Output/", 
        "icon": "", 
        "color": c_green_light},
    {
        "path": "Produktion/Applikationen/Output/WebGL",
        "icon": "",
        "color": c_green_light,
    },
    {
        "path": "Produktion/Applikationen/Realtime/", 
        "icon": "", 
        "color": c_green_light
    },
    {
        "path": "Produktion/Applikationen/Realtime/ThreeJS",
        "icon": "",
        "color": c_green_light,
    },
    {
        "path": "Produktion/Applikationen/Realtime/UEngine",
        "icon": "",
        "color": c_green_light,
    },
    {
        "path": "Produktion/Applikationen/Realtime/Unity",
        "icon": "",
        "color": c_green_light,
    },
    {
        "path": "Produktion/Applikationen/Website_HTML",
        "icon": "",
        "color": c_green_light,
    },
    {
        "path": "Produktion/Applikationen/Website_HTML/Bootstrap",
        "icon": "",
        "color": c_green_light,
    },
    {
        "path": "Produktion/Applikationen/Website_HTML/Bootstrap/HTML",
        "icon": "",
        "color": c_green_light,
    },
    {
        "path": "Produktion/CGI/previews", 
        "icon": "", 
        "color": c_green_light
    },
    {
        "path": "Produktion/CGI/renderoutput", 
        "icon": "", 
        "color": c_green_light
    },
    {
        "path": "Produktion/CGI/renderpresets", 
        "icon": "", 
        "color": c_green_light
    },
    {
        "path": "Produktion/CGI/sceneassets", 
        "icon": "", 
        "color": c_green_light
    },
    {
        "path": "Produktion/CGI/scenes", 
        "icon": "", 
        "color": c_green_light
    },
    {
        "path": "Produktion/CGI/scenes/xref", 
        "icon": "", 
        "color": c_green_light
    },
    {
        "path": "Produktion/CGI/scenes/xref/objects", 
        "icon": "", 
        "color": c_green_light
    },
    {
        "path": "Produktion/Grafik-Design/Edit", 
        "icon": "", 
        "color": c_green_light
    },
    {
        "path": "Produktion/Grafik-Design/Footage", 
        "icon": "", 
        "color": c_green_light
    },
    {
        "path": "Produktion/Grafik-Design/Output", 
        "icon": "", 
        "color": c_green_light
    },
    {
        "path": "Produktion/Postproduktion/Footage", 
        "icon": "", 
        "color": c_green_light
    },
    {
        "path": "Produktion/Postproduktion/Output", 
        "icon": "", 
        "color": c_green_light
    },
    {
        "path": "Produktion/Postproduktion/Output/AS1-Final",
        "icon": "",
        "color": c_green_light,
    },
    {
        "path": "Produktion/Postproduktion/Output/Final",
        "icon": "",
        "color": c_green_light,
    },
    {
        "path": "Produktion/Postproduktion/Output/Prefinal",
        "icon": "",
        "color": c_green_light,
    },
    {
        "path": "Produktion/Postproduktion/Output/Preview",
        "icon": "",
        "color": c_green_light,
    },
    {
        "path": "Produktion/Postproduktion/Videoedit", 
        "icon": "", 
        "color": c_green_light
    },
]
# fmt: one

# --------------------------------------------------------
# Function for creating the folder structure and .gitkeep
# --------------------------------------------------------
def button_create_folders(dialog):

    parentDirectory = apc.project_path

    for currentDirectory in directories:

        doGitkeep = dialog.get_value("doGitkeep")
        doSetIcons = dialog.get_value("doSetIcons")

        # append paths for folders and .gitkeep
        directoryToCreate = parentDirectory + "/" + currentDirectory
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
        if doSetIcons == True:
            set_icons()
        ui.show_info("Folders & .gitkeep files successfully created.", "", 2500)
    else:
        if doSetIcons == True:
            set_icons()
        ui.show_info("Folders successfully created.", "", 2500)

    dialog.close()


# -----------------------------------------------
# Function for setting icons on existing folders
# -----------------------------------------------
def set_icons():
    for directory in iconDirectories:
        relPath = str.replace(projectPath + "/" + directory["path"], "\\", "/")
        icon = directory["icon"]
        color = directory["color"]
        print("Directory Icon", relPath, ":/icons/" + icon + ".svg", color, "set")
        apsync.set_folder_icon(relPath, apsync.Icon(":/icons/" + icon + ".svg", color))


# ---------------------------------
# Function for closing the dialoge
# ---------------------------------
def button_close(dialog: anchorpoint.Dialog):
    dialog.close()


# --------------
# Dialog Window
# --------------
dialog = anchorpoint.Dialog()

dialog.title = "Create Project Folder Template"
dialog.add_text(
    "<b>Do you really want to create the entire folder structure in this project?</b>"
)
dialog.add_text("Path: " + apc.project_path)
dialog.add_empty()
dialog.add_checkbox(True, var="doGitkeep").add_text("Create .gitkeep files")
dialog.add_info(
    "By default, Git ignores all folders without a file in it. This will create a .gitkeep file in every last folder <br>in a chain to make sure every user gets every folder. This should be enabled in most cases."
)
dialog.add_checkbox(True, var="doSetIcons").add_text("Set icons and colors")
dialog.add_info(
    "Sets default icons and colors after creating the folders. This should be enabled in most cases."
)
dialog.add_empty()
dialog.add_info(
    "Warning: Anchorpoint will freeze for a couple of seconds. This is normal."
)
dialog.add_button("Create Folders", callback=button_create_folders)

dialog.show()
