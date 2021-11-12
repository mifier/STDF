from STDF.RecordFile.Record import RecordBase

# class HBR
class HBR(RecordBase):
    """Function:
    Stores a count of the parts "physically" placed in a particular bin after testing. (In
    wafer testing, "physical" binning is not an actual transfer of the DUT, but rather is
    represented by a drop of ink or an entry in a wafer map file.) This bin count can be for
    a single test site (when parallel testing) or a total for all test sites. The STDF
    specification also supports a Software Bin Record (SBR) for logical binning categories.
    A part is "physically" placed in a hardware bin after testing. A part can be "logically"
    associated with a software bin during or after testing."""
    type='HBR'
    verson = 'V4'
    fields={  
        'record_length'      : { 'id' :  0,'Type' :  'U*2',                  'std_name': 'REC_LEN'    ,'Text' : 'Bytes of data following header ', 'Missing' : None},
        'record_type'        : { 'id' :  1,'Type' :  'U*1', 'Value' :     1, 'std_name': 'REC_TYP'    ,'Text' : 'Record type                    ', 'Missing' : None},
        'record_subtype'     : { 'id' :  2,'Type' :  'U*1', 'Value' :    40, 'std_name': 'REC_SUB'    ,'Text' : 'Record sub-type                ', 'Missing' : None},
        'head_number'        : { 'id' :  3,'Type' :  'U*1',                  'std_name': 'HEAD_NUM'   ,'Text' : 'Test head number            ', 'Missing' :   255},
        'site_number'        : { 'id' :  4,'Type' :  'U*1',                  'std_name': 'SITE_NUM'   ,'Text' : 'Test site number            ', 'Missing' :   255},
        'hardwarebin_number' : { 'id' :  5,'Type' :  'U*2',                  'std_name': 'HBIN_NUM'   ,'Text' : 'Hardware bin number         ', 'Missing' : 65535},
        'number_parts'       : { 'id' :  6,'Type' :  'U*4',                  'std_name': 'HBIN_CNT'   ,'Text' : 'Number of parts in bin      ', 'Missing' :     0},
        'pass/fail_indicate' : { 'id' :  7,'Type' :  'C*1',                  'std_name': 'HBIN_PF'    ,'Text' : 'Pass/fail indication (P/F)  ', 'Missing' :   ' '},
        'name_hardwarebin'   : { 'id' :  8,'Type' :  'C*n',                  'std_name': 'HBIN_NAM'   ,'Text' : 'Name of hardware bin        ', 'Missing' :    ''}
        }

    
       
    def __init__(self): 
        super().__init__()

