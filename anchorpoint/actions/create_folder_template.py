import anchorpoint as ap
import apsync as aps
import os

apc = ap.Context.instance() # setup anchorpoint context
ui = ap.UI() # setup UI


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

# Function for creating the folder structure
def button_clicked_doit(dialog):

    parentDirectory = apc.project_path
    
    for currentDirectory in directories:

        directoryToCreate = parentDirectory + "/" + currentDirectory

        mode = 0o666
        exist_ok = True
        os.makedirs(directoryToCreate, mode, exist_ok)

        print("Directory " + directoryToCreate + " created")

    ui.show_info("Folders successfully created")
    dialog.close()


# Dialogue Window before creating the folder structure
dialog = ap.Dialog()

dialog.title ="WARNING"
dialog.add_text("Do you really want to create the entire folder structure in this folder:")
dialog.add_text(apc.project_path)
dialog.add_text(" ")
dialog.add_button("DO IT!", callback = button_clicked_doit)

dialog.show()

# TESTKOMMENTAR


