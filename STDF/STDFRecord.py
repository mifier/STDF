from io import BytesIO
import struct
import math
import copy
from STDF.RecordFile import Records,get_DataType_typelength,get_bit_val,set_bit_val,get_V_subtypecode,get_subtypecode_V
from STDF.Log import logger


class STDFError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
 

class STDFRecord:
    BinBuffer = b''
    type=''
    version = ''
    length=0
    
    def __init__(self, binarydata,type=None,version = 'V4'):
        self.BinBuffer = binarydata 
        # REC_TYP = int(self.BinBuffer[2])
        # REC_SUB = int(self.BinBuffer[3])  
        self.type=type
        self.version = version
        self.length=len(binarydata)
    @classmethod
    def decode(cls,STDFRecordcase):
        byIo = BytesIO(STDFRecordcase.BinBuffer)
        if Records.get(STDFRecordcase.type):
            record=Records[STDFRecordcase.type][1]()
        else:
            logger.warning('STDFRecord.type is not supported')
            return        
        byIo.max=STDFRecordcase.length
        def Bytes2Data(Type,Length):
            # 获取可变长度
            if Length is None:
                if  Type=='D':
                    Length=int.from_bytes(byIo.read(2), byteorder='big', signed=False)
                else:
                    Length=int.from_bytes(byIo.read(1), byteorder='big', signed=False)

            # 数据填入字典中
            if Type=='U':
                return int.from_bytes(byIo.read(Length), byteorder='big', signed=False)  
                # print(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(STDFRecordcase.body[body_key]['Value'])))
            elif Type=='I':
                return int.from_bytes(byIo.read(Length), byteorder='big', signed=True)
            elif Type=='C':
                return str(byIo.read(Length), encoding = "utf-8")
            elif Type=='R4':
                return struct.unpack('>f',byIo.read(Length))[0]
            elif Type=='R8':
                return struct.unpack('>d',byIo.read(Length))[0]
            elif Type=='B':
                temp=byIo.read(Length)
                return [get_bit_val(temp,x) for x in range(8*Length)]
            elif Type=='N':
                temp_1=byIo.read(1)
                lb = (0x0f & temp_1)
                return lb
            elif Type=='U*1':
                Length=record[record.fields[body_key]['Length']]
                temp=[]
                for i in range(Length):
                    temp.append(int.from_bytes(byIo.read(1), byteorder='big', signed=False)) 
                return temp
            elif Type=='U*2':
                Length=record[record.fields[body_key]['Length']]
                temp=[]
                for i in range(Length):
                    temp.append(int.from_bytes(byIo.read(2), byteorder='big', signed=False)) 
                return temp
            elif Type=='R*4':
                Length=record[record.fields[body_key]['Length']]
                temp=[]
                for i in range(Length):
                    temp.append( struct.unpack('>f',byIo.read(4))[0]) 
                return temp
            elif Type=='D':
                byte_Length= math.ceil(Length/8)
                temp_length=0
                temp_data=byIo.read(byte_Length)
                temp=[]
                for i in range(byte_Length):
                    temp_byte=temp_data[i]
                    temp_byte=int(temp_byte).to_bytes(length=1, byteorder='big', signed=False) 
                    for i in range(8):
                        if temp_length<Length:
                            temp_length+=temp_length
                            temp.append(get_bit_val(temp_byte,i))

                return temp

            elif Type=='V':
                Length=record[record.fields[body_key]['Length']]
                temp=[]
                for i in range(Length):
                    typecode=get_V_subtypecode(int.from_bytes(byIo.read(1), byteorder='big', signed=False))
                    (subType,subLength)=get_DataType_typelength(typecode) 
                    if subLength ==0:
                        temp_1=None
                    else:
                        temp_1=Bytes2Data(subType,subLength)
                    temp.append([typecode,temp_1])
                return temp
            elif Type=='N*1': 
                Length=record[record.fields[body_key]['Length']]
                temp=[]
                for i in range(Length):
                    if i%2==0:
                        temp_1=ord(byIo.read(1))
                        lb = (0x0f & temp_1)
                        temp.append(lb)
                    else:
                        hb=  (0xf0 & temp_1)>>4
                        temp.append(hb)
                return temp

                  
            else:
                raise ValueError("?")

        for body_key,body_value in record.fields.items():
            (Type,Length)=get_DataType_typelength(body_value['Type'])
            if byIo.max==byIo.tell():
                break
            else:
                record[body_key]=Bytes2Data(Type,Length)

        byIo.close()
        return record
    @classmethod    
    def encode(cls,Recordcase):
        byIo = BytesIO()
        # 'REC_LEN'
        # byIo.write(b'\x00\x00')
        # # 'REC_TYP'
        # data_1byte = int(Recordcase['record_type']).to_bytes(length=1, byteorder='big', signed=False)
        # byIo.write(data_1byte)
        # # 'REC_SUB' 
        # data_1byte = int(Recordcase['record_subtype']).to_bytes(length=1, byteorder='big', signed=False)
        # byIo.write(data_1byte)
        def Data2Bytes(Type,length,data):
            if Type=='U':
                if length is None:
                    temp_length=Data2Bytes('U',1,len(data))
                    return temp_length+int(data).to_bytes(length=length, byteorder='big', signed=False) 
                else:
                    return int(data).to_bytes(length=length, byteorder='big', signed=False) 
                # print(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(STDFRecordcase.body[body_key]['Value'])))
            elif Type=='I':
                return int(data).to_bytes(length=length, byteorder='big', signed=True) 
            elif Type=='C':
                if length is None:
                    temp_length=Data2Bytes('U',1,len(data))
                    return temp_length+bytes(data, encoding = "utf8")  
                else :
                    return bytes(data, encoding = "utf8")  
            elif Type=='R4':
                return struct.pack('>f',data)
            elif Type=='R8':
                return struct.pack('>d',data)
            elif Type=='N':
                temp=(0x0f & data)
                return temp
            elif Type=='B':
                dataLength=math.ceil(len(data)/8)
                temp_length=Data2Bytes('U',1,len(data))
                temp=b''
                temp_data=[int(0).to_bytes(length=1, byteorder='big', signed=False) for i in range(dataLength)]
                for i,bit in enumerate(data):
                    byteindex=i//8
                    bitindex=i%8
                    if bit:
                        temp_data[byteindex]=set_bit_val(temp_data[byteindex],bitindex,1)
                    else:
                        temp_data[byteindex]=set_bit_val(temp_data[byteindex],bitindex,0)
                for i in temp_data:
                    temp+=i
                if length is None:
                    return temp_length+temp
                else:
                    return temp
            elif Type=='U*1':
                dataLength=Recordcase[Recordcase.fields[body_key]['Length']]
                temp=b''
                for i in range(dataLength):
                    temp+=int(data[i]).to_bytes(length=length, byteorder='big', signed=True)
                return temp
            elif Type=='U*2':
                dataLength=Recordcase[Recordcase.fields[body_key]['Length']]
                temp=b''
                for i in range(dataLength):
                    temp+=int(data[i]).to_bytes(length=length, byteorder='big', signed=True) 
                return temp
            elif Type=='R*4':
                dataLength=Recordcase[Recordcase.fields[body_key]['Length']]
                temp=b''
                for i in range(dataLength):
                    temp+= struct.pack('>f',data[i])
                return temp
            elif Type=='D':
                dataLength=math.ceil(len(data)/8)
                temp_length=Data2Bytes('U',2,len(data))
                temp=b''
                temp_data=[int(0).to_bytes(length=1, byteorder='big', signed=False) for i in range(dataLength)]
                for i,bit in enumerate(data):
                    byteindex=i//8
                    bitindex=i%8
                    if bit:
                        temp_data[byteindex]=set_bit_val(temp_data[byteindex],bitindex,1)
                    else:
                        temp_data[byteindex]=set_bit_val(temp_data[byteindex],bitindex,0)
                for i in temp_data:
                    temp+=i
                
                return temp_length+temp
 
            elif Type=='V':
                # dataCnt=Recordcase.body[Recordcase.body[body_key]['Length']]['Value']
                temp=b''
                for item in data:
                    (subType,subLength)=get_DataType_typelength(item[0])
                    temp1=get_subtypecode_V(item[0])
                    temp1=int(temp1).to_bytes(length=1, byteorder='big', signed=True)
                    temp2=Data2Bytes(subType,subLength,item[1])
                    temp=temp+temp1+temp2
                return temp
            elif Type=='N*1': 
                # Length=Recordcase.body[Recordcase.body[body_key]['Length']]['Value']
                temp=b''
                for i,item in enumerate(data):
                    if i%2==0:
                        temp_1=(0x0f & item)
                    else:
                        temp_1=temp_1 &(item<<4)
                        temp=temp+int(temp_1).to_bytes(length=1, byteorder='big', signed=True)
                return temp
        # 获取record，body的有效属性数
        for i,body_value in enumerate(Recordcase.value):
            if  body_value is not None:
                body_length=i+1
        temp_length=0
        for body_key,body_value in Recordcase.fields.items():
            if temp_length<body_length:
                temp_length+=1
                (DataType,typelength)=get_DataType_typelength(body_value['Type'])
                data=Recordcase[body_key]
                if data is None:
                    byte=Data2Bytes(DataType,typelength,body_value['Missing'])
                else:
                    byte=Data2Bytes(DataType,typelength,data)
                # print(data)
                byIo.write(byte)
            else:
                break
        length=byIo.tell()-4
        length=int(length).to_bytes(length=2, byteorder='big', signed=True)
        byIo.seek(0)
        byIo.write(length)
        BinData=byIo.getvalue()
        byIo.close()
        return cls(BinData,type=Recordcase.type)


def get_RecordType(REC_TYP,REC_SUB):
    for key,item in Records.items():
        if(REC_TYP,REC_SUB)==item[0]:
            return key
