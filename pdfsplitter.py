#import
from PyPDF2 import PdfFileReader, PdfFileWriter


#function
def cropper(start,end,file):

    inputPdf = PdfFileReader(open(file,'rb'))
    outputPdf = PdfFileWriter()

    ostream = open(file.split('.')[0] + 'cropped' + '.pdf' , 'wb')

    while start <= end:
        outputPdf.addPage(inputPdf.getPage(start))

        outputPdf.write(ostream)

        start+=1

    ostream.close()

#--------to run the code use----- >
cropper(1,4,'sample.pdf')
