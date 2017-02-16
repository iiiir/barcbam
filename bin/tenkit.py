from string import maketrans

dna_to_decimal_dict = maketrans('ACGTacgt', '01230123')
def barcode_to_decimals(barcode):
    '''
    must be 16bp barcode
    Note: no "+ 1"
    '''
    chrom = int( barcode[0:3].translate( dna_to_decimal_dict ), 4)
    pos   = int( barcode[3:].translate( dna_to_decimal_dict ), 4) 
    return chrom,pos

