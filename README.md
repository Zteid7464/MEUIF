# The MEUIF (Minimal Easy to Use Image Format) image format. It's header is only 13 Bytes long. In the moment there is no compression
# but im planning on adding some later.

| The structure of a MEUIF file:                                             |
| The first 5 bytes are just MEUIF in ASCII. <br>                            |
| Four bytes for the total size of the image file. <br>                      |
| Two bytes for the width, and two bytes for the height of the image. <br>   |
| The Pixel data <br>                                                        |