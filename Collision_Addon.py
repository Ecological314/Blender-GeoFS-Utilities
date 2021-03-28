# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Collision Addon",
    "author" : "A Name",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 1, 1),
    "location" : "View3D > Sidebar > Geo Collisions",
    "warning" : "",
    "category" : "Generic"
}

#Importing all of the things
import bpy
from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       )
from bpy.types import (AddonPreferences,
                       PropertyGroup,
                       )
#Property settings
class MySettings(PropertyGroup):

    x_symmetry : BoolProperty(
        name="X Symmetry",
        description="Enables main collision mirroring on the x axis",
        default = False
        )
    roundDpProp : IntProperty(
        name = "Rounding Decimal Place",
        description="Sets the decimal place for rounding(0 = integer, 5 = 5 decimal places)",
        default = 2,
        min = 0,
        max = 5
        )
    mirrorThreshProp : FloatProperty(
        name = "Mirror Threshold",
        description = "Threshold for the points which are mirrored mirroring",
        default = 0.3,
        min = 0.05,
        max = 1.5
        )
    gearRoundDpProp : IntProperty(
        name = "Gear Rounding Decimal Place",
        description="Sets the decimal place for rounding(0 = integer, 5 = 5 decimal places) in the Gear section",
        default = 2,
        min = 0,
        max = 5
        )

#UI panel
from bpy.types import Panel
class Main_panel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Geo Collisions"
class GCOL_PT_Panel_Parent(Main_panel, Panel):
    bl_idname = "GCOL_PT_Panel_Parent"
    bl_label = "Collisions"
    def draw(self, context):
        layout = self.layout
class GCOL_PT_Panel_Col(Main_panel,Panel):
    bl_parent_id = "GCOL_PT_Panel_Parent"
    bl_label = "Main Collisions"

    def draw(self, context):
        
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        #Draw main collision generate button
        row = layout.row()
        col = row.column()
        col.operator("object.get_collisions", text = "Generate Main Collisions", icon = "PLUS")
        #Draw Collection selector
        col.prop(scene, "collisionCollection", text="Collision Point Collection")
        #Draw symmetry toggle
        layout.prop(mytool, "x_symmetry", text="X Symmetry")
        #Draw rounding and threshold selectors
        layout.prop(mytool, "roundDpProp", text="Rounding D.P.")
        layout.prop(mytool, "mirrorThreshProp", text="Mirror Threshold")    
class GCOL_PT_Panel_Gear(Main_panel,Panel):
    bl_parent_id = "GCOL_PT_Panel_Parent"
    bl_label = "Gear Collisions"

    def draw(self, context):
        
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        #Draw Gear Collision button 
        row = layout.row()
        col = row.column()
        col.operator("object.get_collisions_gear", text = "Generate Gear Collisions", icon = "PLUS")
        #Draw gear collection selector
        col.prop(scene, "gearCollection", text="Gear Point Collection")
        #Draw gear rouding selector
        layout.prop(mytool, "gearRoundDpProp", text="Rounding D.P.")
class GCOL_PT_Panel_Util(Main_panel,Panel):
    bl_idname = "GCOL_PT_Panel_Utils"
    bl_label = "Utilities"

    def draw(self, context):
        
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        #Draw Console Toggle
        row = layout.row()
        col = row.column()
        col.operator("object.toggle_console", text = "Toggle Output Console", icon = "CONSOLE")

