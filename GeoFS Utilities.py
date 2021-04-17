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
    "name" : "GeoFS Utilities",
    "author" : "A Name",
    "description" : "Adds several different utilites for GeoFS aircraft developmet",
    "blender" : (2, 92, 0),
    "version" : (0, 2, 1),
    "location" : "View3D > Sidebar > GeoFS Util",
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
    lightType : EnumProperty(
        name="Type",
        items=(
            ('none', 'Navigaition', 'Navigation light that is always on'),
            ('night', 'Navigaition Night', 'Navigation light that is on at night'),
            ('strobe1', 'Stobe 1', 'Strobe light that '),
            ('strobe2', 'Strobe 2', 'Strobe light that'),
            ('strobe3', 'Strobe 3', 'Strobe light that'),
        )
        )
    lightColour : EnumProperty(
        name="Type",
        items=(
            ('red', 'Red', 'Sets the light colour to red'),
            ('green', 'Green', 'Sets the light colour to green'),
            ('white', 'White', 'Sets the light colour to white'),
        )
        )
    lightName : StringProperty(
        name="Name",
        default="untitled"
        )
    lightRoundDpProp : IntProperty(
        name = "Light Rounding Decimal Place",
        description="Sets the decimal place for rounding(0 = integer, 5 = 5 decimal places) for the light",
        default = 2,
        min = 0,
        max = 5
        )
    instrumentType : EnumProperty(
        name="Type",
        items=(
            ('attitude', 'Artifical Horizon GA', 'General Aviaition artifical horizon'),
            ('attitude-jet', 'Artifical Horizon Jet 1', 'Jet Aircraft artifical horizon, first style'),
            ('attitude-jet2', 'Artifical Horizon Jet 2', 'Jet Aircraft artifical horizon, second style'),
            ('altimeter', 'Altimeter', 'General Aviaition artifical horizon'),
            ('ias', 'IAS GA', 'General Aviaition IAS gauge'),
            ('ias-high', 'IAS', 'Normal jet aircraft IAS guage'),
            ('ias-supersonic', 'IAS Supersonic', 'Supersonic aircraft IAS guage'),
            ('compass', 'Compass', 'Standard compass/heading indicator'),
            ('vario', 'V-Speed 2000', 'Standard max 2000fpm(+/-) vertical speed indicator'),
            ('vario-high', 'V-Speed 6000', 'Standard max 6000fpm(+/-) vertical speed indicator'),
            ('rpm', 'RPM Prop', 'RPM gauge up to 8000rpm usually for prop aircraft'),
            ('rpm-jet', 'RPM Jet', 'RPM gauge up to 10000rpm usually for jet aircraft'),
            ('turn-coordinator', 'Turn Coordinator', 'Standard turn and slip indicator'),
            ('gmeter', 'G Meter', 'Indicator for the current G Forces'),
            ('compassball', 'Compass Ball', 'Compassball that indicats heading'),
            ('manifold', 'Manifold', 'Indicates manifold pressure and fuel flow'),
            ('oil', 'Oil Gauge', 'Indicates oil presure and temperature'),
        )
        )
    instrumentName : StringProperty(
        name="Name",
        default="untitled"
        )
    instRoundDpProp : IntProperty(
        name = "Light Rounding Decimal Place",
        description="Sets the decimal place for rounding(0 = integer, 5 = 5 decimal places) for the instrument",
        default = 2,
        min = 0,
        max = 5
        )
    instScaleProp : FloatProperty(
            name = "Instrument Scale",
            description = "Sets the scale of the instrument",
            default = 1,
            min = 0.2,
            max = 5
            )

