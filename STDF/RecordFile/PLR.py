from STDF.RecordFile.Record import RecordBase
# class PLR
class PLR(RecordBase):
    """Function:
    Defines the current display radix and operating mode for a pin or pin group."""
    type='PLR'
    verson = 'V4'
    fields ={
        'record_length'           : { 'id' :  0,'Type' :  'U*2',                  'std_name':  'REC_LEN'  ,'Text' : 'Bytes of data following header ', 'Missing' : None},
        'record_type'             : { 'id' :  1,'Type' :  'U*1',  'Value' :     1,'std_name':  'REC_TYP'  ,'Text' : 'Record type                    ', 'Missing' : None},
        'record_subtype'          : { 'id' :  2,'Type' :  'U*1',  'Value' :    63,'std_name':  'REC_SUB'  ,'Text' : 'Record sub-type                ', 'Missing' : None},
        'Count_pingroups'         : { 'id' :  3,'Type' :  'U*2',                  'std_name':  'GRP_CNT'  ,'Text' : 'Count (k) of pins or pin groups       ', 'Missing' :    0},
        'pingroup_indexes'        : { 'id' :  4,'Type' : 'xU*2',                  'std_name':  'GRP_INDX' ,'Text' : 'Array of pin or pin group indexes     ', 'Missing' :   []},
        'mode_pingroup'           : { 'id' :  5,'Type' : 'xU*2',                  'std_name':  'GRP_MODE' ,'Text' : 'Operating mode of pin group           ', 'Missing' :   []},
        'radix_pingroup'          : { 'id' :  6,'Type' : 'xU*1',                  'std_name':  'GRP_RADX' ,'Text' : 'Display radix of pin group            ', 'Missing' :   []},
        'Programcharacters_right' : { 'id' :  7,'Type' : 'xC*n',                  'std_name':  'PGM_CHAR' ,'Text' : 'Program state encoding characters     ', 'Missing' :   []},
        'Returncharacters_right'  : { 'id' :  8,'Type' : 'xC*n',                  'std_name':  'RTN_CHAR' ,'Text' : 'Return state encoding characters      ', 'Missing' :   []},
        'Programcharacters_left'  : { 'id' :  9,'Type' : 'xC*n',                  'std_name':  'PGM_CHAL' ,'Text' : 'Program state encoding characters     ', 'Missing' :   []},
        'Returncharacters_left'   : { 'id' : 10,'Type' : 'xC*n',                  'std_name':  'RTN_CHAL' ,'Text' : 'Return state encoding characters      ', 'Missing' :   []}
    
    }

    
    def __init__(self): 
        super().__init__()

       