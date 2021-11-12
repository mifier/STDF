from STDF.RecordFile.Record import RecordBase
# class RDR
class RDR(RecordBase):
    """Function:
    Signals that the data in this STDF file is for retested parts. The data in this record,
    combined with information in the MIR, tells data filtering programs what data to
    replace when processing retest data."""

    type='RDR'
    verson = 'V4'
    fields={
        'record_length'    : { 'id' :  0,'Type' :  'U*2',                           'std_name':'REC_LEN'   , 'Text' : 'Bytes of data following header ', 'Missing' : None},
        'record_type'      : { 'id' :  1,'Type' :  'U*1',  'Value' :     1,         'std_name':'REC_TYP'   , 'Text' : 'Record type                    ', 'Missing' : None},
        'record_subtype'   : { 'id' :  2,'Type' :  'U*1',  'Value' :    70,         'std_name':'REC_SUB'   , 'Text' : 'Record sub-type                ', 'Missing' : None},
        'number_retested'  : { 'id' :  3,'Type' : 'U*2' ,                           'std_name':'NUM_BINS'  , 'Text' : 'Number (k) of bins being retested     ', 'Missing' : 0   },
        'retest_numbers'   : { 'id' :  4,'Type' : 'xU*2','Length':'number_retested','std_name':'RTST_BIN'  , 'Text' : 'Array of retest bin numbers           ', 'Missing' : []  }
        
    }

    
    def __init__(self): 
        super().__init__()

    
