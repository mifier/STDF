from STDF.RecordFile.Record import RecordBase
# class PCR
class PCR(RecordBase):
    """Function:
    Contains the part count totals for one or all test sites. Each data stream must have at
    least one PCR to show the part count."""
    type='PCR'
    verson = 'V4'
    fields={
        'record_length'       : { 'id' :  0, 'Type' :  'U*2',                    'std_name':'REC_LEN' , 'Text' : 'Bytes of data following header ', 'Missing' : None},
        'record_type'         : { 'id' :  1, 'Type' :  'U*1',  'Value' :     1,  'std_name':'REC_TYP' , 'Text' : 'Record type                    ', 'Missing' : None},
        'record_subtype'      : { 'id' :  2, 'Type' :  'U*1',  'Value' :    30,  'std_name':'REC_SUB' , 'Text' : 'Record sub-type                ', 'Missing' : None},
        'head_number'         : { 'id' :  3, 'Type' : 'U*1',                     'std_name':'HEAD_NUM', 'Text' : 'Test head number                      ', 'Missing' :           0},
        'site_number'         : { 'id' :  4, 'Type' : 'U*1',                     'std_name':'SITE_NUM', 'Text' : 'Test site number                      ', 'Missing' :           0},
        'count_partstested'   : { 'id' :  5, 'Type' : 'U*4',                     'std_name':'PART_CNT', 'Text' : 'Number of parts tested                ', 'Missing' :           0},
        'count_partsretested' : { 'id' :  6, 'Type' : 'U*4',                     'std_name':'RTST_CNT', 'Text' : 'Number of parts retested              ', 'Missing' : 4294967295},
        'count_aborts'        : { 'id' :  7, 'Type' : 'U*4',                     'std_name':'ABRT_CNT', 'Text' : 'Number of aborts during testing       ', 'Missing' : 4294967295},
        'count_good'          : { 'id' :  8, 'Type' : 'U*4',                     'std_name':'GOOD_CNT', 'Text' : 'Number of good (passed) parts tested  ', 'Missing' : 4294967295},
        'count_functional'    : { 'id' :  9, 'Type' : 'U*4',                     'std_name':'FUNC_CNT', 'Text' : 'Number of functional parts tested     ', 'Missing' : 4294967295}

    }

  
  
      
  
  
        
    def __init__(self): 
        super().__init__()

