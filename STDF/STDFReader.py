
from STDF import Records,STDFError,STDFRecord
from STDF.STDFRecord import get_RecordType
from STDF.Log import logger
class STDFReader:
    """this class is used for reading STDF file"""
    HEADER_SIZE = 4
    STDF_version = 'V4'

    def __init__(self,FilePath):
        self.fp=open(FilePath, mode='rb')
        logger.info('open file path: %s'%FilePath)
        temp=self.fp.read(self.HEADER_SIZE)   
        if  temp[2:] != b'\x00\x0a':
           raise STDFError("File is not a STDF file!") 
        self.fp.seek(5) 
        temp=int.from_bytes(self.fp.read(1), byteorder='big', signed=False)
        if temp==4:
           self.STDF_version = 'V4'
           logger.info('STDF Version is V4')
        elif temp==3:
            self.STDF_version = 'V3'
        else:
            logger.warn('Unknown STDF version')
        self.fp.seek(0)

           
       

    def read_record(self):
        head=self.fp.read(self.HEADER_SIZE)
        if len(head)==0:
            logger.info('End of reading')
            
            return
        elif len(head)<4:
            logger.error('record error at %s'%self.fp.tell())
            raise STDFError('file error  at %s'%self.fp.tell())

        REC_LEN = int.from_bytes(head[:2], byteorder='big', signed=False)
        REC_TYP = int(head[2])
        REC_SUB = int(head[3])        
        body = self.fp.read(REC_LEN)
        record=get_RecordType(REC_TYP,REC_SUB)
        if record is  None:
            logger.error('record error at %s'%self.fp.tell())
            raise STDFError('record error at %s'%self.fp.tell())
        return STDFRecord(binarydata=head+body,type=record)

    def __iter__(self):
        return self

    def __next__(self):
        r = self.read_record()
        if r: 
            return r
        else:
            raise StopIteration


    

        
       

 

