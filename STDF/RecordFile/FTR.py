from STDF.RecordFile.Record import RecordBase
# class FTR
class FTR(RecordBase):
    """Function:
    Contains the results of the single execution of a functional test in the test program. The
    first occurrence of this record also establishes the default values for all semi-static
    information about the test. The FTR is related to the Test Synopsis Record (TSR) by test
    number, head number, and site number."""
    type='FTR'
    verson = 'V4'
    fields ={           
        'record_length'          : { 'id' :  0, 'Type' :  'U*2' ,                                            'std_name': 'REC_LEN'  , 'Text' : 'Bytes of data following header      '  , 'Missing' :    0},
        'record_type'            : { 'id' :  1, 'Type' :  'U*1' ,  'Value' :    15,                          'std_name': 'REC_TYP'  , 'Text' : 'Record type                         '  , 'Missing' : None},
        'record_subtype'         : { 'id' :  2, 'Type' :  'U*1' ,  'Value' :    20,                          'std_name': 'REC_SUB'  , 'Text' : 'Record sub-type                     '  , 'Missing' : None},       
        'test_number'            : { 'id' :  3, 'Type' : 'U*4',                                              'std_name': 'TEST_NUM' , 'Text' : 'Test number                           ', 'Missing' :    None},# Obligatory!
        'head_number'            : { 'id' :  4, 'Type' : 'U*1',                                              'std_name': 'HEAD_NUM' , 'Text' : 'Test head number                      ', 'Missing' :       1},#
        'site_number'            : { 'id' :  5, 'Type' : 'U*1',                                              'std_name': 'SITE_NUM' , 'Text' : 'Test site number                      ', 'Missing' :       1},#
        'test_flag'              : { 'id' :  6, 'Type' : 'B*1',                                              'std_name': 'TEST_FLG' , 'Text' : 'Test flags (fail, alarm, etc.)        ', 'Missing' : ['0']*8},#
        'optional_flag'          : { 'id' :  7, 'Type' : 'B*1',                                              'std_name': 'OPT_FLAG' , 'Text' : 'Optional data flag                    ', 'Missing' : ['1']*8},#
        'cycle_count'            : { 'id' :  8, 'Type' : 'U*4',                                              'std_name': 'CYCL_CNT' , 'Text' : 'Cycle count of vector                 ', 'Missing' :       0},# OPT_FLAG bit0 = 1
        'relative_vectoraddress' : { 'id' :  9, 'Type' : 'U*4',                                              'std_name': 'REL_VADR' , 'Text' : 'Relative vector address               ', 'Missing' :       0},# OPT_FLAG bit1 = 1
        'repeat_count'           : { 'id' : 10, 'Type' : 'U*4',                                              'std_name': 'REPT_CNT' , 'Text' : 'Repeat count of vector                ', 'Missing' :       0},# OPT_FLAG bit2 = 1
        'Number_failures'        : { 'id' : 11, 'Type' : 'U*4',                                              'std_name': 'NUM_FAIL' , 'Text' : 'Number of pins with 1 or more failures', 'Missing' :       0},# OPT_FLAG bit3 = 1
        'X_failureaddress'       : { 'id' : 12, 'Type' : 'I*4',                                              'std_name': 'XFAIL_AD' , 'Text' : 'X logical device failure address      ', 'Missing' :       0},# OPT_FLAG bit4 = 1
        'Y_failureaddress'       : { 'id' : 13, 'Type' : 'I*4',                                              'std_name': 'YFAIL_AD' , 'Text' : 'Y logical device failure address      ', 'Missing' :       0},# OPT_FLAG bit4 = 1
        'vector_offest'          : { 'id' : 14, 'Type' : 'I*2',                                              'std_name': 'VECT_OFF' , 'Text' : 'Offset from vector of interest        ', 'Missing' :       0},# OPT_FLAG bit5 = 1
        'Count_returndata'       : { 'id' : 15, 'Type' : 'U*2',                                              'std_name': 'RTN_ICNT' , 'Text' : 'Count (j) of return data PMR indexes  ', 'Missing' :       0},#
        'Count_programmedstate'  : { 'id' : 16, 'Type' : 'U*2',                                              'std_name': 'PGM_ICNT' , 'Text' : 'Count (k) of programmed state indexes ', 'Missing' :       0},#
        'array_returndata'       : { 'id' : 17, 'Type' :'xU*2', 'Length':'Count_returndata',                 'std_name': 'RTN_INDX' , 'Text' : 'Array of j return data PMR indexes    ', 'Missing' :      []},# RTN_ICNT = 0
        'Count_returnstates'     : { 'id' : 18, 'Type' :'xN*1', 'Length':'Count_returndata',                 'std_name': 'RTN_STAT' , 'Text' : 'Array of j returned states            ', 'Missing' :      []},# RTN_ICNT = 0
        'Count_programmedindexes': { 'id' : 19, 'Type' :'xU*2', 'Length':'Count_programmedstate',            'std_name': 'PGM_INDX' , 'Text' : 'Array of k programmed state indexes   ', 'Missing' :      []},# PGM_ICNT = 0
        'Count_programmedstates' : { 'id' : 20, 'Type' :'xN*1', 'Length':'Count_programmedstate',            'std_name': 'PGM_STAT' , 'Text' : 'Array of k programmed states          ', 'Missing' :      []},# PGM_ICNT = 0
        'failing_pin'            : { 'id' : 21, 'Type' : 'D*n',                                              'std_name': 'FAIL_PIN' , 'Text' : 'Failing pin bitfield                  ', 'Missing' :      []},
        'vector_name'            : { 'id' : 22, 'Type' : 'C*n',                                              'std_name': 'VECT_NAM' , 'Text' : 'Vector module pattern name            ', 'Missing' :      ''},
        'Timeset_name'           : { 'id' : 23, 'Type' : 'C*n',                                              'std_name': 'TIME_SET' , 'Text' : 'Time set name                         ', 'Missing' :      ''},
        'Vector_OpCode'          : { 'id' : 24, 'Type' : 'C*n',                                              'std_name': 'OP_CODE'  , 'Text' : 'Vector Op Code                        ', 'Missing' :      ''},
        'descriptive_text'       : { 'id' : 25, 'Type' : 'C*n',                                              'std_name': 'TEST_TXT' , 'Text' : 'Descriptive text or label             ', 'Missing' :      ''},
        'alarm_name'             : { 'id' : 26, 'Type' : 'C*n',                                              'std_name': 'ALARM_ID' , 'Text' : 'Name of alarm                         ', 'Missing' :      ''},
        'programmed_information' : { 'id' : 27, 'Type' : 'C*n',                                              'std_name': 'PROG_TXT' , 'Text' : 'Additional programmed information     ', 'Missing' :      ''},
        'result_information'     : { 'id' : 28, 'Type' : 'C*n',                                              'std_name': 'RSLT_TXT' , 'Text' : 'Additional result information         ', 'Missing' :      ''},
        'pattern_number'         : { 'id' : 29, 'Type' : 'U*1',                                              'std_name': 'PATG_NUM' , 'Text' : 'Pattern generator number              ', 'Missing' :    0xFF},
        'comparators_map'        : { 'id' : 30, 'Type' : 'D*n',                                              'std_name': 'SPIN_MAP' , 'Text' : 'Bit map of enabled comparators        ', 'Missing' :      []}
        }      
          
       

    def __init__(self): 
        super().__init__()
        