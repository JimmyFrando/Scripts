"""
Author: Jimmy Frando
Date: 9/22/2015
Title: bindRigsScript

Details: This script allows the maya user to select two joints. First, the root to be the driver and second,
the root to be the driven. These hierarchies should be the same. Simply press the Bind Skeletons button
to bind the two hierarchies together. You can unbind them as well but you must reselect the same joints in 
the same order as you did before. 

Running The Script: To run the script, you should copy this py file into your maya/scripts folder. 
Then, in maya, type: import bindRigsScript
Then, to bring up the GUI window, type: bindRigsScript.draw()

"""

import pymel.core as pmc

class Skeleton_Binder(object):
    WINDOW_NAME = 'SkeletonBinderPymel'
    WINDOW_TITLE = 'Skeleton Binder Pymel'

    def __init__(self):
        self._win = None

    def GUI(self):
        #Create GUI with window and 3 buttons
        self._win = pmc.window(self.WINDOW_NAME, title = self.WINDOW_TITLE)
        pmc.columnLayout(adjustableColumn = True)
        pmc.button(label = "Bind Skeletons", c = pmc.Callback(self._callbackBind))
        pmc.button(label = "Unbind Skeletons", c = pmc.Callback(self._callbackUnbind))
        pmc.button(label = "Cancel", c = pmc.Callback(pmc.deleteUI, self._win))
        self._win.show()

    def _callbackBind(self):

        #assign selections to joint list
        joints = pmc.ls(selection = True, type = 'joint')

        if len(joints) < 2:
            print "ERROR: Need to select 2 joints."
            return


        if len(joints) > 2:
            print "ERROR: Need to select 2 joints."
            return

        #Assign first selected joint and second selected joint
        driverRootJoint = joints[0]
        drivenRootJoint = joints[1]

        #Call bind method
        self.doBind(driverRootJoint, drivenRootJoint)

    def _callbackUnbind(self):

        joints = pmc.ls(selection = True, type = 'joint')

        if len(joints) < 2:
            print "ERROR: Need to select 2 joints."
            return


        if len(joints) > 2:
            print "ERROR: Need to select 2 joints."
            return

        #Assign first selected joint and second selected joint
        driverRootJoint = joints[0]
        drivenRootJoint = joints[1]

        #Call Unbind method
        self.doUnbind(driverRootJoint, drivenRootJoint)

    def doBind(self, driverRootJoint, drivenRootJoint):
        
        #Clear selection, select the first root joint the user selected, select all joint hierarchy
        pmc.select(clear = True)
        pmc.select(driverRootJoint)
        pmc.select(pmc.ls(dag = 1, sl = 1, type = 'joint'))
        driverJointsList = pmc.ls(selection = True)

        #Clear selection, select the second root joint the user selected, select all joint hierarchy
        pmc.select(clear = True)
        pmc.select(drivenRootJoint)
        pmc.select(pmc.ls(dag = 1, sl = 1, type = 'joint'))
        drivenJointsList = pmc.ls(selection = True)
        
        #Loop through both hierarchies and point/orient constrain them to each other 
        for jnt1,jnt2 in zip(driverJointsList,drivenJointsList):
            pmc.orientConstraint(jnt1, jnt2, mo = False)
            pmc.pointConstraint(jnt1, jnt2, mo = False)


    def doUnbind(self, driverRootJoint, drivenRootJoint):
        
        #Clear selection, select the first root joint the user selected, select all joint hierarchy
        pmc.select(clear = True)
        pmc.select(driverRootJoint)
        pmc.select(pmc.ls(dag = 1, sl = 1, type = 'joint'))
        driverJointsList = pmc.ls(selection = True)

        #Clear selection, select the second root joint the user selected, select all joint hierarchy
        pmc.select(clear = True)
        pmc.select(drivenRootJoint)
        pmc.select(pmc.ls(dag = 1, sl = 1, type = 'joint'))
        drivenJointsList = pmc.ls(selection = True)

        for jnt in driverJointsList:
            pmc.delete(jnt, cn = True)
            

def draw():
    global MAIN_WINDOW
    MAIN_WINDOW = Skeleton_Binder()
    MAIN_WINDOW.GUI()

