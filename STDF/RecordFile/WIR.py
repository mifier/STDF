from STDF.RecordFile.Record import RecordBase
# class WIR
class WIR(RecordBase):

    """Function:
    Acts mainly as a marker to indicate where testing of a particular wafer begins for each
    wafer tested by the job plan. The WIR and the Wafer Results Record (WRR) bracket all
    the stored information pertaining to one tested wafer. This record is used only when
    testing at wafer probe. A WIR/WRR pair will have the same HEAD_NUM and SITE_GRP values."""
    type='WIR'
    verson = 'V4'
    fields={
        'record_length'     : {'id' :  0,'Type' :  'U*2',                   'std_name': 'REC_LEN'  ,'Text' : 'Bytes of data following header ', 'Missing' : None},
        'record_type'       : {'id' :  1,'Type' :  'U*1',  'Value' :     2, 'std_name': 'REC_TYP'  ,'Text' : 'Record type                    ', 'Missing' : None},
        'record_subtype'    : {'id' :  2,'Type' :  'U*1',  'Value' :    10, 'std_name': 'REC_SUB'  ,'Text' : 'Record sub-type                ', 'Missing' : None},
        'head_number'       : {'id' :  3,'Type' : 'U*1',                    'std_name': 'HEAD_NUM' ,'Text' : 'Test head number                ', 'Missing' : 1   },
        'site_group_number' : {'id' :  4,'Type' : 'U*1',                    'std_name': 'SITE_GRP' ,'Text' : 'Site group number               ', 'Missing' : 255 },
        'start_time'        : {'id' :  5,'Type' : 'U*4',                    'std_name': 'START_T'  ,'Text' : 'Date and time first part tested ', 'Missing' : 0   },
        'wafer_ID'          : {'id' :  6,'Type' : 'C*n',                    'std_name': 'WAFER_ID' ,'Text' : 'Wafer ID                        ', 'Missing' : ''  }        
        }

    
    
    def __init__(self): 
        super().__init__()
