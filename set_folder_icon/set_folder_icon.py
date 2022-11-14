import pathlib
import anchorpoint
import apsync

# -------------------------------------------------------------------------------------------------
#   READ ME 
# -------------------------------------------------------------------------------------------------
#   
# -------------------------------------------------------------------------------------------------

# ANCHORPOINT STUFF
apc = anchorpoint.Context.instance()  # setup anchorpoint context
ui = anchorpoint.UI()  # setup UI

ProjectPath = str(pathlib.Path(apc.project_path))

## ANCHORPOINT COLORS
# special default color; seems to be broken though
c_default = "#000000"

# default anchorpoint colors
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

## DIRECTORIES ICONS AND COLORS
dirsToCreate = [
    # Folders with Icons
    {
        "path" : "Kundendaten",
        "icon" : "emoticons/skull",
        "color" : c_red_bright
    },
    {
        "path" : "Beratung",
        "icon" : "music-audio/gramophone",
        "color" : c_blue_light
    },
    {
        "path" : "Beratung/Konzept",
        "icon" : "design/guides",
        "color" : c_blue_light
    },

    {
        "path" : "Produktion",
        "icon" : "design/paint-brush",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/Applikationen",
        "icon" : "design/layers",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/CGI",
        "icon" : "design/3d",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/Grafik-Design",
        "icon" : "design/brush",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/Postproduktion",
        "icon" : "design/paper-cutter",
        "color" : c_green_light
    },
    
    {
        "path" : "Vorproduktion",
        "icon" : "design/palette",
        "color" : c_orange_light
    },
    {
        "path" : "Vorproduktion/Drehbuch",
        "icon" : "multimedia/album",
        "color" : c_orange_light
    },
    {
        "path" : "Vorproduktion/Inspiration",
        "icon" : "feedback/feedback-9",
        "color" : c_orange_light
    },

    # Folders with just colors
    {
        "path" : "Produktion/Applikationen/360_2D_Events",
        "icon" : "",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/Applikationen/360_2D_Events/3DVista",
        "icon" : "",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/Applikationen/360_2D_Events/krpano",
        "icon" : "",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/Applikationen/360_2D_Events/PTGui",
        "icon" : "",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/Applikationen/Output/",
        "icon" : "",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/Applikationen/Output/WebGL",
        "icon" : "",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/Applikationen/Realtime/",
        "icon" : "",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/Applikationen/Realtime/ThreeJS",
        "icon" : "",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/Applikationen/Realtime/UEngine",
        "icon" : "",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/Applikationen/Realtime/Unity",
        "icon" : "",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/Applikationen/Website_HTML",
        "icon" : "",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/Applikationen/Website_HTML/Bootstrap",
        "icon" : "",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/Applikationen/Website_HTML/Bootstrap/HTML",
        "icon" : "",
        "color" : c_green_light
    },
    
    {
        "path" : "Produktion/CGI/previews",
        "icon" : "",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/CGI/renderoutput",
        "icon" : "",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/CGI/renderpresets",
        "icon" : "",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/CGI/sceneassets",
        "icon" : "",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/CGI/scenes",
        "icon" : "",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/CGI/scenes/xref",
        "icon" : "",
        "color" : c_green_light
    },
        {
        "path" : "Produktion/CGI/scenes/xref/objects",
        "icon" : "",
        "color" : c_green_light
    },
    
    {
        "path" : "Produktion/Grafik-Design/Edit",
        "icon" : "",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/Grafik-Design/Footage",
        "icon" : "",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/Grafik-Design/Output",
        "icon" : "",
        "color" : c_green_light
    },
    
    {
        "path" : "Produktion/Postproduktion/Footage",
        "icon" : "",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/Postproduktion/Output",
        "icon" : "",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/Postproduktion/Output/AS1-Final",
        "icon" : "",
        "color" : c_green_light
    },
     {
        "path" : "Produktion/Postproduktion/Output/Final",
        "icon" : "",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/Postproduktion/Output/Prefinal",
        "icon" : "",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/Postproduktion/Output/Preview",
        "icon" : "",
        "color" : c_green_light
    },
    {
        "path" : "Produktion/Postproduktion/Videoedit",
        "icon" : "",
        "color" : c_green_light
    },
]

def set_icons():
    for directory in dirsToCreate:
        relPath = str.replace(ProjectPath + "/" + directory["path"], "\\", "/")
        icon = directory["icon"]
        color = directory["color"]
        print(relPath, ":/icons/" + icon + ".svg", color)
        apsync.set_folder_icon(relPath, apsync.Icon(":/icons/" + icon + ".svg", color))

set_icons()