#UI panel
from bpy.types import Panel
class Main_panel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "GeoFS Utils"
class GCOL_PT_Panel_Parent(Main_panel, Panel):
    bl_idname = "GCOL_PT_Panel_Parent"
    bl_label = "Collisions"
    bl_options = {"DEFAULT_CLOSED"}
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
        layout.prop(mytool, "instScaleProp", text="Mirror Threshold")    
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
class GCOL_PT_Panel_Lights(Main_panel,Panel):
    bl_idname = "GCOL_PT_Panel_Lights"
    bl_label = "Lights"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self,context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        #Draw generate button
        row = layout.row()
        col = row.column()
        col.operator("object.get_light", text = "Generate Light", icon = "PLUS")
        #Draw settings
        row = layout.row()
        layout.prop(mytool, "lightName", text="Name")
        row = layout.row()
        layout.prop(scene, "selectLight", text="Location")
        layout.prop(mytool, "lightRoundDpProp", text="Rounding D.P.")
        row = layout.row()
        layout.prop(mytool, "lightType", text="Type")
        layout.prop(mytool, "lightColour", text="Colour")
class GCOL_PT_Panel_Instruments(Main_panel,Panel):
    bl_idname = "GCOL_PT_Panel_Instruments"
    bl_label = "Instruments"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self,context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        #Draw generate button
        row = layout.row()
        col = row.column()
        col.operator("object.get_instrument", text = "Generate Instrument", icon = "PLUS")
        #Draw settings
        row = layout.row()
        layout.prop(mytool, "instrumentName", text="Name")
        row = layout.row()
        layout.prop(scene, "selectInst", text="Location")#Locaition object picture
        layout.prop(mytool, "instRoundDpProp", text="Rounding D.P.")
        row = layout.row()
        layout.prop(mytool, "instrumentType", text="Type")
        layout.prop(mytool, "instScaleProp", text="Scale")
        layout.label(text = "Rotations not supported")
class GCOL_PT_Panel_Util(Main_panel,Panel):
    bl_idname = "GCOL_PT_Panel_Utils"
    bl_label = "Utilities"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        #Draw Console Toggle
        row = layout.row()
        col = row.column()
        col.operator("object.extra_smooth", text = "Shade Smooth")
        col = row.column()
        col.operator("object.merge_by_distance", text = "Remove Duplicates")
        #row = layout.row()
        #col = row.column()
        #col.operator("object.extra_smooth", text = "Apply all Modifiers")
        #col = row.column()
        #col.operator("object.extra_smooth", text = "Remove all Modifiers")
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
#Light Generator
class GCOL_OT_Gen_Light(Operator):
    """Generates one light form the current settings"""
    bl_idname = "object.get_light"
    bl_label = "Generates a section of code for a light"

    def execute(self, context):

        locObj = context.scene.selectLight
        if locObj == None:
            print("No location object selected")
            return{'FINISHED'}

        lName = context.scene.my_tool.lightName
        roundDp = context.scene.my_tool.lightRoundDpProp
        lType = context.scene.my_tool.lightType
        lColour = context.scene.my_tool.lightColour

        lLocX = round(-locObj.location[1], roundDp)
        lLocY = round(locObj.location[0],roundDp)
        lLocZ = round(locObj.location[2],roundDp)
        
        print("{")
        print(f'\"name\":\"{lName}\",')
        print(f'\"light\":\"{lColour}\",')
        
        if lType == 'none':
            print("\"animations\": \"\",")
        else:
            print("\"animations\": [")
            print("{",f'"type": "show", "value": "{lType}"',"}")
            print("],")
        
        print(f'\"position\": [{lLocX},{lLocY},{lLocZ}]')
        print("},")
        return{'FINISHED'}
