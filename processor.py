#!/usr/bin/env python
# coding: utf-8

BACKPRINT_LINE_1 = 'folder-to-AUTPRINT'
BACKPRINT_LINE_2 = '...'

DIR_INPUT = 'input'
DIR_OUTPUT = 'output'
DIR_TMP = 'tmp'

import os
import random

from datetime import date, datetime

order_count = 0

input_dir = os.path.join(os.getcwd(), DIR_INPUT)
output_dir = os.path.join(os.getcwd(), DIR_OUTPUT)
tmp_dir = os.path.join(os.getcwd(), DIR_TMP)

d_files = []

# browse 'input_dir', process all files - non printable
# files are not expected in this folder.

# at the moment - only IMG_NNNN.jpg files are expected. It would probably
# be a great idea to add a RE filter on filenames

for file_path in os.listdir(input_dir):
    file_nitems = file_path.split('-')
    dpof_line1 = "{} {}".format(file_nitems[0], BACKPRINT_LINE_1)
    dpof_line2 = "{} {}-{:02d}-{:02d}".format(BACKPRINT_LINE_2,
                                              date.today().year,
                                              date.today().month,
                                              date.today().day)

    d_files.append({
        'file_name': file_path,
        'dpof_line1': dpof_line1,
        'dpof_line2': dpof_line2
    })

# creates an AUTMARK.MRK file following an exemple extracted
# from an actual order - renames files to avoid utf-8 issues on
# the printer

if d_files:

    timestamp_str = datetime.now()
    buffer_dpof = """[HDR]
GEN REV = 01.00
GEN CRT = "NORITSU KOKI"-01.00
GEN DTM = {:4d}:{:02d}:{:02d}:{:02d}:{:02d}:{:02d}
VUQ RGN = BGN
VUQ VNM = "NORITSU KOKI" -ATR "QSSPrint"
VUQ VER = 01.00
PRT PSL = NML -PSIZE "4x6"
PRT PCH = 100
GEN INP = "Other"
VUQ RGN = END""".format(timestamp_str.year,
                        timestamp_str.month,
                        timestamp_str.day,
                        timestamp_str.hour,
                        timestamp_str.minute,
                        timestamp_str.second)

    order_ref = '{:02d}{:05d}'.format(order_count, random.randint(1, 99999))
    order_dir = os.path.join(tmp_dir, 'tmp-{}'.format(order_ref))
    image_dir = os.path.join(order_dir, 'IMAGE')
    misc_dir = os.path.join(order_dir, 'MISC')

    count_files = 1

    os.mkdir(order_dir)
    os.mkdir(image_dir)
    os.mkdir(misc_dir)

    for filer in d_files:
        file_renamed = u'{}_{}.{}'.format(order_ref,
                                          count_files,
                                          filer['file_name'].split('.')[1])

        os.rename(os.path.join(input_dir, u'{}'.format(filer['file_name'])),
                  os.path.join(image_dir, file_renamed))

        buffer_dpof += """

[Job]
PRT PID = {:03d}
PRT TYP = STD
PRT QTY = 001
IMG FMT = EXIF2 -J
<IMG SRC = "..\IMAGE\{}">
VUQ RGN = BGN
VUQ VNM = "NORITSU KOKI" -ATR "QSSPrint"
VUQ VER = 01.00
PRT CVP1 = 1 -STR "{}"
PRT CVP2 = 1 -STR "{}"
VUQ RGN = END""".format(count_files,
                        file_renamed,
                        filer['dpof_line1'],
                        filer['dpof_line2'])

        count_files += 1

    f = open(os.path.join(misc_dir, 'AUTPRINT.MRK'), 'w')
    f.write(buffer_dpof)
    f.close()

    os.rename(os.path.join(tmp_dir, 'tmp-{}'.format(order_ref)),
              os.path.join(output_dir, 'o{}'.format(order_ref)))

    order_count += 1
