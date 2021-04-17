# Blender-GeoFS-Utilities
A collection of blender tools to aid with aircraft development in GeoFS.

# How to install the addon:
This addon is installed like any other downloaded blender addon. If you do not know how to do this, please follow these steps:
1) Download and save the python file
2) Open blender and find the addon section in the preferences (Edit > Preferences > Addons)
3) Select the install option in the top right corner of the window
4) Find the python file that you previously downloaded and select it, then select "Install Add-on"
5) Blender should automatically display the addon in the addon selector, but if you do not see it, search for "Collision Addon"
6) Enable the addon by ticking the tick box

The Addon should now be enabled.

# How to use the addon:
The use of the addon is quite self-explanatory however here is a short quite on it's basic use:

First of all: This addon assumes that your plane is positioned in such a way that it is the correct rotation for GeoFS. This means that the positive X axis is the forward direction.

The main panel is found in the main workspace in the side bar. The tab in which it is found is named: "GeoFS Util".
The collision section of this tab is split into two main sections; Main collisions and Gear collisions.

Main collisions:
To generate the main collision points, you first need to select the collection in which all of the points are defined. In this collection there should only be objects that are positioned where a collision point will be. Using empties for this is recommended. The script will look at all objects in this collection so even if they are not intended to be in the position of the collision point, they will be mirrored.
The "X symmetry" option will mirror any point that outside of the "Mirror Threshold" in the positive or negative. This is only done for one axis, that axis being the =/- Y axis in blender, and the +/- X axis in GeoFS. This corresponds to left/right viewed from the back of the plane. The threshold can be set to any number between 0.005 and 1.5, any points in this range will not be mirrored (only applies for the mirror axis), which is done to avoid mirroring points in the centre of the plane which are usually only needed once. 
  The "Rounding D.P." value determines to how many decimal places the output values are rounded. This ranges from 0 to 5, 0 resulting in rounding to the nearest whole number and 5 leading to the values being rounded to 5 decimal places. For the output, see the output section.

Gear Collisions:
This is mostly the same as the previous section however there is no option for mirroring. The collection selection and "Rounding D.P" functions identically to the previous section. The main difference in this is the way that the data is output and how the empties should be setup. Each gear part for this section should have at least two empties; One of these is for the position of the gear around which it will pivot and the other for the collision point of the gear. The empty/object used for the collision point has to be parented to the position/pivot point. For objects that do not have a parent a position will be printed, however if an object/empty does have a parent, it will print the name of the parent as well as a collision point.

Lights:
Lights are currently only able to be generated one at a time. For each light that is generated, a name has to be initially set which can be any name. After that, an object is required to determine the position of the light. This also uses the global position and does not consider any parent/children and when the position is printed in the output, it is rounded to the "Decimal D.P." which functions in the same way as it does for the collisions. The main unique feature in lights is the different settings that have to be chose, the type of light which determines the animation that the light has. Each of these has a tool tip that describes briefly what the light will do. The second setting is the colour, of which there are three. At the moment only basic lights are supported but more may be added in the future, if there are any specific ones, please create a feature request for them in the issues.

Instruments:
Instruments function similarly to the lights in terms of which settings have to be set. This also requires a name to be set and after that a a position has to also be chosen. This is identical to the way that lights work. The main difference to lights in in the settings, where initially the type of instrument has to be chosen. The drop down has a list of each instrument which a short description, however the names displayed will not match the ones used in GeoFS. In the output the names will be what GeoFS uses but, in the settings, they have been changed to make them easier to understand. Additionally, there is a slider that determines the scale, which will be applied equally on the x y and z axis’ to avoid distortion. The range allowed should work for all instruments, however if the values do not go high enough or are not the thing you want, it most likely best to adjust the code manually. Rotations are currently not part of the plugin as they are more complex, but also are often not used in instruments as it can make them harder to see or read. any rotations will have to be added manually to the output.

Utilities and Output:
In the utilities section there is currently only two options, the main being a short cut for toggling the system console.
**The system console is where all outputs are found**.
Once this is open you will see the output of all the operations you have carried out, or any errors that have occurred while trying to generate them.
The other main option is the shade smooth which will shade smooth and apply auto smooth to the current selected object. Please note that this will deselect all of the objects that are selected but not active in order to avoid shading errors.

Output formatting:
All of the output arrays are formatted to be ready to use in GeoFS out of the box. There should be no issues with parts being in the wrong position or please report the issue.

Bugs and issues:
There will most likely be bug or issues with the addon, especially if you are using a version on the experimental branch. If you find any issues, please either create an issue on the repository or let someone know directly. Please report issues with as much detail as possible.
