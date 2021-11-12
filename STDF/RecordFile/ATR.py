from STDF.RecordFile.Record import RecordBase

# class ATR
class ATR(RecordBase):
    """ Function:
    Used to record any operation that alters the contents of the STDF file. The name of the
    program and all its parameters should be recorded in the ASCII field provided in this
    record. Typically, this record will be used to track filter programs that have been
    applied to the data."""
    type='ATR'
    verson = 'V4' 
    fields ={     
        'record_length'      : {'id' :  0 ,'Type' :  'U*2' ,                   'std_name': 'REC_LEN'  , 'Text' : 'Bytes of data following header      '  , 'Missing' :    0},
        'record_type'        : {'id' :  1 ,'Type' :  'U*1' ,  'Value' :     0, 'std_name': 'REC_TYP'  , 'Text' : 'Record type                         '  , 'Missing' : None},
        'record_subtype'     : {'id' :  2 ,'Type' :  'U*1' ,  'Value' :    20, 'std_name': 'REC_SUB'  , 'Text' : 'Record sub-type                     '  , 'Missing' : None},
        'modification_time'  : {'id' :  3 ,'Type' :  'U*4' ,                   'std_name': 'MOD_TIM'  ,'Text' : 'Date & time of STDF file modification ', 'Missing' :    0},
        'command_line'       : {'id' :  4 ,'Type' :  'C*n' ,                   'std_name': 'CMD_LINE'  ,'Text' : 'Command line of program               ', 'Missing' :   ''}
        }

    

    def __init__(self): 
        super().__init__()

