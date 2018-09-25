import os
import glob

def read_directory(folder):
    # Set the directory to chdir
    os.chdir(folder)

    # For all files that end with .shp add the file name without extension to a list
    for file in glob.glob("*.shp"):
        shapefile_names.append(file[0:-4])
    print('These are the shapefiles in your directory: {}'.format(shapefile_names))
    # Return the list of file names
    return shapefile_names


def create_sub_directory(shapefile_names):
    # Create sub_directories for each shapefile in shapefile_names
    for shapefile in shapefile_names:
        newpath = r'{}_shapefile'.format(shapefile)
        if not os.path.exists(newpath):
            os.makedirs(newpath)

def move_shapefiles(shapefile_names):
    # List of extensions (not every shapefile has all of these extensions)
    list_of_shp_extensions = ['.shp', '.shx', '.dbf', '.sbn', '.sbx',
                              '.fbn', '.fbx', '.ain', '.aih', '.atx', '.ixs',
                              '.mxs', '.prj', '.xml', '.cpg', '.shp.xml']
    # Move all the files that are in the shapefile_names list and have a proper extension to the corresponding folder
    for shapefile in shapefile_names:
        for extension in list_of_shp_extensions:
            file = r'{}{}'.format(shapefile, extension)
            file_path = r'{}_shapefile/{}'.format(shapefile,file)
            if os.path.isfile(file):
                os.rename(file, file_path)
            else:
                continue



def main(folder):
    shapefile_names = read_directory(folder)

    create_sub_directory(shapefile_names)

    move_shapefiles(shapefile_names)

main(r'D:\Documenten\Studentassistent_17-18\Introgis17')