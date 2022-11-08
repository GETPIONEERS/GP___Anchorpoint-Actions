from typing_extensions import Self
import anchorpoint

apc = anchorpoint.Context.instance() # setup anchorpoint context
ui = anchorpoint.UI() # setup UI


def manage_switch(dialog: anchorpoint.dialog, state):
    print(dialog)


# --------------
# Dialog Window 
# --------------

dialog = anchorpoint.Dialog()

dialog.title ="Create Folder Template"
dialog.add_text("<b>This is a testing area for switches that enable and disable each other</b>")
dialog.add_switch(True, callback = manage_switch, var = "switch_1").add_text("I am setting #1")
dialog.add_switch(True, callback = manage_switch, var = "switch_2").add_text("I am setting #2")
dialog.show()