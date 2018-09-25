import os
import glob

def read_directory(folder):
    # Set the directory to chdir
    os.chdir(folder)
    # Return a list shapefile_names
    shapefile_names = []
    for file in glob.glob("*.shp"):
        shapefile_names.append(file[0:-4])
    print('These are the shapefiles in your directory: {}'.format(shapefile_names))
    return shapefile_names


def create_sub_directory(shapefile_names):
    # Create sub_directories for each shapefile in shapefile_names
    for shapefile in shapefile_names:
        newpath = r'{}_shapefile'.format(shapefile)
        if not os.path.exists(newpath):
            os.makedirs(newpath)

def move_shapefiles(shapefile_names):
    # Move all the shapefiles to their new folders
    list_of_shp_extensions = ['.shp', '.shx', '.dbf', '.sbn', '.sbx',
                              '.fbn', '.fbx', '.ain', '.aih', '.atx', '.ixs',
                              '.mxs', '.prj', '.xml', '.cpg', '.shp.xml']
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