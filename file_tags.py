import re


def get_tags( matched_file ):
    with open( matched_file, "rb" ) as imageFile:
        d = imageFile.read()
        # xmp_start = d.find(b'<x:xmpmeta')
        xmp_start = d.find( b'<MicrosoftPhoto:LastKeywordXMP>' )
        # xmp_end = d.find(b'</x:xmpmeta')
        end_token = b'</MicrosoftPhoto:LastKeywordXMP>'
        xmp_end = d.find( end_token )
        if xmp_start is not -1 and xmp_end is not -1:
            xmp_str = d[ xmp_start:xmp_end + len( end_token ) ]
            return re.findall( b'(?s)(?<=<rdf:li>).*?(?=</rdf:li>)', xmp_str )
        else:
            return None