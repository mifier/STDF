from STDF.RecordFile.Record import RecordBase
# class SDR
class SDR(RecordBase):
    """Function:
    Contains the configuration information for one or more test sites, connected to one test
    head, that compose a site group.
"""

    type='SDR'
    verson = 'V4'
    fields={
        'record_length'      : { 'id' :  0,'Type' :  'U*2',                          'std_name': 'REC_LEN'  ,'Text' : 'Bytes of data following header ', 'Missing' : None},
        'record_type'        : { 'id' :  1,'Type' :  'U*1',  'Value' :     1,        'std_name': 'REC_TYP'  ,'Text' : 'Record type                    ', 'Missing' : None},
        'record_subtype'     : { 'id' :  2,'Type' :  'U*1',  'Value' :    80,        'std_name': 'REC_SUB'  ,'Text' : 'Record sub-type                ', 'Missing' : None},
        'head_number'        : { 'id' :  3,'Type' : 'U*1',                           'std_name': 'HEAD_NUM' ,'Text' : 'Test head number                      ', 'Missing' : 1   },
        'site group number'  : { 'id' :  4,'Type' : 'U*1',                           'std_name': 'SITE_GRP' ,'Text' : 'Site group number                     ', 'Missing' : 1   },
        'number_testsites'   : { 'id' :  5,'Type' : 'U*1',                           'std_name': 'SITE_CNT' ,'Text' : 'Number (k) of test sites in site group', 'Missing' : 1   },
        'site_number'        : { 'id' :  6,'Type' : 'xU*1','Length':'number_testsites','std_name': 'SITE_NUM' ,'Text' : 'Array of k test site numbers          ', 'Missing' : [1] },
        'handler_type'       : { 'id' :  7,'Type' : 'C*n',                           'std_name': 'HAND_TYP' ,'Text' : 'Handler or prober type                ', 'Missing' : ''  },
        'handler_ID'         : { 'id' :  8,'Type' : 'C*n',                           'std_name': 'HAND_ID'  ,'Text' : 'Handler or prober ID                  ', 'Missing' : ''  },
        'card_type'          : { 'id' :  9,'Type' : 'C*n',                           'std_name': 'CARD_TYP' ,'Text' : 'Probe card type                       ', 'Missing' : ''  },
        'card_ID'            : { 'id' : 10,'Type' : 'C*n',                           'std_name': 'CARD_ID'  ,'Text' : 'Probe card ID                         ', 'Missing' : ''  },
        'loadboard_type'     : { 'id' : 11,'Type' : 'C*n',                           'std_name': 'LOAD_TYP' ,'Text' : 'Load board type                       ', 'Missing' : ''  },
        'loadboard_ID'       : { 'id' : 12,'Type' : 'C*n',                           'std_name': 'LOAD_ID'  ,'Text' : 'Load board ID                         ', 'Missing' : ''  },
        'DIBboard_type'      : { 'id' : 13,'Type' : 'C*n',                           'std_name': 'DIB_TYP'  ,'Text' : 'DIB (aka load-) board type            ', 'Missing' : ''  },
        'DIBboard_ID'        : { 'id' : 14,'Type' : 'C*n',                           'std_name': 'DIB_ID'   ,'Text' : 'DIB (aka load-) board ID              ', 'Missing' : ''  },
        'cable_type'         : { 'id' : 15,'Type' : 'C*n',                           'std_name': 'CABL_TYP' ,'Text' : 'Interface cable type                  ', 'Missing' : ''  },
        'cable_ID'           : { 'id' : 16,'Type' : 'C*n',                           'std_name': 'CABL_ID'  ,'Text' : 'Interface cable ID                    ', 'Missing' : ''  },
        'contactor_type'     : { 'id' : 17,'Type' : 'C*n',                           'std_name': 'CONT_TYP' ,'Text' : 'Handler contactor type                ', 'Missing' : ''  },
        'contactor_ID'       : { 'id' : 18,'Type' : 'C*n',                           'std_name': 'CONT_ID'  ,'Text' : 'Handler contactor ID                  ', 'Missing' : ''  },
        'laser_type'         : { 'id' : 19,'Type' : 'C*n',                           'std_name': 'LASR_TYP' ,'Text' : 'Laser type                            ', 'Missing' : ''  },
        'laser_ID'           : { 'id' : 20,'Type' : 'C*n',                           'std_name': 'LASR_ID'  ,'Text' : 'Laser ID                              ', 'Missing' : ''  },
    'extra_equipment_type'   : { 'id' : 21,'Type' : 'C*n',                           'std_name': 'EXTR_TYP' ,'Text' : 'Extra equipment type                  ', 'Missing' : ''  },
        'extra_equipment_ID' : { 'id' : 22,'Type' : 'C*n',                           'std_name': 'EXTR_ID'  ,'Text' : 'Extra equipment ID                    ', 'Missing' : ''  }
    
    }

                   
    
    def __init__(self): 
        super().__init__()
