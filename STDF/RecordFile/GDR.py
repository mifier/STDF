from STDF.RecordFile.Record import RecordBase

# class GDR
class GDR(RecordBase):
    """Function:
    Contains information that does not conform to any other record type defined by the
    STDF specification. Such records are intended to be written under the control of job
    plans executing on the tester. This data may be used for any purpose that the user
    desires."""

    type='GDR'
    verson = 'V4'

    fields ={     
        'record_length'  : {'id' :  0 ,'Type' :  'U*2' ,                    'std_name': 'REC_LEN'  , 'Text' : 'Bytes of data following header      '  , 'Missing' :    0},
        'record_type'    : {'id' :  1 ,'Type' :  'U*1' ,  'Value' :    50,  'std_name': 'REC_TYP'  , 'Text' : 'Record type                         '  , 'Missing' : None},
        'record_subtype' : {'id' :  2 ,'Type' :  'U*1' ,  'Value' :    10,  'std_name': 'REC_SUB'  , 'Text' : 'Record sub-type                     '  , 'Missing' : None},
        'count_fields'   : {'id' :  3 ,'Type' :  'U*2' ,                    'std_name': 'FLD_CNT' ,  'Text' : 'Count of data fields in record        ', 'Missing' :    0},
        'repeat_data'    : {'id' :  4 ,'Type' : 'xV*n' , 'Length':'count_fields','std_name': 'GEN_DATA' , 'Text' : 'Data type code and data for one field ', 'Missing' :   []}
    }      

    
    def __init__(self): 
        super().__init__()
