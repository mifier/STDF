from STDF.RecordFile.Record import RecordBase
# class WRR
class WRR(RecordBase):
    """
Function:
    Contains the result information relating to each wafer tested by the job plan. The WRR
    and the Wafer Information Record (WIR) bracket all the stored information pertaining
    to one tested wafer. This record is used only when testing at wafer probe time. A
    WIR/WRR pair will have the same HEAD_NUM and SITE_GRP values."""
    type='WRR'
    verson = 'V4'
    fields ={
        'record_length'         : {  'id' :  0, 'Type' :  'U*2',                     'std_name':  'REC_LEN'  ,'Text' : 'Bytes of data following header ', 'Missing' : None},
        'record_type'           : {  'id' :  1, 'Type' :  'U*1',  'Value' :     2,   'std_name':  'REC_TYP'  ,'Text' : 'Record type                    ', 'Missing' : None},
        'record_subtype'        : {  'id' :  2, 'Type' :  'U*1',  'Value' :    20,   'std_name':  'REC_SUB'  ,'Text' : 'Record sub-type                ', 'Missing' : None},
        'head_number'           : {  'id' :  3, 'Type' : 'U*1',                      'std_name':  'HEAD_NUM' ,'Text' : 'Test head number                      ', 'Missing' : 255       },
        'sit_group_number'      : {  'id' :  4, 'Type' : 'U*1',                      'std_name':  'SITE_GRP' ,'Text' : 'Site group number                     ', 'Missing' : 255       },
        'finish_time'           : {  'id' :  5, 'Type' : 'U*4',                      'std_name':  'FINISH_T' ,'Text' : 'Date and time last part tested        ', 'Missing' : 0         },
        'number_tested'         : {  'id' :  6, 'Type' : 'U*4',                      'std_name':  'PART_CNT' ,'Text' : 'Number of parts tested                ', 'Missing' : 0         },
        'number_retested'       : {  'id' :  7, 'Type' : 'U*4',                      'std_name':  'RTST_CNT' ,'Text' : 'Number of parts retested              ', 'Missing' : 4294967295},
        'number_aborts'         : {  'id' :  8, 'Type' : 'U*4',                      'std_name':  'ABRT_CNT' ,'Text' : 'Number of aborts during testing       ', 'Missing' : 4294967295},
        'number_good'           : {  'id' :  9, 'Type' : 'U*4',                      'std_name':  'GOOD_CNT' ,'Text' : 'Number of good (passed) parts tested  ', 'Missing' : 4294967295},
        'number_functional'     : {  'id' : 10, 'Type' : 'U*4',                      'std_name':  'FUNC_CNT' ,'Text' : 'Number of functional parts tested     ', 'Missing' : 4294967295},
        'wafer_ID'              : {  'id' : 11, 'Type' : 'C*n',                      'std_name':  'WAFER_ID' ,'Text' : 'Wafer ID                              ', 'Missing' : ''        },
        'fab_wafer_ID'          : {  'id' : 12, 'Type' : 'C*n',                      'std_name':  'FABWF_ID' ,'Text' : 'Fab wafer ID                          ', 'Missing' : ''        },
        'frame_ID'              : {  'id' : 13, 'Type' : 'C*n',                      'std_name':  'FRAME_ID' ,'Text' : 'Wafer frame ID                        ', 'Missing' : ''        },
        'mask_ID'               : {  'id' : 14, 'Type' : 'C*n',                      'std_name':  'MASK_ID'  ,'Text' : 'Wafer mask ID                         ', 'Missing' : ''        },
        'user_description'      : {  'id' : 15, 'Type' : 'C*n',                      'std_name':  'USR_DESC' ,'Text' : 'Wafer description supplied by user    ', 'Missing' : ''        },
        'exec_description'      : {  'id' : 16, 'Type' : 'C*n',                      'std_name':  'EXC_DESC' ,'Text' : 'Wafer description supplied by exec    ', 'Missing' : ''        }
       
    }

    
    def __init__(self): 
        super().__init__()

