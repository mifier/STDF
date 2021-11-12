import os
import sys
from STDF.Log import logger
import pkgutil
import inspect
from STDF.RecordFile.Record import RecordBase,get_DataType_typelength,get_bit_val,set_bit_val,get_V_subtypecode,get_subtypecode_V
pkgpath = os.path.dirname(__file__)
pkgname = os.path.basename(pkgpath)
sys.path.append(pkgpath)
Records=dict()

for _, file, _ in pkgutil.iter_modules([pkgpath]):
    module=__import__(file)
    classes = inspect.getmembers(module, inspect.isclass)
    for item in classes:
        class_name, class_var = item
        if issubclass(class_var,RecordBase):
            REC_TYP = class_var.fields['record_type']['Value']
            REC_SUB = class_var.fields['record_subtype']['Value']
            for TYP,classvar in Records.values():
                if TYP ==(REC_TYP,REC_SUB) and (REC_TYP,REC_SUB)!=(0,0):
                    logger.error('At RecordFile %s ang %s have same (REC_TYP,REC_SUB) -( %s,%s)'%(classvar,class_var,REC_TYP,REC_SUB)) 
            

            Records.update({class_name:[(REC_TYP,REC_SUB),class_var]})

       
pass

 # 判断从基类继承