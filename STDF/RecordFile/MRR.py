from STDF.RecordFile.Record import RecordBase,_stdf_time_value
# class MRR
class MRR(RecordBase):
    """Function:
    The Master Results Record (MRR) is a logical extension of the Master Information
    Record (MIR). The data can be thought of as belonging with the MIR, but it is not
    available when the tester writes the MIR information. Each data stream must have
    exactly one MRR as the last record in the data stream."""

    type='MRR'
    verson = 'V4'
    fields={
        'record_length'        : { 'id' :  0, 'Type' :  'U*2',                      'std_name':  'REC_LEN'  ,  'Text' : 'Bytes of data following header ', 'Missing' : None},
        'record_type'          : { 'id' :  1, 'Type' :  'U*1',   'Value' :     1,   'std_name':  'REC_TYP'  ,  'Text' : 'Record type                    ', 'Missing' : None},
        'record_subtype'       : { 'id' :  2, 'Type' :  'U*1',   'Value' :    20,   'std_name':  'REC_SUB'  ,  'Text' : 'Record sub-type                ', 'Missing' : None},
        'finish_time'          : { 'id' :  3, 'Type' : 'U*4',                       'std_name':  'FINISH_T' ,  'Text' : 'Date and time last part tested        ', 'Missing' : _stdf_time_value},
        'disposition_code'     : { 'id' :  4, 'Type' : 'C*1',                       'std_name':  'DISP_COD' ,  'Text' : 'Lot disposition code                  ', 'Missing' :        ' '},
        'user_description'     : { 'id' :  5, 'Type' : 'C*n',                       'std_name':  'USR_DESC' ,  'Text' : 'Lot description supplied by user      ', 'Missing' :         ''},
        'software_description' : { 'id' :  6, 'Type' : 'C*n',                       'std_name':  'EXC_DESC' ,  'Text' : 'Lot description supplied by exec      ', 'Missing' :         ''}        
    }

    
    
    def __init__(self): 
        super().__init__()

