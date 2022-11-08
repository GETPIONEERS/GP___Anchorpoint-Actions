from typing_extensions import Self
from datetime import datetime
import os
import pathlib
import anchorpoint
import apsync 

apc = anchorpoint.Context.instance()  # setup anchorpoint context
ui = anchorpoint.UI()  # setup UI

ProjectPath = str(pathlib.Path(apc.project_path))

# --------------------
# List of directories
# --------------------

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


# ----------------------------------------------------------------------------
# List of icons. Write icon names ABOVE the path you want to set the icon for
# ----------------------------------------------------------------------------

icon = [
"eye"
# "Beratung/Konzept", 
# "Kundendaten", 
# "Produktion/Applikationen/360_2D_Events/3DVista",
# "Produktion/Applikationen/360_2D_Events/krpano",
# "Produktion/Applikationen/360_2D_Events/PTGui",

# "Produktion/Applikationen/Output/WebGL",

# "Produktion/Applikationen/Realtime/ThreeJS",
# "Produktion/Applikationen/Realtime/UEngine",
# "Produktion/Applikationen/Realtime/Unity",

# "Produktion/Applikationen/Website_HTML/Bootstrap/HTML",

# "Produktion/CGI/previews",
# "Produktion/CGI/renderoutput",
# "Produktion/CGI/renderpresets",
# "Produktion/CGI/sceneassets",
# "Produktion/CGI/scenes/xref/objects",

# "Produktion/Grafik-Design/Edit",
# "Produktion/Grafik-Design/Footage",
# "Produktion/Grafik-Design/Output",

# "Produktion/Postproduktion/Footage",
# "Produktion/Postproduktion/Output/AS1-Final",
# "Produktion/Postproduktion/Output/Final",
# "Produktion/Postproduktion/Output/Prefinal",
# "Produktion/Postproduktion/Output/Preview",
# "Produktion/Postproduktion/Videoedit",

# "Vorproduktion/Drehbuch",
# "Vorproduktion/Inspiration"
]

def set_icons():
    i = 0
    
    for relPath in directories:
        # check if the directory to be added has a corresponding icon in the array
        try:
            relPath = ProjectPath + "/" +  relPath
            relPath = str.replace(relPath, "\\", "/")
            # print("relative path is: " + relPath)
            # print("icon is: " + ":/icons/" + icon[i] + ".svg")
            apsync.set_folder_icon(relPath, apsync.Icon(":/icons/" + icon[i] + ".svg", "#ff0000"))
            print ("icon " + icon[i] + " for " + relPath)
        except:
            print ("no icon for " + relPath + "... skipping")
        i += 1

set_icons()