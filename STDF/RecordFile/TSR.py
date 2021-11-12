from STDF.RecordFile.Record import RecordBase
# class TSR
class TSR(RecordBase):
    """Function:
    Contains the test execution and failure counts for one parametric or functional test in
    the test program. Also contains static information, such as test name. The TSR is
    related to the Functional Test Record (FTR), the Parametric Test Record (PTR), and the
    Multiple Parametric Test Record (MPR) by test number, head number, and site
    number."""
    type='TSR'
    verson = 'V4'
    fields={
        'record_length'      : {'id' :  0,'Type' :  'U*2',                   'std_name': 'REC_LEN'  , 'Text' : 'Bytes of data following header ', 'Missing' : None},
        'record_type'        : {'id' :  1,'Type' :  'U*1',  'Value' :    10, 'std_name': 'REC_TYP'  , 'Text' : 'Record type                    ', 'Missing' : None},
        'record_subtype'     : {'id' :  2,'Type' :  'U*1',  'Value' :    30, 'std_name': 'REC_SUB'  , 'Text' : 'Record sub-type                ', 'Missing' : None},
        'head_number'        : {'id' :  3,'Type' : 'U*1',                    'std_name': 'HEAD_NUM' , 'Text' : 'Test head number                      ', 'Missing' : 255        },
        'site_number'        : {'id' :  4,'Type' : 'U*1',                    'std_name': 'SITE_NUM' , 'Text' : 'Test site number                      ', 'Missing' : 255        },
        'test type'          : {'id' :  5,'Type' : 'C*1',                    'std_name': 'TEST_TYP' , 'Text' : 'Test type [P/F/space]                 ', 'Missing' : ' '        },
        'test number'        : {'id' :  6,'Type' : 'U*4',                    'std_name': 'TEST_NUM' , 'Text' : 'Test number                           ', 'Missing' : None       },
        'number_executions'  : {'id' :  7,'Type' : 'U*4',                    'std_name': 'EXEC_CNT' , 'Text' : 'Number of test executions             ', 'Missing' : 4294967295},
        'number_failures'    : {'id' :  8,'Type' : 'U*4',                    'std_name': 'FAIL_CNT' , 'Text' : 'Number of test failures               ', 'Missing' : 4294967295},
        'number_alarmed'     : {'id' :  9,'Type' : 'U*4',                    'std_name': 'ALRM_CNT' , 'Text' : 'Number of alarmed tests               ', 'Missing' : 4294967295},
        'test_name'          : {'id' : 10,'Type' : 'C*n',                    'std_name': 'TEST_NAM' , 'Text' : 'Test name                             ', 'Missing' : ''         },
        'sequencer_name'     : {'id' : 11,'Type' : 'C*n',                    'std_name': 'SEQ_NAME' , 'Text' : 'Sequencer (program segment/flow) name ', 'Missing' : ''         },
        'test_label'         : {'id' : 12,'Type' : 'C*n',                    'std_name': 'TEST_LBL' , 'Text' : 'Test label or text                    ', 'Missing' : ''         },
        'optional_flag'      : {'id' : 13,'Type' : 'B*1',                    'std_name': 'OPT_FLAG' , 'Text' : 'Optional data flag See note           ', 'Missing' : ['1']*8    },
        'execution_time'     : {'id' : 14,'Type' : 'R*4',                    'std_name': 'TEST_TIM' , 'Text' : 'Average test execution time in seconds', 'Missing' : 0.0        },
        'lowest_test_result ': {'id' : 15,'Type' : 'R*4',                    'std_name': 'TEST_MIN' , 'Text' : 'Lowest test result value              ', 'Missing' : 0.0        },
        'highest_test_result': {'id' : 16,'Type' : 'R*4',                    'std_name': 'TEST_MAX' , 'Text' : 'Highest test result value             ', 'Missing' : 0.0        },
        'sum_result'         : {'id' : 17,'Type' : 'R*4',                    'std_name': 'TST_SUMS' , 'Text' : 'Sum of test result values             ', 'Missing' : 0.0        },
        'sum_square_result'  : {'id' : 18,'Type' : 'R*4',                    'std_name': 'TST_SQRS' , 'Text' : 'Sum of squares of test result values  ', 'Missing' : 0.0        }
    
    }



    

    
    
    def __init__(self): 
        super().__init__()
     