
import STDF

from STDF import STDFReader,STDFRecord,STDFWriter

from STDF import Records


# stdf=STDFReader('./STDF/data/a595.stdf')
stdf=STDFReader('./STDF/data/demofile.stdf')
temp_stdf=STDFWriter('./STDF/data/1.stdf')
temp_list=[]
# for i in stdf:
#     a=STDFRecord.decode(i)
#     print(a)
#     print(i.decode)
for i in stdf:
    i1=i
    temp_stdf.write(i1)
    a1=STDFRecord.decode(i1)
    i2=STDFRecord.encode(a1)
    if i1.type=='PLR':
        temp_list.append(a1)
        a1=STDFRecord.decode(i1)
        # print(i1)
    # if i1.BinBuffer!=i2.BinBuffer:
    #    pass 
temp_stdf.close()
from STDF import Records