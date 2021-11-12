from STDF.RecordFile.Record import RecordBase
# class BPS
class BPS(RecordBase):
    """Function:
    Marks the beginning of a new program section (or sequencer) in the job plan.
    """
    type='BPS'
    verson = 'V4'

    fields ={     
        'record_length'  : {'id' :  0 ,'Type' :  'U*2' ,                   'std_name': 'REC_LEN'  , 'Text' : 'Bytes of data following header      '  , 'Missing' :    0},
        'record_type'    : {'id' :  1 ,'Type' :  'U*1' ,  'Value' :    20, 'std_name': 'REC_TYP'  , 'Text' : 'Record type                         '  , 'Missing' : None},
        'record_subtype' : {'id' :  2 ,'Type' :  'U*1' ,  'Value' :    10, 'std_name': 'REC_SUB'  , 'Text' : 'Record sub-type                     '  , 'Missing' : None},
        'sequencer_name' : {'id' :  3 ,'Type' :  'C*n',                    'std_name': 'SEQ_NAME' , 'Text' : 'Sequence name               ', 'Missing' :   ''}
        }
    
    def __init__(self): 
        super().__init__()
