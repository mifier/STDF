from STDF.RecordFile.Record import RecordBase
# class PGR
class PGR(RecordBase):
    """Function:
    Associates a name with a group of pins."""
    type='PGR'
    verson = 'V4'
    fields ={
       'record_length'         : {'id' :  0, 'Type' :  'U*2',                         'std_name':'REC_LEN'  ,  'Text' : 'Bytes of data following header ', 'Missing' : None},
       'record_type'           : {'id' :  1, 'Type' :  'U*1',  'Value' :     1,       'std_name':'REC_TYP'  ,  'Text' : 'Record type                    ', 'Missing' : None},
       'record_subtype'        : {'id' :  2, 'Type' :  'U*1',  'Value' :    62,       'std_name':'REC_SUB'  ,  'Text' : 'Record sub-type                ', 'Missing' : None},
        'index_pingroup'       : {'id' :  3, 'Type' :  'U*2',                         'std_name':'GRP_INDX' ,  'Text' : 'Unique index associated with pin group', 'Missing' :    0},
        'Name_pingroup'        : {'id' :  4, 'Type' :  'C*n',                         'std_name':'GRP_NAM'  ,  'Text' : 'Name of pin group                     ', 'Missing' :   ''},
        'Count_indexes'        : {'id' :  5, 'Type' :  'U*2',                         'std_name':'INDX_CNT' ,  'Text' : 'Count (k) of PMR indexes              ', 'Missing' :    0},
        'PMR_indexes'          : {'id' :  6, 'Type' : 'xU*2','Length':'Count_indexes','std_name':'PMR_INDX' ,  'Text' : 'Array of indexes for pins in the group', 'Missing' :   []}
         
    }

    
    

    def __init__(self): 
        super().__init__()

