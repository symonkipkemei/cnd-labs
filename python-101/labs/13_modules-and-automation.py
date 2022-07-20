import pathlib

#path to the desktop
desktop = pathlib.Path("/home/symon_kipkemei")


#create a new folder folder
new_path = pathlib.Path("/home/symon_kipkemei/screenshots")
new_path.mkdir(exist_ok=True)

# list items in desktop
for filepath in desktop.iterdir():
    #filter screenshots only
    if filepath.suffix == ".db":
        # create new path for each file
        new_file_path = new_path.joinpath(filepath.name)

        # move the screenshot there
        filepath.replace(new_file_path)

