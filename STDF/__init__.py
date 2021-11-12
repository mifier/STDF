"""
STDF package for Python. 
Include the following \n
logger :The log will appear in the log file of the current directory\n
Records :This variable contains all records in the RecordFile directory\n
STDFRecord :Used to decode or encode records\n
STDFReader,STDFWriter :Working with STDF files\n
partrecord :A class for one Part\'s all records\n
STDFError 
"""
from .Log import get_logger,logger

from .RecordFile import Records
from .STDFRecord import STDFError,STDFRecord
from .STDFReader import STDFReader
from .STDFWriter import STDFWriter



