"""
Author: Jimmy Frando
Name:Three-Point Light Rig
Class: Tools Programming
Date: 5/8/2015
This script creates a UI for the user that allows them to create a quick three-point light rig set-up
that they can use to get quick lighting results on their subject.

To use this script, simply run it in the maya script editor. 
"""

import maya.cmds as mc
from functools import partial

#LightRig class
class LightRig(object):
    #special runs at creation of LightRig object
    def __init__(self,rigVal,timeVal):
        self.lightRigType = rigVal
        self.timeOfDay = timeVal
		

    #method that creates the light rig			
    def create(self):
        print self.lightRigType
        print self.timeOfDay
        
		#Create locator at origin
        self.lightRigLoc = mc.spaceLocator( name = "lightRig_loc" )
        mc.scale(6,6,6)
        
		#If the user  selected indoor...
        if (self.lightRigType == 1 ):
            print "Indoor Lights"
			
			#Create Key light
            self.lightRigKey = mc.spotLight( name = "lightRig_keyLight", rgb = [1.0,1.0,0.916], dropOff = 0.250, intensity = 1.5, penumbra = 25, coneAngle = 21 )
            mc.setAttr( "lightRig_keyLightShape.useDepthMapShadows", 1)
            mc.setAttr( "lightRig_keyLightShape.dmapResolution", 1024)
            mc.setAttr( "lightRig_keyLightShape.dmapFilterSize", 8)
            mc.move( 13,27,21 )
            mc.rotate( -41, 31.5, 0 )
            
			#Create fill light
            self.lightRigFill = mc.spotLight( name = "lightRig_fillLight", rgb = [0.354,0.360,0.624], intensity = 1.25, coneAngle = 30, penumbra = 70, dropOff = 1.25, rs = False)
            mc.setAttr( "lightRig_fillLightShape.emitSpecular", 0)
            mc.move( -19, 17, 20 )
            mc.rotate( -22.8, -44, 0 )
            
			#Create back light
            self.lightRigFill = mc.spotLight( name = "lightRig_backLight", rgb = [1.0,1.0,0.657], intensity = 1.8, coneAngle = 30, rs = False)
            mc.move(-4,14,-25)
            mc.rotate( -17.4, 189.2, 0 )
		
		#If User selected outdoor and morning
        elif (self.lightRigType == 2 and self.timeOfDay == 1):
            print "Outdoor Lights: Morning"
			
			#Create Key light
            self.lightRigKey = mc.spotLight( name = "lightRig_keyLight", rgb = [1.0,0.863,0.408], dropOff = 0.250, intensity = 1.5, penumbra = 25, coneAngle = 21 )
            mc.setAttr( "lightRig_keyLightShape.useDepthMapShadows", 1)
            mc.setAttr( "lightRig_keyLightShape.dmapResolution", 1024)
            mc.setAttr( "lightRig_keyLightShape.dmapFilterSize", 8)
            mc.move( 13,27,21 )
            mc.rotate( -41, 31.5, 0 )
            
			#Create fill light
            self.lightRigFill = mc.spotLight( name = "lightRig_fillLight", rgb = [0.354,0.416,0.624], intensity = 1.25, coneAngle = 30, penumbra = 70, dropOff = 1.25, rs = False)
            mc.setAttr( "lightRig_fillLightShape.emitSpecular", 0)
            mc.move( -19, 17, 20 )
            mc.rotate( -22.8, -44, 0 )
            
			#Create back light
            self.lightRigFill = mc.spotLight( name = "lightRig_backLight", rgb = [1.0,0.863,0.148], intensity = 1.8, coneAngle = 30, rs = False)
            mc.move(-4,14,-25)
            mc.rotate( -17.4, 189.2, 0 )
         
		#If User selected outdoor and noon
        elif (self.lightRigType == 2 and self.timeOfDay == 2):
            print "Outdoor Lights: Noon"
			
			#Create key light
            self.lightRigKey = mc.spotLight( name = "lightRig_keyLight", rgb = [0.882,0.963,1.0], dropOff = 0.250, intensity = 1.5, penumbra = 25, coneAngle = 21 )
            mc.setAttr( "lightRig_keyLightShape.useDepthMapShadows", 1)
            mc.setAttr( "lightRig_keyLightShape.dmapResolution", 1024)
            mc.setAttr( "lightRig_keyLightShape.dmapFilterSize", 8)
            mc.move( 13,27,21 )
            mc.rotate( -41, 31.5, 0 )
            
			#Create fill light
            self.lightRigFill = mc.spotLight( name = "lightRig_fillLight", rgb = [1.0,0.949,0.882], intensity = 1.25, coneAngle = 30, penumbra = 70, dropOff = 1.25, rs = False)
            mc.setAttr( "lightRig_fillLightShape.emitSpecular", 0)
            mc.move( -19, 17, 20 )
            mc.rotate( -22.8, -44, 0 )
			
            #Create back light
            self.lightRigFill = mc.spotLight( name = "lightRig_backLight", rgb = [0.882,0.963,0.740], intensity = 1.8, coneAngle = 30, rs = False)
            mc.move(-4,14,-25)
            mc.rotate( -17.4, 189.2, 0 )
        
		#If User selected outdoor and night
        elif (self.lightRigType == 2 and self.timeOfDay == 3):
            print "Outdoor Lights: Midnight"
			
			#Create key light
            self.lightRigKey = mc.spotLight( name = "lightRig_keyLight", rgb = [0.118,0.133,0.247], dropOff = 0.250, intensity = 1.5, penumbra = 25, coneAngle = 21 )
            mc.setAttr( "lightRig_keyLightShape.useDepthMapShadows", 1)
            mc.setAttr( "lightRig_keyLightShape.dmapResolution", 1024)
            mc.setAttr( "lightRig_keyLightShape.dmapFilterSize", 8)
            mc.move( 13,27,21 )
            mc.rotate( -41, 31.5, 0 )
            
			#Create fill light
            self.lightRigFill = mc.spotLight( name = "lightRig_fillLight", rgb = [0.247,0.241,0.118], intensity = 1.25, coneAngle = 30, penumbra = 70, dropOff = 1.25, rs = False)
            mc.setAttr( "lightRig_fillLightShape.emitSpecular", 0)
            mc.move( -19, 17, 20 )
            mc.rotate( -22.8, -44, 0 )
            
			#Create back light
            self.lightRigFill = mc.spotLight( name = "lightRig_backLight", rgb = [0.118,0.133,0.163], intensity = 1.8, coneAngle = 30, rs = False)
            mc.move(-4,14,-25)
            mc.rotate( -17.4, 189.2, 0 )
        
		#Constrain the lights to the locator
        mc.parentConstraint( "lightRig_loc", "lightRig_keyLight", mo = True )
        mc.parentConstraint( "lightRig_loc", "lightRig_fillLight", mo = True )
        mc.parentConstraint( "lightRig_loc", "lightRig_backLight", mo = True )
        
		#Group lights and locator under a named group
        mc.group( "lightRig_loc", "lightRig_keyLight", "lightRig_fillLight", "lightRig_backLight", n = "lightRig_grp" )
            
            
