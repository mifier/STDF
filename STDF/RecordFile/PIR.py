from STDF.RecordFile.Record import RecordBase
# class PIR
class PIR(RecordBase):
    """Function:
    Acts as a marker to indicate where testing of a particular part begins for each part
    tested by the test program. The PIR and the Part Results Record (PRR) bracket all the
    stored information pertaining to one tested part.
"""

    type='PIR'
    verson = 'V4'
    fields={
        'record_length'     : { 'id' :  0, 'Type' :  'U*2',                   'std_name':'REC_LEN' , 'Text' : 'Bytes of data following header ', 'Missing' : None},
        'record_type'       : { 'id' :  1, 'Type' :  'U*1',  'Value' :     5, 'std_name':'REC_TYP' , 'Text' : 'Record type                    ', 'Missing' : None},
        'record_subtype'    : { 'id' :  2, 'Type' :  'U*1',  'Value' :    10, 'std_name':'REC_SUB' , 'Text' : 'Record sub-type                ', 'Missing' : None},
        'head_number'       : { 'id' :  3, 'Type' : 'U*1',                    'std_name':'HEAD_NUM', 'Text' : 'Test head number  ', 'Missing' :    1},
        'site_number'       : { 'id' :  4, 'Type' : 'U*1',                    'std_name':'SITE_NUM', 'Text' : 'Test site number  ', 'Missing' :    1}
        
    }

    
    def __init__(self): 
        super().__init__()
