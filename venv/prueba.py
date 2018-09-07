import xml.etree.ElementTree as ET
from operator import is_not
from functools import partial
import zlib
import base64
import urllib.parse

def urlencode(str):
  return urllib.parse.quote(str)


def urldecode(str):
  return urllib.parse.unquote(str)

#from urllib.parse import unquote

def decode_base64_and_inflate( b64string ):
    decoded_data = base64.b64decode( b64string )
    return zlib.decompress( decoded_data , -15)


def deflate_and_base64_encode( string_val ):
    zlibbed_str = zlib.compress( string_val )
    compressed_string = zlibbed_str[2:-4]
    return base64.b64encode( compressed_string )


#matrimonio = open ('Matrimonio.xml', "rb")
#tree = ET.parse( matrimonio )
tree = ET.parse( 'Matrimonio.xml' )
root = tree.getroot()

xml_codificado= root[0].text
print ( xml_codificado )
#byte_texto= bytes(xml_codificado , 'ascii')

#xml_codificado.text.encode
result64= base64.b64decode( xml_codificado )
result_data = zlib.decompress( result64 , -15)
print ("Inflate")
print ( result_data )
sin_b = result_data.decode( 'utf-8' )
print ( sin_b )

matrimonio = urldecode( sin_b )

print (matrimonio)

#tree2 = ET.parse( matri.xml )
#root = tree2.getroot()


#f = open ('matri.xml' , 'w' ) NO BORRAR
#f.write(matrimonio) NO BORRAR
#f.close()  NO BORRAR

#decoded_data = decode_base64_and_inflate(contenido)
#zlib.decompress(decoded_data, -15)


#archivo=open("Matrimonio.xml","rb")
#contenido=archivo.read()
#contenido= '7Zldb9owFIZ/TS43JTEEeglp1iEBQcC09moyiRu8hRg5boH9+h1jJ+SDr6rVQKJCQvFrn2P7nMeODQZyF+sHjpfzAQtJbNhmuDbQvWHb7SaCbylslNBAbSVEnIZKsnbChP4lWjS1+kJDkpYaCsZiQZdlMWBJQgJR0jDnbFVu9szicq9LHJGaMAlwXFd/0lDM9bTs1k7/Tmg0z3q2nDtVs8BZYz2TdI5DtipIyDOQyxkT6mmxdkksY5fFRdl9O1CbD4yTROwxYLPfMh62GeMZpGTbYNCZjnsDf9jzlbHX9wbecOqrWtcfut5oquuyflrt9qxlERxghBwHmV+sfOz5mFKxyeLF2UsSEmlrGqi7mlNBJkscyNoVAALaXCzkcCx4TAVnf/K4SiXiOKQwIZfFjIOWsARMu6+ECwpJ6cQ0SkAWTHqCnAtME8K18TOUNUGW7B3r1gE4lI26ambSGVkfjGJxfg+ELYjgG2iiDew2+tpURppoq6UTvNrxYSGtzQtsNLSGNZJR7jzvbwwpw0kEwcw7bDhmqbvGnu6aZ/SGY4hBggXpygylRVTgoTDVnbTNblbUPB1ka9rzhp5hOzG06c44PEUiD3kZtLHX77g9f/jLm0zHP9zpj3GnfwI6+0zorNPQYR5oSJrmWxj8H3Qhq8KWXU+206on2z6CVinLb0rpvT/oub3+u3aLxk3vFpZZWbyfWwV48yYjf9J5B1TNm4aq/gr6xCrHyj/vFXQmaM5Ng1ZL/CdmW297cfIe4URzAqfWUZxIEnbkjUVmMcZpSoNjBIGjLlhoBu5kfXbBkDw80zjOwDJs1L2Xnz3ckDUVj9IGthRVetIeABK+KVTJ4pMeiponCWt3pwpaMD/2wgNyIB7ZhQ7ziIgzTn4FRE9AkWmcxFjQ1/Iwj3A5YjQRh9/ftYOWmp62Kt7WKo5yw0OOVAxqji5NbPuKiS3yukNUEdtoOFVmt4UR4RRiud1GzY8D2T4D5OJJ+PIgo48CueroAMjACd4Umi1lg/TIgJvtUj8WsirrQnm8ilVyd8Wr5BL7+jnLoXiGv73lcGliLdO4WmStYxv7JZEt3gZuD9m37uBNu/Jb1ofu4FDc/XSurHf/PyDvHw'
#print (contenido)
#decode_base64_and_inflate(contenido)
#decoded_data = base64.b64decode(contenido)
#print (decoded_data)

#zlib.compressobj( decoded_data )
#print ("Hola")

#decode_base64_and_inflate( contenido )
print( "DESPUES DE LA DECODIFICACIÓN Y CREACIÓN DEL NUEVO XML")
e = ET.parse('matri.xml').getroot()
i = 0
k = 0
origen = [ ]
destino = [ ]
verdad= bool;


for atype in e.findall('root'):
    for mxCell in e.iter('mxCell'):
        # print(mxCell.get('target')
        if mxCell.get('target') is not None:
            destino = destino + [mxCell.get('target')]
        if mxCell.get('source') is not None:
            origen = origen + [mxCell.get('source')]
    for x in range (len(destino)):
        for cell in atype.findall('object'):
            if (origen[x] == cell.get('id')):
                print('Origen: ', cell.get('label'))
        for cell in atype.findall('object'):
            if (destino[x] == cell.get('id')):
                print('Destino :', cell.get('label'))
