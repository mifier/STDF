from io import BytesIO
from STDF.STDFRecord import STDFRecord
from STDF.Log import logger
import struct
import os
class STDFWriter:
    """this class is used for writting STDF file"""    
    STDF_version = 'V4'
    def __init__(self,FilePath):
        self.FilePath=FilePath
        self.fp=open(FilePath, mode='wb')
        logger.info('Write file path: %s'%FilePath)
        self.cnt_record=0


    def write(self,STDFrecord):
        if isinstance(STDFrecord,STDFRecord):
            bytes=STDFrecord.BinBuffer
            self.fp.write(bytes)
            self.cnt_record+=1
        else:
            print('Write can only be used for STDFRecord Class')

    def close(self):
        self.fp.close()
        Filename=os.path.basename(self.FilePath)
        logger.info('The total number of records written to %s is %s'%(Filename,self.cnt_record))