#Instrument Generator
class GCOL_OT_Gen_Instrument(Operator):
    """Generates instrumentn code from the selected settings"""
    bl_idname = "object.get_instrument"
    bl_label = "Generates a section of code for a instrument"

    def execute(self, context):

        locObj = context.scene.selectInst
        if locObj == None:
            print("No location object selected")
            return{'FINISHED'}

        instName = context.scene.my_tool.instrumentName
        roundDp = context.scene.my_tool.instRoundDpProp
        instType = context.scene.my_tool.instrumentType
        instScale = round(context.scene.my_tool.instScaleProp, roundDp)

        lLocX = round(-locObj.location[1], roundDp)
        lLocY = round(locObj.location[0],roundDp)
        lLocZ = round(locObj.location[2],roundDp)
        
        print("{")
        print(f'\"name\":\"{instName}\",')
        print(f'\"include\":\"3d-{instType}\",')
        print("\"type\": \"none\",")
        print(f'\"position\": [{lLocX},{lLocY},{lLocZ}],')
        print("\"rotation\":[0, 0, 0],")
        print(f'\"scale\": [{instScale}, {instScale}, {instScale}]')
        print("},")
        return{'FINISHED'}
#Operator for toggeling the console
class GCOL_OT_toggle_console(Operator):
    """Toggles the system console"""
    bl_idname = "object.toggle_console"
    bl_label = "Toggles the system console"
    
    def execute(self, context):
        
        bpy.ops.wm.console_toggle()

        return{'FINISHED'}
#Shade smooth operator
class GCOL_OT_shadeSmooth(Operator):
    """Shades object smooth and enables auto-smooth"""
    bl_idname = "object.extra_smooth"
    bl_label = "Applies auto-smooth and shade smooth"

    @classmethod
    def poll(cls, context):
        selectObj = bpy.context.object

        if selectObj is not None:
            if selectObj.mode == "OBJECT":
                return True

        return False

    def execute(self, context):
        activeObj = bpy.context.selected_objects
        activeObjName = bpy.context.active_object.name

        for obj in activeObj:
            if obj.name != activeObjName:
                obj.select_set(False)

        bpy.ops.object.shade_smooth()
        bpy.context.object.data.use_auto_smooth = True
        return{'FINISHED'}
#Remove Dupliactes
class GCOL_OT_removeDoubles(Operator):
    """Removes duplicate vertices by mergiving vertisies by distance"""
    bl_idname = "object.merge_by_distance"
    bl_label = "Shortcut to merge by distance"

    @classmethod
    def poll(cls, context):
        selectObj = bpy.context.object

        if selectObj is not None:
            if selectObj.mode == "EDIT":
                return True

        return False

    def execute(self, context):
        
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles()
        bpy.ops.mesh.select_all(action='DESELECT')

        return{'FINISHED'}


#Registering all of the classes
classes = (
    GCOL_OT_Gen_MainCollisions, 
    MySettings, 
    GCOL_OT_toggle_console, 
    GCOL_OT_Gen_GearCollisions,
    GCOL_OT_Gen_Light,
    GCOL_OT_Gen_Instrument,
    GCOL_OT_shadeSmooth,
    GCOL_OT_removeDoubles, 
    GCOL_PT_Panel_Parent, 
    GCOL_PT_Panel_Col, 
    GCOL_PT_Panel_Gear,
    GCOL_PT_Panel_Lights,
    GCOL_PT_Panel_Instruments, 
    GCOL_PT_Panel_Util)

def register():
    
    for c in classes:
        bpy.utils.register_class(c)
    
    bpy.types.Scene.my_tool = PointerProperty(type=MySettings)
    bpy.types.Scene.collisionCollection = PointerProperty(type=bpy.types.Collection, name="Collision Point Collection", description="Collection from which the collisions are found")
    bpy.types.Scene.gearCollection = PointerProperty(type=bpy.types.Collection, name="Gear Point Collection", description="Collection from which the gear possitions/collisions are found")
    bpy.types.Scene.selectLight = PointerProperty(type=bpy.types.Object, name="Light Possition", description="Object from which the locaition of the light is found")
    bpy.types.Scene.selectInst = PointerProperty(type=bpy.types.Object, name="Instrument Possition", description="Object from which the locaition of the light is found")

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

    del bpy.types.Scene.my_tool
    del bpy.types.Scene.gearCollection
    del bpy.types.Scene.collisionCollection
    del bpy.types.Scene.selectLight
    del bpy.types.Scene.selectInst
