from STDF.RecordFile.Record import RecordBase
# class MPR
class MPR(RecordBase):
    """Function:
    Contains the results of a single execution of a parametric test in the test program
    where that test returns multiple values. The first occurrence of this record also
    establishes the default values for all semi-static information about the test, such as
    limits, units, and scaling. The MPR is related to the Test Synopsis Record (TSR) by test
    number, head number, and site number.
"""
    type='MPR'
    verson = 'V4'
    fields={
        'record_length'    : { 'id' :  0, 'Type' :  'U*2',                            'std_name': 'REC_LEN'  , 'Text' : 'Bytes of data following header ', 'Missing' : None},
        'record_type'      : { 'id' :  1, 'Type' :  'U*1', 'Value' :    15,           'std_name': 'REC_TYP'  , 'Text' : 'Record type                    ', 'Missing' : None},
        'record_subtype'   : { 'id' :  2, 'Type' :  'U*1', 'Value' :    15,           'std_name': 'REC_SUB'  , 'Text' : 'Record sub-type                ', 'Missing' : None},
        'test_number'      : { 'id' :  3, 'Type' : 'U*4',                             'std_name': 'TEST_NUM' , 'Text' : 'Test number                           ', 'Missing' :                                     None},
        'head_number'      : { 'id' :  4, 'Type' : 'U*1',                             'std_name': 'HEAD_NUM' , 'Text' : 'Test head number                      ', 'Missing' :                                        1},
        'site_number'      : { 'id' :  5, 'Type' : 'U*1',                             'std_name': 'SITE_NUM' , 'Text' : 'Test site number                      ', 'Missing' :                                        1},
        'test_flags'       : { 'id' :  6, 'Type' : 'B*1',                             'std_name': 'TEST_FLG' , 'Text' : 'Test flags (fail, alarm, etc.)        ', 'Missing' :                                  ['0']*8},
        'parametric_flags' : { 'id' :  7, 'Type' : 'B*1',                             'std_name': 'PARM_FLG' , 'Text' : 'Parametric test flags (drift, etc.)   ', 'Missing' : ['1', '1', '0', '0', '0', '0', '0', '0']}, # 0xC0
        'count_indexes'    : { 'id' :  8, 'Type' : 'U*2',                             'std_name': 'RTN_ICNT' , 'Text' : 'Count (j) of PMR indexes              ', 'Missing' :                                        0},
        'Count_results'    : { 'id' :  9, 'Type' : 'U*2',                             'std_name': 'RSLT_CNT' , 'Text' : 'Count (k) of returned results         ', 'Missing' :                                        0},
        'returned_states'  : { 'id' : 10, 'Type' : 'xN*1', 'Length':'count_indexes',  'std_name': 'RTN_STAT' , 'Text' : 'Array of j returned states            ', 'Missing' :                                       []}, # RTN_ICNT = 0
        'returned_results' : { 'id' : 11, 'Type' : 'xR*4', 'Length':'Count_results',  'std_name': 'RTN_RSLT' , 'Text' : 'Array of k returned results           ', 'Missing' :                                       []}, # RSLT_CNT = 0
        'descriptive_text' : { 'id' : 12, 'Type' : 'C*n',                             'std_name': 'TEST_TXT' , 'Text' : 'Descriptive text or label             ', 'Missing' :                                       ''},
        'Name_alarm'       : { 'id' : 13, 'Type' : 'C*n',                             'std_name': 'ALARM_ID' , 'Text' : 'Name of alarm                         ', 'Missing' :                                       ''},
        'optional_flag'    : { 'id' : 14, 'Type' : 'B*1',                             'std_name': 'OPT_FLAG' , 'Text' : 'Optional data flag See note           ', 'Missing' : ['0', '0', '0', '0', '0', '0', '1', '0']}, # 0x02
        'result_scaling'   : { 'id' : 15, 'Type' : 'I*1',                             'std_name': 'RES_SCAL' , 'Text' : 'Test result scaling exponent          ', 'Missing' :                                        0}, # OPT_FLAG bit 0 = 1
        'lowlimit_scaling' : { 'id' : 16, 'Type' : 'I*1',                             'std_name': 'LLM_SCAL' , 'Text' : 'Test low limit scaling exponent       ', 'Missing' :                                        0}, # OPT_FLAG bit 4 or 6 = 1
        'highlimit_scaling': { 'id' : 17, 'Type' : 'I*1',                             'std_name': 'HLM_SCAL' , 'Text' : 'Test high limit scaling exponent      ', 'Missing' :                                        0}, # OPT_FLAG bit 5 or 7 = 1
        'lowlimit_value'   : { 'id' : 18, 'Type' : 'R*4',                             'std_name': 'LO_LIMIT' , 'Text' : 'Test low limit value                  ', 'Missing' :                                      0.0}, # OPT_FLAG bit 4 or 6 = 1
        'highlimit_value'  : { 'id' : 19, 'Type' : 'R*4',                             'std_name': 'HI_LIMIT' , 'Text' : 'Test high limit value                 ', 'Missing' :                                      0.0}, # OPT_FLAG bit 5 or 7 = 1
        'starting_input'   : { 'id' : 20, 'Type' : 'R*4',                             'std_name': 'START_IN' , 'Text' : 'Starting input value [condition]      ', 'Missing' :                                      0.0}, # OPT_FLAG bit 1 = 1
        'increment_input'  : { 'id' : 21, 'Type' : 'R*4',                             'std_name': 'INCR_IN'  , 'Text' : 'Increment of input condition          ', 'Missing' :                                       -1}, # OPT_FLAG bit 1 = 1
        'PMR_indexes'      : { 'id' : 22, 'Type' : 'xU*2', 'Length':'count_indexes',  'std_name': 'RTN_INDX' , 'Text' : 'Array of j PMR indexes                ', 'Missing' :                                       []}, # RTN_ICNT = 0
        'units_results'    : { 'id' : 23, 'Type' : 'C*n',                             'std_name': 'UNITS'    , 'Text' : 'Units of returned results             ', 'Missing' :                                       ''},
        'input_units'      : { 'id' : 24, 'Type' : 'C*n',                             'std_name': 'UNITS_IN' , 'Text' : 'Input condition units                 ', 'Missing' :                                       ''},
        'C_resultformat'   : { 'id' : 25, 'Type' : 'C*n',                             'std_name': 'C_RESFMT' , 'Text' : 'ANSI C result format string           ', 'Missing' :                                       ''},
        'C_lowlimitformat' : { 'id' : 26, 'Type' : 'C*n',                             'std_name': 'C_LLMFMT' , 'Text' : 'ANSI C low limit format string        ', 'Missing' :                                       ''},
        'C_highlimitformat': { 'id' : 27, 'Type' : 'C*n',                             'std_name': 'C_HLMFMT' , 'Text' : 'ANSI C high limit format string       ', 'Missing' :                                       ''},
        'low_specification': { 'id' : 28, 'Type' : 'R*4',                             'std_name': 'LO_SPEC'  , 'Text' : 'Low specification limit value         ', 'Missing' :                                      0.0}, # OPT_FLAG bit 2 = 1
       'high_specification': { 'id' : 29, 'Type' : 'R*4',                             'std_name': 'HI_SPEC'  , 'Text' : 'High specification limit value        ', 'Missing' :                                      0.0}  # OPT_FLAG bit 3 = 1
    
    }


    



    def __init__(self): 
        super().__init__()
