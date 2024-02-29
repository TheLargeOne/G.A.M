import os


def main():

    directory = "SWEPBASE"

    parent_dir = ""


    path = os.path.join(parent_dir, directory) 

    os.mkdir(path)

    directory = "lua"

    parent_dir = "SWEPBASE" 


    path = os.path.join(parent_dir, directory) 

    os.mkdir(path)


    directory = "materials"

    parent_dir = "SWEPBASE" 


    path = os.path.join(parent_dir, directory) 

    os.mkdir(path)


    directory = "entities"

    parent_dir = "SWEPBASE/materials" 


    path = os.path.join(parent_dir, directory) 

    os.mkdir(path)




    directory = "autorun"

    parent_dir = "SWEPBASE/lua"


    path = os.path.join(parent_dir, directory) 

    os.mkdir(path)


    directory = "weapons"

    parent_dir = "SWEPBASE/lua"


    path = os.path.join(parent_dir, directory) 

    os.mkdir(path)

    directory = "CHANGEME"

    parent_dir = "SWEPBASE/lua/weapons"


    path = os.path.join(parent_dir, directory) 

    os.mkdir(path)


    directory = "effects"

    parent_dir = "SWEPBASE/lua"


    path = os.path.join(parent_dir, directory) 

    os.mkdir(path)

    with open("SWEPBASE/lua/weapons/CHANGEME/shared.lua", "w") as f:
        f.write("")
    with open("SWEPBASE/lua/effects/CHANGEME.lua", "w") as f:
        f.write("")
    with open("SWEPBASE/lua/autorun/autorun.lua", "w") as f:
        f.write("")


    

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