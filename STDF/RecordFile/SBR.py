from STDF.RecordFile.Record import RecordBase
# class SBR
class SBR(RecordBase):
    """Function:
    Stores a count of the parts associated with a particular logical bin after testing. This
    bin count can be for a single test site (when parallel testing) or a total for all test sites.
    The STDF specification also supports a Hardware Bin Record (HBR) for actual physical
    binning. A part is "physically" placed in a hardware bin after testing. A part can be
    "logically" associated with a software bin during or after testing."""
    type='SBR'
    verson = 'V4'
    fields={
         'record_length'       : {'id' :  0, 'Type' :  'U*2',                   'std_name': 'REC_LEN'  , 'Text' : 'Bytes of data following header ', 'Missing' : None},
         'record_type'         : {'id' :  1, 'Type' :  'U*1',  'Value' :     1, 'std_name': 'REC_TYP'  , 'Text' : 'Record type                    ', 'Missing' : None},
         'record_subtype'      : {'id' :  2, 'Type' :  'U*1',  'Value' :    50, 'std_name': 'REC_SUB'  , 'Text' : 'Record sub-type                ', 'Missing' : None},
         'head_number'         : {'id' :  3, 'Type' :  'U*1',                   'std_name': 'HEAD_NUM' , 'Text' : 'Test head number (255 = summary)      ', 'Missing' : 1   },
         'site_number'         : {'id' :  4, 'Type' :  'U*1',                   'std_name': 'SITE_NUM' , 'Text' : 'Test site number                      ', 'Missing' : 1   },
         'softwarebin_number'  : {'id' :  5, 'Type' :  'U*2',                   'std_name': 'SBIN_NUM' , 'Text' : 'Software bin number                   ', 'Missing' : 0   },
         'number_parts'        : {'id' :  6, 'Type' :  'U*4',                   'std_name': 'SBIN_CNT' , 'Text' : 'Number of parts in bin                ', 'Missing' : 0   },
         'pass/fail_indicate'  : {'id' :  7, 'Type' :  'C*1',                   'std_name': 'SBIN_PF'  , 'Text' : 'Pass/fail indication (P/F)            ', 'Missing' : ' ' },
         'name_softwarebin'    : {'id' :  8, 'Type' :  'C*n',                   'std_name': 'SBIN_NAM' , 'Text' : 'Name of software bin                  ', 'Missing' : ''  }
          
    }

    
    def __init__(self): 
        super().__init__()


       