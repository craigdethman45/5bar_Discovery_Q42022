# Created on: 28.09.2021
# Author: JH

from PyTrinamic.features.Feature import FeatureProvider
from PyTrinamic.features.SRamp import SRamp

class SRampModule(SRamp, FeatureProvider):
    "S-Ramp feature implementation for modules"

    class __GROUPING(SRamp,FeatureProvider):     
        def __init__(self, parent):
            self.parent = parent
                
        def get_ramp_type(self):
            """
            Gets if Ramp that is used for this axis.
            This value is stored in the  RampType axis parameter.

            Returns: ramp type 
            """
            return self.parent.get_axis_parameter(self.parent.APs.RampType)
        def set_ramp_type(self, ramp_type):
            """
            Sets if Ramp that is used for this axis.
            This value is stored as RampType axis parameter.

            Parameters:
            ramp_type: ramp type value 
            """
            self.parent.set_axis_parameter(self.parent.APs.RampType, ramp_type)
        def get_bow_1(self):
            """
            Gets the bow 1 value for the S-Ramp of this axis.
            This value is stored as Bow1 axis parameter.

            Returns: Bow 1 value 
            """
            return self.parent.get_axis_parameter(self.parent.APs.Bow1)
        def set_bow_1(self, pps):
            """
            Sets the bow 1 value for the S-Ramp of this axis.
            This value is stored as Bow1 axis parameter.

            Parameters:
            pps: Bow 1 value
            """
            self.parent.set_axis_parameter(self.parent.APs.Bow1,pps)
        def get_bow_2(self):
            """
            Gets the bow 1 value for the S-Ramp of this axis.
            This value is stored as Bow1 axis parameter.

            Returns: Bow 1 value 
            """
            return self.parent.get_axis_parameter(self.parent.APs.Bow2)
        def set_bow_2(self, pps):
            """
            Sets the bow 2 value for the S-Ramp of this axis.
            This value is stored as Bow2 axis parameter.

            Parameters:
            pps: Bow 2 value
            """
            self.parent.set_axis_parameter(self.parent.APs.Bow2,pps)
        def get_bow_3(self):
            """
            Gets the bow 3 value for the S-Ramp of this axis.
            This value is stored as Bow3 axis parameter.

            Returns: Bow 3 value 
            """
            return self.parent.get_axis_parameter(self.parent.APs.Bow3)
        def set_bow_3(self, pps):
            """
            Sets the bow 3 value for the S-Ramp of this axis.
            This value is stored as Bow3 axis parameter.

            Parameters:
            pps: Bow 3 value
            """
            self.parent.set_axis_parameter(self.parent.APs.Bow3,pps)
        def get_bow_4(self):
            """
            Gets the bow 4 value for the S-Ramp of this axis.
            This value is stored as Bow4 axis parameter.

            Returns: Bow 4 value 
            """
            return self.parent.get_axis_parameter(self.parent.APs.Bow4)
        def set_bow_4(self, pps):
            """
            Sets the bow 4 value for the S-Ramp of this axis.
            This value is stored as Bow4 axis parameter.
    
            Parameters:
            pps: Bow 4 value
            """
            self.parent.set_axis_parameter(self.parent.APs.Bow4,pps)

        # Properties
        ramp_type = property(get_ramp_type, set_ramp_type)
        bow_1 = property(get_bow_1, set_bow_1)
        bow_2 = property(get_bow_2, set_bow_2)
        bow_3 = property(get_bow_3, set_bow_3)
        bow_4 = property(get_bow_4, set_bow_4)

    # Feature initialization
    def __init__(self):
        self.SRamp = self.__GROUPING(self)