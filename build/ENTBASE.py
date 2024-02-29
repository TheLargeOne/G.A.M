import os


def main(): 
    
    directory = "ENTBASE"

    parent_dir = ""


    path = os.path.join(parent_dir, directory) 

    os.mkdir(path)

    directory = "lua"

    parent_dir = "ENTBASE" 


    path = os.path.join(parent_dir, directory) 

    os.mkdir(path)




    directory = "entities"

    parent_dir = "ENTBASE/lua"


    path = os.path.join(parent_dir, directory) 

    os.mkdir(path)

    directory = "CHANGEME"

    parent_dir = "ENTBASE/lua/entities" 


    path = os.path.join(parent_dir, directory) 

    os.mkdir(path)

    directory = "autorun"

    parent_dir = "ENTBASE/lua" 


    path = os.path.join(parent_dir, directory) 

    os.mkdir(path)

    with open("ENTBASE/lua/entities/CHANGEME/shared.lua", "w") as f:
        f.write("")
    with open("ENTBASE/lua/entities/CHANGEME/cl_init.lua", "w") as f:
        f.write("")
    with open("ENTBASE/lua/entities/CHANGEME/init.lua", "w") as f:
        f.write("")
    with open("ENTBASE/lua/autorun/autorun.lua", "w") as f:
        f.write("")