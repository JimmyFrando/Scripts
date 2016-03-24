"""
Author: Jimmy Frando
Name: stretchyIK
Class: Advanced Rigging
Date: 10/3/2015
This script converts a regular IK joint chain system in Maya into a stretchy one. The animator or user is given the ability to stretch the IK system and exaggerate them to how they see fit. 
To use the script, simply select the ikHandle you wish to make stretchy and click the Stretch It! button. Be sure to also have a control in place for the ikHandle 
To run this script type the following into the Maya script editor (This assumes this file is located in your /maya/scripts folder): 

import stretchyIK

stretchyIK.draw()

"""


import pymel.core as pmc

class Stretchy_IK(object):
    WINDOW_NAME = 'StretchyIKPymel'
    WINDOW_TITLE = 'Stretchy IK Pymel'

    def __init__(self):
        self._win = None

    def GUI(self):
        # Create GUI with window and 3 buttons
        self._win = pmc.window(self.WINDOW_NAME, title = self.WINDOW_TITLE)
        pmc.columnLayout(adjustableColumn = True)
        pmc.button(label = "Stretch It!", c = pmc.Callback(self._callbackBind))
        pmc.button(label = "Cancel", c = pmc.Callback(pmc.deleteUI, self._win))
        self._win.show()


    def basicStretchyIK(self, ikHandle):
        print "basic called"

        # Find the joints connected to the IK Handle
        incomingJnt = pmc.listConnections(ikHandle, destination = False, source = True, type = 'joint')
        effectorNode = pmc.listConnections(ikHandle, destination = False, source = True, type = 'ikEffector')
        outgoingJnt = pmc.listConnections(effectorNode, destination = False, source = True, type = 'joint')

        # Create two locators.
        locatorFirst = pmc.spaceLocator()
        locatorSecond = pmc.spaceLocator()


        # Point Constrain one locator to the first joint,
        pmc.pointConstraint(incomingJnt, locatorFirst, maintainOffset = False)
		
        # Constrain the second locator to the ikHandle. MaintainOffset should be set to False for both
        ikCtrl = pmc.listRelatives(ikHandle, parent = True)
        pmc.pointConstraint(ikCtrl, locatorSecond, maintainOffset = False)

        # Create a distanceBetween node, and connect the locators' worldPosition into point1 and point2
        distance = pmc.shadingNode('distanceBetween', asUtility = True)
        pmc.connectAttr(locatorFirst.worldPosition, distance.point1)
        pmc.connectAttr(locatorSecond.worldPosition, distance.point2)

        # Create a normalize multiplyDivide node that divides the current distance, by the max distance
        divNode = pmc.shadingNode('multiplyDivide', asUtility = True)
        pmc.setAttr(divNode.operation, 2)
		
        # The max distance can be calculated by adding up the translateX values in the joint chain (except the first joint)
        jointList = pmc.listRelatives(incomingJnt, allDescendents = True, type = 'joint')
        jointList.reverse()
        ikJointsList = self.newList(jointList, outgoingJnt)

        maxDistance = 0
        for x in ikJointsList:
            maxDistance += abs(pmc.getAttr(x.translateX))

        pmc.connectAttr(distance.distance, divNode.input1X)
        pmc.setAttr(divNode.input2X, maxDistance)

        # Create and connect clamp node to maintain the current length and also cap the maximum mount the joints can stretch
        clamp = pmc.shadingNode('clamp', asUtility = True)
        pmc.connectAttr(divNode.outputX, clamp.inputR)
        pmc.setAttr(clamp.minR, 1.0)
        pmc.setAttr(clamp.maxR, 2.0)

		# For each child joints, create multiplyDivide nodes to multiply their current length by scale value outputted by the clamp node
        multNodeList = []
        for x in ikJointsList:
            multNodeList.append(pmc.shadingNode('multiplyDivide', asUtility = True))

		# Connect the multiplyDivide nodes to the skeleton
        for x in multNodeList:
            pmc.connectAttr(clamp.outputR, x.input1X)

		# Get the translate values of each joint and set each multiply node's 2X to that value
        for jnt,node in zip(ikJointsList, multNodeList):
            val = pmc.getAttr(jnt.translateX)
            pmc.setAttr(node.input2X, val)
		
		# Connect outputX of each multiply node to the translateX of each joint
        for jnt,node in zip(ikJointsList, multNodeList):
            pmc.connectAttr(node.outputX, jnt.translateX)

    def newList(self, jointsList, outgoingJnt):

		# Get the list of joints that are only involved with the IKHandle selected
        ikJointsList = []
        for jnt in jointsList:
            print jnt
            if jnt != outgoingJnt[0]:
                ikJointsList.append(jnt)
            else:
                ikJointsList.append(jnt)
                return ikJointsList

    def _callbackBind(self):
        print "callbackBind Initiated"

        # Assign selections to ikHandle variable
        ikHandle = pmc.ls(selection = True, type = 'ikHandle')

        if len(ikHandle) == 0:
            print "ERROR: Need to select an IKHandle"
            return

        # Call basicStretchyIK method
        self.basicStretchyIK(ikHandle)

def draw():

	# Create GUI for user 
    global MAIN_WINDOW
    MAIN_WINDOW = Stretchy_IK()
    MAIN_WINDOW.GUI()

