import pathlib
import anchorpoint
import apsync

# -------------------------------------------------------------------------------------------------
#   READ ME 
# -------------------------------------------------------------------------------------------------
#   By default, the script creates all necessary folders for a full path to be created. 
#   That means, if you add "/Testfolder/Content/Innercontent" to dirsToCreate the script
#   will create the FULL directory tree. That also means that ONLY THE LAST FOLDER IN 
#   THE TREE WILL GET AN ICON. This what the "############## EXPLICIT ICONS AND COLORING" 
#   part at the bottom is for. For this example, you could use this to color /Testfolder/Content/
#
#   The script also does not care if the folder already has an icon or a color. It will simply
#   override it with whatever is defined in dirsToCreate.
# -------------------------------------------------------------------------------------------------

# ANCHORPOINT STUFF
apc = anchorpoint.Context.instance()  # setup anchorpoint context
ui = anchorpoint.UI()  # setup UI

ProjectPath = str(pathlib.Path(apc.project_path))

## ANCHORPOINT COLORS
c_grey = "#9E9E9E" # default color
c_purple = "#7937d4"
c_red = "#d33434"
c_turk = "#37d4bb"
c_yellow = "#d4aa37"
c_orange = "#fe7c3f"
c_green = "#fe7c3f"
c_blue = "#1e88e5"

## DIRECTORIES ICONS AND COLORS
dirsToCreate = [
    ############## Beratung
    {
        "path" : "Beratung/Konzept", 
        "icon" : "folderGrey",
        "color" : c_grey
    },
    ############## Kundendaten
    {
        "path" : "Kundendaten", 
        "icon" : "folderGrey",
        "color" : c_grey
    },
    ############## Produktion / Applikationen / 360_2D_Events
    {
        "path" : "Produktion/Applikationen/360_2D_Events/3DVista", 
        "icon" : "folderGrey",
        "color" : c_grey
    },
    {
        "path" : "Produktion/Applikationen/360_2D_Events/krpano", 
        "icon" : "folderGrey",
        "color" : c_grey
    },
    {
        "path" : "Produktion/Applikationen/360_2D_Events/PTGui", 
        "icon" : "folderGrey",
        "color" : c_grey
    },
    ############## Produktion / Applikationen / Output
    {
        "path" : "Produktion/Applikationen/Output/WebGL",
        "icon" : "folderGrey",
        "color" : c_grey
    },
    ############## Produktion / Applikationen / Realtime
    {
        "path" : "Produktion/Applikationen/Realtime/ThreeJS",
        "icon" : "folderGrey",
        "color" : c_grey
    },
    {
        "path" : "Produktion/Applikationen/Realtime/UEngine",
        "icon" : "folderGrey",
        "color" : c_grey
    },
    {
        "path" : "Produktion/Applikationen/Realtime/Unity",
        "icon" : "folderGrey",
        "color" : c_grey
    },
    ############## Produktion / Applikationen / Website_HTML / Bootstrap
    {
        "path" : "Produktion/Applikationen/Website_HTML/Bootstrap/HTML",
        "icon" : "folderGrey",
        "color" : c_grey
    },
    ############## Produktion / CGI
    {
        "path" : "Produktion/CGI/previews",
        "icon" : "folderGrey",
        "color" : c_grey
    },
    {
        "path" : "Produktion/CGI/renderoutput",
        "icon" : "folderGrey",
        "color" : c_grey
    },
    {
        "path" : "Produktion/CGI/renderpresets",
        "icon" : "folderGrey",
        "color" : c_grey
    },
    {
        "path" : "Produktion/CGI/sceneassets",
        "icon" : "folderGrey",
        "color" : c_grey
    },
    {
        "path" : "Produktion/CGI/scenes/xref/objects",
        "icon" : "folderGrey",
        "color" : c_grey
    },
    ############## Produktion / Grafik-Design
    {
        "path" : "Produktion/Grafik-Design/Edit",
        "icon" : "folderGrey",
        "color" : c_grey
    },
    {
        "path" : "Produktion/Grafik-Design/Footage",
        "icon" : "folderGrey",
        "color" : c_grey
    },
    {
        "path" : "Produktion/Grafik-Design/Output",
        "icon" : "folderGrey",
        "color" : c_grey
    },
    ############## Produktion / Postproduktion
    {
        "path" : "Produktion/Postproduktion/Footage",
        "icon" : "folderGrey",
        "color" : c_grey
    },
    {
        "path" : "Produktion/Postproduktion/Output/AS1-Final",
        "icon" : "folderGrey",
        "color" : c_grey
    },
    {
        "path" : "Produktion/Postproduktion/Output/Final",
        "icon" : "folderGrey",
        "color" : c_grey
    },
    {
        "path" : "Produktion/Postproduktion/Output/Prefinal",
        "icon" : "folderGrey",
        "color" : c_grey
    },
    {
        "path" : "Produktion/Postproduktion/Output/Preview",
        "icon" : "folderGrey",
        "color" : c_grey
    },
    {
        "path" : "Produktion/Postproduktion/Videoedit",
        "icon" : "folderGrey",
        "color" : c_grey
    },
    ############## Vorproduktion
    {
        "path" : "Vorproduktion/Drehbuch",
        "icon" : "folderGrey",
        "color" : c_grey
    },
    {
        "path" : "Vorproduktion/Inspiration",
        "icon" : "folderGrey",
        "color" : c_grey
    },
    ############## EXPLICIT ICONS AND COLORING
    {
        "path" : "Kundendaten",
        "icon" : "eye",
        "color" : c_red
    },
    {
        "path" : "Beratung",
        "icon" : "eye",
        "color" : c_red
    },
    {
        "path" : "Produktion",
        "icon" : "eye",
        "color" : c_red
    },
    {
        "path" : "Vorproduktion",
        "icon" : "eye",
        "color" : c_red
    }
]

def set_icons():
    for directory in dirsToCreate:
        relPath = str.replace(ProjectPath + "/" + directory["path"], "\\", "/")
        icon = directory["icon"]
        color = directory["color"]
        print(relPath, ":/icons/" + icon + ".svg", color)
        apsync.set_folder_icon(relPath, apsync.Icon(":/icons/" + icon + ".svg", color))

set_icons()