#OptionsWindow class that creates UI for the user
class OptionsWindow(object):
    #@classmethod
    def showUI(cls):
        win = cls()
        win.create()
        return win
		
	#special method runs at creation
    def __init__(self):
        self.window = "optionsWindow"
        self.title = "Three-Point Light Rig"
        self.size = (546,350)
        self.rigBtnVal = 1
        self.dayBtnVal = 0
        

    #Create UI   
    def create(self):
        if mc.window(self.window,exists=True): 
            mc.deleteUI(self.window,window=True)

        self.window = mc.window(self.window, title=self.title,widthHeight=self.size,menuBar=True)
        self.mainForm = mc.formLayout(nd=100)
        self.commandMenu()
        self.commonButtons()
        
       
        self.secondForm = mc.formLayout(nd=100)
        self.lightRigTypeText = mc.text( label = "Rig Type:", height = 15)
        radBtnCollection1 = mc.radioCollection()
        self.indoorRadBtn = mc.radioButton( "indoorRadBtn", label = "Indoor", onCommand = partial(self.rigBtnToggle,1) )
        self.outdoorRadBtn = mc.radioButton( "outdoorRadBtn",label = "Outdoor", onCommand = partial(self.rigBtnToggle,2) )
        
        self.timeOfDayText = mc.text( label = "Time of Day:", height = 15)
        radBtnCollection2 = mc.radioCollection()
        self.morningRadBtn = mc.radioButton( "morningRadBtn", label = "Morning", enable = True, onCommand = partial(self.dayBtnToggle,1)  )
        self.noonRadBtn = mc.radioButton( "noonRadBtn", label = "Noon", enable = True, onCommand = partial(self.dayBtnToggle,2) )
        self.nightRadBtn = mc.radioButton( "nightRadBtn", label = "Night", enable = True, onCommand = partial(self.dayBtnToggle,3) )
        
        mc.formLayout( self.secondForm, e = True, attachForm = ( [self.lightRigTypeText,"left", 135],[self.lightRigTypeText, "bottom", 500], 
                                                                        [self.indoorRadBtn, "left", 185],[self.indoorRadBtn, "bottom", 497],
                                                                        [self.outdoorRadBtn, "left", 185],[self.outdoorRadBtn, "bottom", 477],
                                                                        [self.timeOfDayText,"left", 120], [self.timeOfDayText, "bottom", 452],
                                                                        [self.morningRadBtn, "left", 185],[self.morningRadBtn, "bottom", 449],
                                                                        [self.noonRadBtn, "left", 185],[self.noonRadBtn, "bottom", 429],
                                                                        [self.nightRadBtn, "left", 185],[self.nightRadBtn, "bottom", 409]))
                                                                        
        mc.radioCollection( radBtnCollection1, edit=True, select = self.indoorRadBtn )               
       
        self.displayOptions()
        mc.showWindow()
    
