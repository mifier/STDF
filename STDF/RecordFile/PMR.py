from STDF.RecordFile.Record import RecordBase
# class PMR
class PMR(RecordBase):
    """Function:
    Provides indexing of tester channel names, and maps them to physical and logical pin
    names. Each PMR defines the information for a single channel/pin combination."""
    type='PMR'
    verson = 'V4'
    fields={
        'record_length' : {'id' :  0,'Type' :  'U*2',                  'std_name':'REC_LEN'  , 'Text' : 'Bytes of data following header ', 'Missing' : None},
        'record_type'   : {'id' :  1,'Type' :  'U*1',  'Value' :     1,'std_name':'REC_TYP'  , 'Text' : 'Record type                    ', 'Missing' : None},
        'record_subtype': {'id' :  2,'Type' :  'U*1',  'Value' :    60,'std_name':'REC_SUB'  , 'Text' : 'Record sub-type                ', 'Missing' : None},
        'pin_ index'    : {'id' :  3,'Type' :  'U*2',                  'std_name':'PMR_INDX' , 'Text' : 'Unique index associated with pin      ', 'Missing' :    0},
        'channel_type'  : {'id' :  4,'Type' :  'U*2',                  'std_name':'CHAN_TYP' , 'Text' : 'Channel type                          ', 'Missing' :    0},
        'channel_name'  : {'id' :  5,'Type' :  'C*n',                  'std_name':'CHAN_NAM' , 'Text' : 'Channel name                          ', 'Missing' :   ''},
        'physical_name' : {'id' :  6,'Type' :  'C*n',                  'std_name':'PHY_NAM'  , 'Text' : 'Physical name of pin                  ', 'Missing' :   ''},
        'logical_name ' : {'id' :  7,'Type' :  'C*n',                  'std_name':'LOG_NAM'  , 'Text' : 'Logical name of pin                   ', 'Missing' :   ''},
        'head_number'   : {'id' :  8,'Type' :  'U*1',                  'std_name':'HEAD_NUM' , 'Text' : 'Head number associated with channel   ', 'Missing' :    1},
        'site_number'   : {'id' :  9,'Type' :  'U*1',                  'std_name':'SITE_NUM' , 'Text' : 'Site number associated with channel   ', 'Missing' :    1}
            
    }

    
    def __init__(self): 
        super().__init__()

       