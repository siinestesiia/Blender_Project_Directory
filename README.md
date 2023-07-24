# Blender Project Directory Creator

This is my current personal way of organizing folders for a **Blender** project. I've always done it by hand, but now I'm using my **Python** skills to automate this (*kind of tedious*) task.
Feel free to use it and/or modify it at will.

## A brief explanation:

The `ProjectCreator` class creates a subdirectory (*in this case, in a desired path on my HDD*) named by the user, and a few other folders within it for fast and organized
Blender project creation. It also creates a PureRef empty file with
a default name so the user can later add some pictures for reference (*when you open this PureRef file, a window pop up, telling you that the file is corrupted, but if you press '**Ok**' or the '**x**', it will work just fine*).
Once the project is created, the **File Explorer** will open
at the location of the main folder named by the user.
A minor addition to the program is an error **beeping sound** whenever 
the user enters a '*wrong*' answer, and a high-pitched **beeping sound** 
after successfully creating the desired project.