#Operators
from bpy.types import Operator
#Operator for main collision points
class GCOL_OT_Gen_MainCollisions(Operator):
    """Generates Main Collision Array"""
    bl_idname = "object.get_collisions"
    bl_label = "Generate Main Collisions"
    
    def execute(self, context):
        roundDp = context.scene.my_tool.roundDpProp
        mirrorThresh = round(context.scene.my_tool.mirrorThreshProp, 5)
        symmetry_ON = context.scene.my_tool.x_symmetry

        collections = bpy.data.collections
        selectedCollection = bpy.context.scene.collisionCollection
        collisionsFound = False

        for c in collections:

            if selectedCollection == None:
                print("No collection selected")
                break
            
            selectedColLen = len(selectedCollection.objects)
            if selectedColLen == 0:
                print("No objects in collection")
                break

            cName = c.name
            slectedColName = selectedCollection.name

            if cName == slectedColName:
                currentObject = 0
                collisionsFound = True
                empties = selectedCollection.objects
                emptiesAmount = len(empties)
                print("Collisions: \n")
                print("\"collisionPoints\": [")
                
                for x in empties:
                    name = x.name
                    currentObject += 1

                    locX = round(-x.location[1], roundDp)
                    locY = round(x.location[0],roundDp)
                    locZ = round(x.location[2],roundDp)
                    mirLocX = -locX
                    
                    if currentObject == emptiesAmount:
                        if locX <= -mirrorThresh or locX >= mirrorThresh and symmetry_ON:
                            print(f'[{locX},{locY},{locZ}],')
                            print(f'[{mirLocX},{locY},{locZ}]')
                        else:
                            print(f'[{locX},{locY},{locZ}]')
                    else:
                        if locX <= -mirrorThresh or locX >= mirrorThresh and symmetry_ON:
                            print(f'[{locX},{locY},{locZ}],')
                            print(f'[{mirLocX},{locY},{locZ}],')
                        else:
                            print(f'[{locX},{locY},{locZ}],')
                print(f'] \n')   
             
        return{'FINISHED'}
#Operator for gear collision points
class GCOL_OT_Gen_GearCollisions(Operator):
    """Generates Gear Collisions and Positions"""
    bl_idname = "object.get_collisions_gear"
    bl_label = "Generates Gear Collisions + Possition"
    
    def execute(self, context):
        roundDp = context.scene.my_tool.gearRoundDpProp
        collections = bpy.data.collections
        collisionsFound = False

        selectedCollection = bpy.context.scene.gearCollection

        for c in collections:
            
            if selectedCollection == None:
                print("No gear collection selected")
                break
            
            selectedColLen = len(selectedCollection.objects)
            if selectedColLen == 0:
                print("No objects in collection")
                break

            cName = c.name
            slectedColName = selectedCollection.name

            if cName == slectedColName:
                collisionsFound = True
                print("Gear collisions:")
                gEmpties = selectedCollection.objects
                gEmptiesAmount = len(gEmpties)
                for x in gEmpties:
                    locX = round(-x.location[1], roundDp)
                    locY = round(x.location[0],roundDp)
                    locZ = round(x.location[2],roundDp)
                    name = x.name
                    
                    parent = x.parent
                    if parent == None:
                        print(f'{name}:')
                        print(f'\"position\": [{locX},{locY},{locZ}], \n')
                    else:
                        cLocX = round(locX - (-parent.location[1]),roundDp)
                        cLocY = round(locY - parent.location[0],roundDp)
                        cLocZ = round(locZ - parent.location[2],roundDp)
                        parentName = x.parent.name
                        print(f'{name}:')
                        print(f'\"parent\": \"{parentName}\",')
                        print(f'\"collisionPoints\": [[{cLocX},{cLocY},{cLocZ}]], \n')
                    
        return{'FINISHED'}
#Operator for toggeling the console
class GCOL_OT_toggle_console(Operator):
    """Toggles the system console"""
    bl_idname = "object.toggle_console"
    bl_label = "Toggles the system console"
    
    def execute(self, context):
        
        bpy.ops.wm.console_toggle()

        return{'FINISHED'}

#Registering all of the classes
classes = (GCOL_OT_Gen_MainCollisions, MySettings, GCOL_OT_toggle_console, GCOL_OT_Gen_GearCollisions, GCOL_PT_Panel_Parent, GCOL_PT_Panel_Col, GCOL_PT_Panel_Gear, GCOL_PT_Panel_Util)

def register():
    
    for c in classes:
        bpy.utils.register_class(c)
    
    bpy.types.Scene.my_tool = PointerProperty(type=MySettings)
    bpy.types.Scene.collisionCollection = PointerProperty(type=bpy.types.Collection, name="Collision Point Collection", description="Collection from which the collisions are found")
    bpy.types.Scene.gearCollection = PointerProperty(type=bpy.types.Collection, name="Gear Point Collection", description="Collection from which the gear possitions/collisions are found")

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

    del bpy.types.Scene.my_tool
    del bpy.types.Scene.gearCollection
    del bpy.types.Scene.collisionCollection
