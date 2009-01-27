#------------------------------------------------------------------------------
# Copyright (c) 2007, Riverbank Computing Limited
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# license.
#
# Author: Riverbank Computing Limited
#------------------------------------------------------------------------------

""" Defines the PyQt implementation of the editor used to wrap a non-Traits
based custom control.
"""

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from PyQt4 import QtGui

    
# FIXME: ToolkitEditorFactory is a proxy class defined here just for backward
# compatibility. The class has been moved to the 
# enthought.traits.ui.editors.custom_editor file.
from enthought.traits.ui.editors.custom_editor \
    import ToolkitEditorFactory
    
from editor \
    import Editor
    
from helper \
    import open_fbi

#-------------------------------------------------------------------------------
#  'CustomEditor' class:
#-------------------------------------------------------------------------------
                               
class CustomEditor ( Editor ):
    """ Wrapper for a custom editor control
    """
    #---------------------------------------------------------------------------
    #  Finishes initializing the editor by creating the underlying toolkit
    #  widget:
    #---------------------------------------------------------------------------
        
    def init ( self, parent ):
        """ Finishes initializing the editor by creating the underlying toolkit
            widget.
        """
        factory = self.factory.factory
        if factory is not None:
            try:
                self.control = factory( *(( parent, self ) + self.factory.args ) )
            except:
                open_fbi()
        if self.control is None:
            self.control = QtGui.QLabel(
                'An error occurred creating a custom editor.\n'
                'Please contact the developer.', parent)
            self.control.setStyleSheet("background-color: red; color: white")
        self.set_tooltip()
        
    #---------------------------------------------------------------------------
    #  Updates the editor when the object trait changes external to the editor:
    #---------------------------------------------------------------------------
        
    def update_editor ( self ):
        """ Updates the editor when the object trait changes externally to the 
            editor.
        """
        pass
