# Shapefile directory organizer
### Work in progress

A Shapefile is one of the most used geographical data formats (https://desktop.arcgis.com/en/arcmap/10.3/manage-data/shapefiles/what-is-a-shapefile.htm).  Currently this format it is the propietary standard in geospatial analysis. Although more effective alternatives exists, many users still prefer ESRI Shapefiles.

A disadvantages of a shapefile is the multitude of files that form a single shapefile. For many users this leads to organized data directories and user errors when moving files. This tools lists all the shapefiles in a directory and moves each of them to a to a new folder corresponding to the shapefile's file name.

The program works as follows:
* Find a folder with one or more shapefiles
![alt text](https://i.imgur.com/JxKwDKM.png)
* Start the GUI.py;

![alt text](https://i.imgur.com/ntmDyVQ.png)
* Press 'Browse' to select the folder;
* Press 'Clean Directory';
* Read the pop-up message and check the result;

![alt text](https://i.imgur.com/Wijajxq.png)

![alt text](https://i.imgur.com/mlAyK4y.png)

* Clean another folder or press 'Quit'

### To do:
* Command line interface;
* Non Tkinter GUI.
