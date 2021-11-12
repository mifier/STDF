from STDF.RecordFile.Record import RecordBase
# class EPS
class EPS(RecordBase):
    """Function:
    Marks the end of the current program section (or sequencer) in the job plan."""
    type='EPS'
    verson = 'V4'
    fields ={     
        'record_length'  : {'id' :  0 ,'Type' :  'U*2' ,                   'std_name': 'REC_LEN'  , 'Text' : 'Bytes of data following header      '  , 'Missing' :    0},
        'record_type'    : {'id' :  1 ,'Type' :  'U*1' ,  'Value' :    20, 'std_name': 'REC_TYP'  , 'Text' : 'Record type                         '  , 'Missing' : None},
        'record_subtype' : {'id' :  2 ,'Type' :  'U*1' ,  'Value' :    20, 'std_name': 'REC_SUB'  , 'Text' : 'Record sub-type                     '  , 'Missing' : None}
        }

    
    

    def __init__(self): 
        super().__init__()
