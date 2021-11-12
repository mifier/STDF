from STDF.RecordFile.Record import RecordBase
# class WCR
class WCR(RecordBase):
    """Function:
    Contains the configuration information for the wafers tested by the job plan. The
    WCR provides the dimensions and orientation information for all wafers and dice
    in the lot. This record is used only when testing at wafer probe time."""
    type='WCR'
    verson = 'V4'
    fields={
        'record_length'      : {'id' :  0,'Type' :  'U*2',                    'std_name':  'REC_LEN' , 'Text' : 'Bytes of data following header ', 'Missing' : None},
        'record_type'        : {'id' :  1,'Type' :  'U*1',  'Value' :     2,  'std_name':  'REC_TYP' , 'Text' : 'Record type                    ', 'Missing' : None},
        'record_subtype'     : {'id' :  2,'Type' :  'U*1',  'Value' :    30,  'std_name':  'REC_SUB' , 'Text' : 'Record sub-type                ', 'Missing' : None},
        'diameter_wafe'      : {'id' :  3,'Type' : 'R*4',                     'std_name':  'WAFR_SIZ', 'Text' : 'Diameter of wafer in WF_UNITS         ', 'Missing' : 0.0   },
        'height_die'         : {'id' :  4,'Type' : 'R*4',                     'std_name':  'DIE_HT'  , 'Text' : 'Height of die in WF_UNITS             ', 'Missing' : 0.0   },
        'width_die'          : {'id' :  5,'Type' : 'R*4',                     'std_name':  'DIE_WID' , 'Text' : 'Width of die in WF_UNITS              ', 'Missing' : 0.0   },
        'units_wafer'        : {'id' :  6,'Type' : 'U*1',                     'std_name':  'WF_UNITS', 'Text' : 'Units for wafer and die dimensions    ', 'Missing' : 0     }, # 0=?/1=Inch/2=cm/3=mm/4=mils
        'orientation_wafer'  : {'id' :  7,'Type' : 'C*1',                     'std_name':  'WF_FLAT' , 'Text' : 'Orientation of wafer flat (U/D/L/R)   ', 'Missing' : ' '   },
        'X_center'           : {'id' :  8,'Type' : 'I*2',                     'std_name':  'CENTER_X', 'Text' : 'X coordinate of center die on wafer   ', 'Missing' : -32768},
        'Y_center'           : {'id' :  9,'Type' : 'I*2',                     'std_name':  'CENTER_Y', 'Text' : 'Y coordinate of center die on wafer   ', 'Missing' : -32768},
        'positive_X'         : {'id' : 10,'Type' : 'C*1',                     'std_name':  'POS_X'   , 'Text' : 'Positive X direction of wafer (L/R)   ', 'Missing' : ' '   },
        'positive_Y'         : {'id' : 11,'Type' : 'C*1',                     'std_name':  'POS_Y'   , 'Text' : 'Positive Y direction of wafer (U/D)   ', 'Missing' : ' '   }    
    } 

    
    
    def __init__(self): 
        super().__init__()
