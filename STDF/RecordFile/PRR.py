from STDF.RecordFile.Record import RecordBase
# class PRR
class PRR(RecordBase):

    """Function:
    Contains the result information relating to each part tested by the test program. The
    PRR and the Part Information Record (PIR) bracket all the stored information
    pertaining to one tested part.
    """
    type='PRR'
    verson = 'V4'
    fields={ 
        'record_length'         : { 'id' :  0,'Type' :  'U*2',                   'std_name':'REC_LEN' , 'Text' : 'Bytes of data following header ', 'Missing' : None},
        'record_type'           : { 'id' :  1,'Type' :  'U*1',  'Value' :     5, 'std_name':'REC_TYP' , 'Text' : 'Record type                    ', 'Missing' : None},
        'record_subtype'        : { 'id' :  2,'Type' :  'U*1',  'Value' :    20, 'std_name':'REC_SUB' , 'Text' : 'Record sub-type                ', 'Missing' : None},
        'head_number'           : { 'id' :  3,'Type' : 'U*1',                    'std_name':'HEAD_NUM', 'Text' : 'Test head number                      ', 'Missing' :                                        1},
        'site_number'           : { 'id' :  4,'Type' : 'U*1',                    'std_name':'SITE_NUM', 'Text' : 'Test site number                      ', 'Missing' :                                        1},
        'part_flag'             : { 'id' :  5,'Type' : 'B*1',                    'std_name':'PART_FLG', 'Text' : 'Part information flag                 ', 'Missing' : ['0', '0', '0', '1', '0', '0', '0', '0']},
        'number_tests'          : { 'id' :  6,'Type' : 'U*2',                    'std_name':'NUM_TEST', 'Text' : 'Number of tests executed              ', 'Missing' :                                        0},
        'hardwarebin_number'    : { 'id' :  7,'Type' : 'U*2',                    'std_name':'HARD_BIN', 'Text' : 'Hardware bin number                   ', 'Missing' :                                        0},
        'softwarebin_number'    : { 'id' :  8,'Type' : 'U*2',                    'std_name':'SOFT_BIN', 'Text' : 'Software bin number                   ', 'Missing' :                                    65535},
        'X_coordinate'          : { 'id' :  9,'Type' : 'I*2',                    'std_name':'X_COORD' , 'Text' : '(Wafer) X coordinate                  ', 'Missing' :                                   -32768},
        'Y_coordinate'          : { 'id' : 10,'Type' : 'I*2',                    'std_name':'Y_COORD' , 'Text' : '(Wafer) Y coordinate                  ', 'Missing' :                                   -32768},
        'test_time'             : { 'id' : 11,'Type' : 'U*4',                    'std_name':'TEST_T'  , 'Text' : 'Elapsed test time in milliseconds     ', 'Missing' :                                        0},
        'Part_identification'   : { 'id' : 12,'Type' : 'C*n',                    'std_name':'PART_ID' , 'Text' : 'Part identification                   ', 'Missing' :                                       ''},
        'Part_description '     : { 'id' : 13,'Type' : 'C*n',                    'std_name':'PART_TXT', 'Text' : 'Part description text                 ', 'Missing' :                                       ''},
       'Part_repair_information': { 'id' : 14,'Type' : 'B*n',                    'std_name':'PART_FIX', 'Text' : 'Part repair information               ', 'Missing' :                                       []}
     
    } 
 
 
 
 
 
    
    def __init__(self): 
        super().__init__()
