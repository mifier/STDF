from STDF.RecordFile.Record import _stdf_time_value,RecordBase
# class MIR
class MIR(RecordBase):
    """Function:
    The MIR and the MRR (Master Results Record) contain all the global information that
    is to be stored for a tested lot of parts. Each data stream must have exactly one MIR,
    immediately after the FAR (and the ATRs, if they are used). This will allow any data
    reporting or analysis programs access to this information in the shortest possible
    amount of time.
"""
    type='MIR'
    verson = 'V4'
    fields={
        'record_length'          : {'id' :  0,'Type' : 'U*2',                  'std_name': 'REC_LEN'  ,'Text' : 'Bytes of data following header ', 'Missing' : None},
        'record_type'            : {'id' :  1,'Type' : 'U*1', 'Value' :     1, 'std_name': 'REC_TYP'  ,'Text' : 'Record type                    ', 'Missing' : None},
        'record_subtype'         : {'id' :  2,'Type' : 'U*1', 'Value' :    10, 'std_name': 'REC_SUB'  ,'Text' : 'Record sub-type                ', 'Missing' : None},
        'time_setup'             : {'id' :  3,'Type' : 'U*4',                   'std_name': 'SETUP_T'  ,  'Text' : 'Date and time of job setup            ', 'Missing' : _stdf_time_value},
        'time_firstparttested'   : {'id' :  4,'Type' : 'U*4',                   'std_name': 'START_T'  ,  'Text' : 'Date and time first part tested       ', 'Missing' : _stdf_time_value},
        'station_number'         : {'id' :  5,'Type' : 'U*1',                   'std_name': 'STAT_NUM' ,  'Text' : 'Tester station number                 ', 'Missing' :    0},
        'mode_code'              : {'id' :  6,'Type' : 'C*1',                   'std_name': 'MODE_COD' ,  'Text' : 'Test mode code : A/M/P/E/M/P/Q/space  ', 'Missing' :  ' '}, 
        'retest_code'            : {'id' :  7,'Type' : 'C*1',                   'std_name': 'RTST_COD' ,  'Text' : 'Lot retest code : Y/N/0..9/space      ', 'Missing' :  ' '},
        'protection_code'        : {'id' :  8,'Type' : 'C*1',                   'std_name': 'PROT_COD' ,  'Text' : 'Data protection code 0..9/A..Z/space  ', 'Missing' :  ' '},
        'burn-in_time'           : {'id' :  9,'Type' : 'U*2',                   'std_name': 'BURN_TIM' ,  'Text' : 'Burn-in time (in minutes)             ', 'Missing' :65535},
        'commandmode_code'       : {'id' : 10,'Type' : 'C*1',                   'std_name': 'CMOD_COD' ,  'Text' : 'Command mode code                     ', 'Missing' :  ' '},
        'lot_ID'                 : {'id' : 11,'Type' : 'C*n',                   'std_name': 'LOT_ID'   ,  'Text' : 'Lot ID (customer specified)           ', 'Missing' :   ''},
        'part_type'              : {'id' : 12,'Type' : 'C*n',                   'std_name': 'PART_TYP' ,  'Text' : 'Part Type (or product ID)             ', 'Missing' :   ''},
        'Name_node'              : {'id' : 13,'Type' : 'C*n',                   'std_name': 'NODE_NAM' ,  'Text' : 'Name of node that generated data      ', 'Missing' :   ''},
        'tester_type'            : {'id' : 14,'Type' : 'C*n',                   'std_name': 'TSTR_TYP' ,  'Text' : 'Tester type                           ', 'Missing' :   ''},
        'Job_name'               : {'id' : 15,'Type' : 'C*n',                   'std_name': 'JOB_NAM'  ,  'Text' : 'Job name (test program name)          ', 'Missing' :   ''},
        'Job_revisionnumber'     : {'id' : 16,'Type' : 'C*n',                   'std_name': 'JOB_REV'  ,  'Text' : 'Job (test program) revision number    ', 'Missing' :   ''},
        'sublot_ID'              : {'id' : 17,'Type' : 'C*n',                   'std_name': 'SBLOT_ID' ,  'Text' : 'Sublot ID                             ', 'Missing' :   ''},
        'operator_name'          : {'id' : 18,'Type' : 'C*n',                   'std_name': 'OPER_NAM' ,  'Text' : 'Operator name or ID (at setup time)   ', 'Missing' :   ''},
        'software_type'          : {'id' : 19,'Type' : 'C*n',                   'std_name': 'EXEC_TYP' ,  'Text' : 'Tester executive software type        ', 'Missing' :   ''},
        'software_version'       : {'id' : 20,'Type' : 'C*n',                   'std_name': 'EXEC_VER' ,  'Text' : 'Tester exec software version number   ', 'Missing' :   ''},
        'test_code'              : {'id' : 21,'Type' : 'C*n',                   'std_name': 'TEST_COD' ,  'Text' : 'Test phase or step code               ', 'Missing' :   ''},
        'test_temperature'       : {'id' : 22,'Type' : 'C*n',                   'std_name': 'TST_TEMP' ,  'Text' : 'Test temperature                      ', 'Missing' :   ''},
        'user_text'              : {'id' : 23,'Type' : 'C*n',                   'std_name': 'USER_TXT' ,  'Text' : 'Generic user text                     ', 'Missing' :   ''},
        'auxiliary_file'         : {'id' : 24,'Type' : 'C*n',                   'std_name': 'AUX_FILE' ,  'Text' : 'Name of auxiliary data file           ', 'Missing' :   ''},
        'package_type'           : {'id' : 25,'Type' : 'C*n',                   'std_name': 'PKG_TYP'  ,  'Text' : 'Package type                          ', 'Missing' :   ''},
        'family_ID'              : {'id' : 26,'Type' : 'C*n',                   'std_name': 'FAMLY_ID' ,  'Text' : 'Product family ID                     ', 'Missing' :   ''},
        'date_code'              : {'id' : 27,'Type' : 'C*n',                   'std_name': 'DATE_COD' ,  'Text' : 'Date code                             ', 'Missing' :   ''},
        'facility_ID'            : {'id' : 28,'Type' : 'C*n',                   'std_name': 'FACIL_ID' ,  'Text' : 'Test facility ID                      ', 'Missing' :   ''},
        'floor_ID'               : {'id' : 29,'Type' : 'C*n',                   'std_name': 'FLOOR_ID' ,  'Text' : 'Test floor ID                         ', 'Missing' :   ''},
        'process_ID'             : {'id' : 30,'Type' : 'C*n',                   'std_name': 'PROC_ID'  ,  'Text' : 'Fabrication process ID                ', 'Missing' :   ''},
        'operation_frequency'    : {'id' : 31,'Type' : 'C*n',                   'std_name': 'OPER_FRQ' ,  'Text' : 'Operation frequency or step           ', 'Missing' :   ''},
        'specification_name'     : {'id' : 32,'Type' : 'C*n',                   'std_name': 'SPEC_NAM' ,  'Text' : 'Test specification name               ', 'Missing' :   ''},
        'specification_version'  : {'id' : 33,'Type' : 'C*n',                   'std_name': 'SPEC_VER' ,  'Text' : 'Test specification version number     ', 'Missing' :   ''},
        'flow_ID'                : {'id' : 34,'Type' : 'C*n',                   'std_name': 'FLOW_ID'  ,  'Text' : 'Test flow ID                          ', 'Missing' :   ''},
        'setup_ID'               : {'id' : 35,'Type' : 'C*n',                   'std_name': 'SETUP_ID' ,  'Text' : 'Test setup ID                         ', 'Missing' :   ''},
        'design_revision'        : {'id' : 36,'Type' : 'C*n',                   'std_name': 'DSGN_REV' ,  'Text' : 'Device design revision                ', 'Missing' :   ''},
        'Engineeringlot_ID'      : {'id' : 37,'Type' : 'C*n',                   'std_name': 'ENG_ID'   ,  'Text' : 'Engineering lot ID                    ', 'Missing' :   ''},
        'ROMcode_ID'             : {'id' : 38,'Type' : 'C*n',                   'std_name': 'ROM_COD'  ,  'Text' : 'ROM code ID                           ', 'Missing' :   ''},
        'serial_number'          : {'id' : 39,'Type' : 'C*n',                   'std_name': 'SERL_NUM' ,  'Text' : 'Tester serial number                  ', 'Missing' :   ''},
        'supervisor_name'        : {'id' : 40,'Type' : 'C*n',                   'std_name': 'SUPR_NAM' ,  'Text' : 'Supervisor name or ID                 ', 'Missing' :   ''}
        }
    
    

    def __init__(self): 
        super().__init__()
