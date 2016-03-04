# folder-to-AUTPRINT

AUTPRINT.MRK python portable generator (for Noritsu QSS DPOF and others)

This small piece of software as been designed a quick and dirty
way to convert a bunch of pics sitting in a folder into a Nortisu QSS
printer compatible order.

## Dependencies

This software has been designed to rely only on the Python standard
library. It has been tested with Python 2.7 on MacOS X and Windows.

As stated before : it was a quick and dirty way to resolve a small
issue and it needs lots of improvements. Please submit pull-requests.

## File paths

Sample file hierarchy :

```
.
./input
./input/IMG_1689.jpg
./input/IMG_1690.jpg
./input/IMG_1691.jpg
./input/IMG_1692.jpg
./input/IMG_1693.jpg
./input/IMG_1695.jpg
./input/IMG_1696.jpg
./input/IMG_1697.jpg
./output
./processor.py
./README.md
./tmp
```

After running the script :

```
.
./input
./output
./output/o0050800
./output/o0050800/IMAGE
./output/o0050800/IMAGE/0050800_1.jpg
./output/o0050800/IMAGE/0050800_2.jpg
./output/o0050800/IMAGE/0050800_3.jpg
./output/o0050800/IMAGE/0050800_4.jpg
./output/o0050800/IMAGE/0050800_5.jpg
./output/o0050800/IMAGE/0050800_6.jpg
./output/o0050800/IMAGE/0050800_7.jpg
./output/o0050800/IMAGE/0050800_8.jpg
./output/o0050800/MISC
./output/o0050800/MISC/AUTPRINT.MRK
./processor.py
./README.md
./tmp
```

## Licence

Copyright (c) 2016 Florian Le Goff

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
