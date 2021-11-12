from STDF.RecordFile.Record import RecordBase
# class FAR
class FAR(RecordBase):
    """Function:
    Contains the information necessary to determine how to decode the STDF data contained in the file.
    """
    type='FAR'
    verson = 'V4'
    fields ={     
        'record_length'  : {'id' :  0 ,'Type' :  'U*2' ,                   'std_name': 'REC_LEN'  , 'Text' : 'Bytes of data following header      '  , 'Missing' :    0},
        'record_type'    : {'id' :  1 ,'Type' :  'U*1' ,  'Value' :     0, 'std_name': 'REC_TYP'  , 'Text' : 'Record type                         '  , 'Missing' : None},
        'record_subtype' : {'id' :  2 ,'Type' :  'U*1' ,  'Value' :    10, 'std_name': 'REC_SUB'  , 'Text' : 'Record sub-type                     '  , 'Missing' : None},
        'cpu_type'       : {'id' :  3 ,'Type' :  'U*1' ,                   'std_name': 'CPU_TYPE' , 'Text' : 'CPU type that wrote this file       '  , 'Missing' : None},
        'stdf_version'   : {'id' :  4 ,'Type' :  'U*1' ,                   'std_name': 'STDF_VER' , 'Text' : 'STDF version number                 '  , 'Missing' : None}
    }

    def __init__(self): 
        super().__init__()



       


