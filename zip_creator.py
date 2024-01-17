import zipfile
import pathlib

def make_archive(name, file, folders):
    the_paths = pathlib.Path(folders, f"{name}.zip")
    with zipfile.ZipFile(the_paths, "w", zipfile.ZIP_DEFLATED) as z:
        for i in file:
            z.write(i, arcname=pathlib.Path(i).name)
