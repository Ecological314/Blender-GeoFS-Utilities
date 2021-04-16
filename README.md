# Blender-GeoFS-Utilities
A collection of blender tools to aid with aircraft development in GeoFS.

# How to install the addon:
This addon is installed like any other downloaded blender addon. If you do not know how to do this, please follow these steps:
1) Download and save the python file
2) Open blender and find the addon section in the preferences(Edit > Preferences > Addons)
3) Select the install option in the top right corner of the window
4) Find the python file that you previously downloaded and select it, then select "Install Add-on"
5) Blender should automatically display the addon in the addon selector, but if you do not see it, search for "Collision Addon"
6) Enable the addon by ticking the tick box
The Addon should now be enabled

# How to use the addon:
The use of the addon is quite self explanatory however here is a short quite on it's basic use:

First of all: This addon assumes that your plane is possitioned in such a way that it is the correct rotaition for GeoFS. THis means that the possitive X axis is the forward direction.

The main panel is found in the main workspace in the side bar. The tab in which it is found is labled:"Geo Collisions".
The collision section of this tab is split into two main sections; Main collisions and Gear collisions.
Main collisions:
  To generate the main collision points, you first need to select the collection in which all of the points are defined. In this collection there should only be objects that are possitioned where a collision point will be. Using empties for this is recomended. The script will look at all objects in this collection so even if they are not intended to be in the possition of the collision point, they will be mirrored.
  The "X symmetry" option will mirror any point that outside of the "Mirror Threshold" in the possitive or negative. This is only done for one axis, that axis being the =/- Y axis in blender, and the +/- X axis in GeoFS. This corresponds to left/right viewed from the back of the plane. The threshold can be set to any number between 0.005 and 1.5, any points in this range will not be mirrored(only applies for the mirror axis), which is done to avoid mirroring points in the center of the plane which are usually only needed once. 
  The "Rounding D.P." value determines to how many decimal places the output values are rounded. This ranges from 0 to 5, 0 resulting in rouding to the nearest whole number and 5 leading to the values being rounded to 5 decimal places. For the output, see the output section.
Gear Collisions:
  This is mostly the same as the previous section however there is no option for mirroring. The collection selection and "Rounding D.P" functions identiacally to the previous section. The main difference in this is the way that the data is outputed and how the empties should be setup. Each gear part for this section should have at least two empties; One of these is for the position of the gear around which it will pivot and the other for the collision point of the gear. The empty/object used for the collision point has to be parented to the position/pivot point. For objects that do not have a parent a possition will be printed, however if an object.empty does have a parent, it will print the name of the parent as well as a collision point.

Utilies and Output:
In the utlities section there is currently only one option, that being a short cut for toggleing the system console.
**The system console is where all outputs are found**.
Once this is open you will see the output of all the operaitions you have carried out, or any errors that have occured while trying to generate them.

Output formating:
All of the output arrays are formated to be ready to use in GeoFS out of the box. There should be no issues with parts being in the wrong possition or please report the issue.