#Create menus	
    def commandMenu(self):
        self.editMenu = mc.menu(label="Edit")
        self.editMenuSave = mc.menuItem(label="Save Settings",command=self.editMenuSaveCmd)
        self.editMenuReset = mc.menuItem(label="Reset Settings",command=self.editMenuResetCmd)
        self.helpMenu = mc.menu(label="Help")
        self.helpMenuItem = mc.menuItem(label="Help on %s"%(self.title),command=self.helpMenuCmd)
    
	#Create help menu
    def helpMenuCmd(self,*args):
        mc.launch(web="http://maya-python.com")
    
    
    def editMenuSaveCmd(self,*args):pass
    
    def editMenuResetCmd(self,*args):pass
    
	#method executed when Create button is clicked
    def actionCmd(self,*args):
        lightRig = LightRig(self.rigBtnVal, self.dayBtnVal)
        lightRig.create()
        if mc.window(self.window,exists=True): 
            mc.deleteUI(self.window,window=True)
        print "ACTION"
		
	#method executed when Apply button is clicked
    def applyBtnCmd(self,*args):
        lightRig = LightRig(self.rigBtnVal, self.dayBtnVal)
        lightRig.create()
        print "APPLY"
	
	#method executed when Close button is clicked
    def closeBtnCmd(self,*args):
        mc.deleteUI(self.window,window=True)
		
	#Creates Buttons on the bottom of the UI
    def commonButtons(self):
        self.commonBtnSize=(self.size[0]-18/3,26)
        self.acctionBtn=mc.button(label="Create",height=self.commonBtnSize[1], command = self.actionCmd)    
        self.applyBtn=mc.button(label="Apply",height=self.commonBtnSize[1],command=self.applyBtnCmd)
        self.closeBtn = mc.button(label="Close",height=self.commonBtnSize[1],command=self.closeBtnCmd)
        
        
        mc.formLayout(self.mainForm, e=True, attachForm=([self.acctionBtn,"left",5],
                                                         [self.acctionBtn,"bottom",5],
                                                         [self.applyBtn,"bottom",5],
                                                         [self.closeBtn,"bottom",5],
                                                         [self.closeBtn,"right",5]),
                                             attachPosition=([self.acctionBtn,"right",1,33],
                                                             [self.closeBtn,"left",0,67]),
                                             attachControl=([self.applyBtn,"left",4,self.acctionBtn],
                                                            [self.applyBtn,"right",4,self.closeBtn]),
                                             attachNone=([self.acctionBtn,"top"],
                                                         [self.applyBtn,"top"],
                                                         [self.closeBtn,"top"]))
    def displayOptions(self):pass
    
	#Method called when the type of rig is selected by the user
    def rigBtnToggle(self,val,*args):
        self.rigBtnVal = val
        print self.rigBtnVal
        print "Funct Called"
    #Method called when the time of day is selected by the user
    def dayBtnToggle(self,val,*args):
        self.dayBtnVal = val
        print self.dayBtnVal
        print "Funct Called"
    
	
#Create UI
win = OptionsWindow()
win.create()
