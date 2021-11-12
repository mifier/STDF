from STDF.RecordFile.Record import RecordBase

# class DTR
class DTR(RecordBase):
  """Function:
    Contains text information that is to be included in the datalog printout. DTRs may be
    written under the control of a job plan: for example, to highlight unexpected test
    results. They may also be generated by the tester executive software: for example, to
    indicate that the datalog sampling rate has changed. DTRs are placed as comments in
    the datalog listing.
    """
  type='DTR'
  verson = 'V4'
  fields ={     
        'record_length'  : {'id' :  0 ,'Type' :  'U*2' ,                   'std_name': 'REC_LEN'  , 'Text' : 'Bytes of data following header      '  , 'Missing' :    0},
        'record_type'    : {'id' :  1 ,'Type' :  'U*1' ,  'Value' :    50, 'std_name': 'REC_TYP'  , 'Text' : 'Record type                         '  , 'Missing' : None},
        'record_subtype' : {'id' :  2 ,'Type' :  'U*1' ,  'Value' :    30, 'std_name': 'REC_SUB'  , 'Text' : 'Record sub-type                     '  , 'Missing' : None},
        'text_data'      : {'id' :  3 ,'Type' :  'C*n' ,                   'std_name': 'TEXT_DAT' ,'Text'  : 'Message         ', 'Missing' :   ''}
      }

  def __init__(self): 
    super().__init__()

  
