from abc import ABC
from io import BytesIO
import time
import struct
import math

DataType = {   
            'C*1'  : {'Type' :'C'  ,'Value' :    1, 'Text' : 'One byte fixed length string             ' },
            'C*2'  : {'Type' :'C'  ,'Value' :    2, 'Text' : 'Two byte fixed length string             ' },
            'C*4'  : {'Type' :'C'  ,'Value' :    4, 'Text' : 'Four byte fixed length string            ' },  
            'C*n'  : {'Type' :'C'  ,'Value' : None, 'Text' : 'Variable length AsCII character string   ' },           
            'U*1'  : {'Type' :'U'  ,'Value' :    1, 'Text' : 'One byte unsigned integer                ' },
            'U*2'  : {'Type' :'U'  ,'Value' :    2, 'Text' : 'Two byte unsigned integer                ' },
            'U*4'  : {'Type' :'U'  ,'Value' :    4, 'Text' : 'Four byte unsigned integer               ' },
            'U*8'  : {'Type' :'U'  ,'Value' :    8, 'Text' : 'Eight byte unsigned integer              ' }, 
            'U*n'  : {'Type' :'U'  ,'Value' : None, 'Text' : 'Variable length byte unsigned integer    ' },           
            'I*1'  : {'Type' :'I'  ,'Value' :    1, 'Text' : 'One byte signed integer                  ' },
            'I*2'  : {'Type' :'I'  ,'Value' :    2, 'Text' : 'Two byte signed integer                  ' },
            'I*4'  : {'Type' :'I'  ,'Value' :    4, 'Text' : 'Four byte signed integer                 ' },
            'R*4'  : {'Type' :'R4' ,'Value' :    4, 'Text' : 'Four byte floating point number          ' },  
            'R*8'  : {'Type' :'R8' ,'Value' :    8, 'Text' : 'Eight byte floating point number         ' },
            'B*0'  : {'Type' :'B'  ,'Value' :    0, 'Text' : 'be used to ensure even byte alignment    ' },
            'B*1'  : {'Type' :'B'  ,'Value' :    1, 'Text' : 'One byte length binary data string       ' },
            'B*n'  : {'Type' :'B'  ,'Value' : None, 'Text' : 'Variable length binary data string       ' },
            'xU*1' : {'Type' :'U*1','Value' :    1, 'Text' : 'One byte unsigned integer                ' },
            'xU*2' : {'Type' :'U*2','Value' :    2, 'Text' : 'Two byte unsigned integer                ' },

            'D*n'  : {'Type' :'D'  ,'Value' : None, 'Text' : 'Bit encoded data                         ' },
            'N*1'  : {'Type' :'N'  ,'Value' :    1, 'Text' : 'Unsigned integer data stored in a nibble ' },
            'xN*1' : {'Type' :'N*1','Value' :    1, 'Text' : 'Unsigned integer data stored in a nibble ' },
            '*R*4' : {'Type' :'R*4','Value' :    4, 'Text' : 'Four byte floating point number          ' }, 
            'xV*n' : {'Type' :  'V','Value' :    1, 'Text' : 'Variable data type field                    ' }
             }

             
def get_DataType_typelength(TypeCode): 
    from operator import itemgetter
    keys = ['Type','Value']
    dicttemp=DataType[TypeCode]
    out = itemgetter(*keys)(dicttemp)
    return out
# 得到某个字节中某一位(Bit)的值
# returns: 返回读取该位的值，0或1
def get_bit_val(byte, index):
    byte=int.from_bytes(byte, byteorder='big', signed=False)
    if byte & (1 << index):
        return 1
    else:
        return 0    
# 更改某个字节中某一位(Bit)的值
# returns: 返回更改后字节的值
def set_bit_val(byte, index, val):
    byte=int.from_bytes(byte, byteorder='big', signed=False)
    
    if val:
        return int(byte | (1 << index)).to_bytes(length=1, byteorder='big', signed=False)
    else:
        return  int(byte & ~(1 << index)).to_bytes(length=1, byteorder='big', signed=False)
#  返回V*n类型的子类型和其长度
V_subtypecode={
               0 :'B*0',
               1 :'U*1',
               2 :'U*2',
               3 :'U*4',
               4 :'I*1',
               5 :'I*2',
               6 :'I*4',
               7 :'R*4',
               8 :'R*8',
               10:'C*n',
               11:'B*n',
               12:'D*n',
               13:'N*1'
               }
# 将V*n的子类型代码解析成data类型
def get_V_subtypecode(firstbyte_int):
    for key,value in V_subtypecode.items():
        if key==firstbyte_int:
            return value
# 将data类型解析成V*n的子类型代码
def get_subtypecode_V(dataType):
    for key,value in V_subtypecode.items():
        if value==dataType:
            return key
        
class RecordBase(ABC):
    """Record base class"""
    BinBuffer=b''
    type='Record'
    number_fields=0
    fields ={     
        'record_length'  : {'id' :  0 ,'Type' :  'U*2' ,                  'std_name': 'REC_LEN'  , 'Text' : 'Bytes of data following header      '  , 'Missing' : 0  },
        'record_type'    : {'id' :  1 ,'Type' :  'U*1' ,  'Value' :    0, 'std_name': 'REC_TYP'  , 'Text' : 'Record type                         '  , 'Missing' : None},
        'record_subtype' : {'id' :  2 ,'Type' :  'U*1' ,  'Value' :    0, 'std_name': 'REC_SUB'  , 'Text' : 'Record sub-type                     '  , 'Missing' : None}
    }

    def __init__(self,):
        self.value=[None for _ in range(len(self.fields))]
        self.value[1]=self.fields[ 'record_type']['Value']
        self.value[2]=self.fields[ 'record_subtype']['Value']
      
    
    def __getitem__(self, item):
        id =self.fields[item]['id']
        return self.value[id]
 
    def __setitem__(self, item, value):
        id =self.fields[item]['id']
        self.value[id] = value

#填充STDF中的时间属性
def _stdf_time_value():
    return int(time.time())


