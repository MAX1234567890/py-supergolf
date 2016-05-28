## Py-supergolf.py

import sys, base64, codecs


with open(sys.argv[1]) as data_stream:
    exec(
        base64.a85decode(
                codecs.decode(
                    codecs.decode(
                        ''.join(data_stream.readlines()),
                        'zip'
                    ),
                    'bz2'
                )
            )
        )
    )
