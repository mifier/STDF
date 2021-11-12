from STDF.RecordFile.Record import RecordBase

# class PTR


class PTR(RecordBase):
    """Function:
    Contains the results of a single execution of a parametric test in the test program. The
    first occurrence of this record also establishes the default values for all semi-static
    information about the test, such as limits, units, and scaling. The PTR is related to the
    Test Synopsis Record (TSR) by test number, head number, and site number."""
    type='PTR'
    verson = 'V4'    
    fields={
    'record_length'      : { 'id' :  0, 'Type' :  'U*2',                    'std_name':'REC_LEN'  ,  'Text' : 'Bytes of data following header ', 'Missing' : None},
    'record_type'        : { 'id' :  1, 'Type' :  'U*1',  'Value' :    15,  'std_name':'REC_TYP'  ,  'Text' : 'Record type                    ', 'Missing' : None},
    'record_subtype'     : { 'id' :  2, 'Type' :  'U*1',  'Value' :    10,  'std_name':'REC_SUB'  ,  'Text' : 'Record sub-type                ', 'Missing' : None},
    'test_number'        : { 'id' :  3, 'Type' : 'U*4',                     'std_name':'TEST_NUM' ,  'Text' : 'Test number                           ','Missing' : None   },
    'head_number'        : { 'id' :  4, 'Type' : 'U*1',                     'std_name':'HEAD_NUM' ,  'Text' : 'Test head number                      ','Missing' : 1      },
    'site_number'        : { 'id' :  5, 'Type' : 'U*1',                     'std_name':'SITE_NUM' ,  'Text' : 'Test site number                      ','Missing' : 1      },
    'test_flag'          : { 'id' :  6, 'Type' : 'B*1',                     'std_name':'TEST_FLG' ,  'Text' : 'Test flags (fail, alarm, etc.)        ','Missing' : ['0']*8},
    'parametric_flags'   : { 'id' :  7, 'Type' : 'B*1',                     'std_name':'PARM_FLG' ,  'Text' : 'Parametric test flags (drift, etc.)   ','Missing' : ['0']*8},
    'test_result'        : { 'id' :  8, 'Type' : 'R*4',                     'std_name':'RESULT'   ,  'Text' : 'Test result                           ','Missing' : 0.0    },
    'description_text'   : { 'id' :  9, 'Type' : 'C*n',                     'std_name':'TEST_TXT' ,  'Text' : 'Test description text or label        ','Missing' : ''     },
    'name_alarm'         : { 'id' : 10, 'Type' : 'C*n',                     'std_name':'ALARM_ID' ,  'Text' : 'Name of alarm                         ','Missing' : ''     },
    'optional_flag'      : { 'id' : 11, 'Type' : 'B*1',                     'std_name':'OPT_FLAG' ,  'Text' : 'Optional data flag                    ','Missing' : 255    }, #TODO: Needs some more work
    'results_scaling'    : { 'id' : 12, 'Type' : 'I*1',                     'std_name':'RES_SCAL' ,  'Text' : 'Test results scaling exponent         ','Missing' : 0      },
    'lowlimit_scaling'   : { 'id' : 13, 'Type' : 'I*1',                     'std_name':'LLM_SCAL' ,  'Text' : 'Low limit scaling exponent            ','Missing' : 0      },
    'highlimit_scaling'  : { 'id' : 14, 'Type' : 'I*1',                     'std_name':'HLM_SCAL' ,  'Text' : 'High limit scaling exponent           ','Missing' : 0      },
    'lowtest_limit '     : { 'id' : 15, 'Type' : 'R*4',                     'std_name':'LO_LIMIT' ,  'Text' : 'Low test limit value                  ','Missing' : 0.0    },
    'hightest_limit'     : { 'id' : 16, 'Type' : 'R*4',                     'std_name':'HI_LIMIT' ,  'Text' : 'High test limit value                 ','Missing' : 0.0    },
    'test_units'         : { 'id' : 17, 'Type' : 'C*n',                     'std_name':'UNITS'    ,  'Text' : 'Test units                            ','Missing' : ''     },
    'C_resultformat'     : { 'id' : 18, 'Type' : 'C*n',                     'std_name':'C_RESFMT' ,  'Text' : 'ANSI C result format string           ','Missing' : ''     },
    'C_lowlimitformat'   : { 'id' : 19, 'Type' : 'C*n',                     'std_name':'C_LLMFMT' ,  'Text' : 'ANSI C low limit format string        ','Missing' : ''     },
    'C_highlimitformat'  : { 'id' : 20, 'Type' : 'C*n',                     'std_name':'C_HLMFMT' ,  'Text' : 'ANSI C high limit format string       ','Missing' : ''     },
    'low_specification'  : { 'id' : 21, 'Type' : 'R*4',                     'std_name':'LO_SPEC'  ,  'Text' : 'Low specification limit value         ','Missing' : 0.0    },
    'high_specification' : { 'id' : 22, 'Type' : 'R*4',                     'std_name':'HI_SPEC'  ,  'Text' : 'High specification limit value        ','Missing' : 0.0    }
    }
    

    
    def __init__(self): 
        super().__init__()
            
        


