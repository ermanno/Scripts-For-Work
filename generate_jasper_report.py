#!/usr/bin/env python

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

image_code_snippet = """
<image hAlign="Center">
<reportElement mode="Opaque" x="{}" y="{}" width="{}" height="{}"/>
<imageExpression><![CDATA[$P{{watermark}}]]></imageExpression>
</image>
"""

current_x = 0
current_y = 0
img_width = 50
img_height = 50

## -- data for portrait
buffer_x = 1
buffer_y = 0
watermark_width = 553
watermark_height = 726

## -- data for landscape
# buffer_x = 0
# buffer_y = 3
# watermark_width = 800
# watermark_height = 479

watermark_width_no_borders = watermark_width - 2 * current_x
watermark_height_no_borders = watermark_height - 2 * current_y
num_of_columns = watermark_width_no_borders / img_width
num_of_rows = watermark_height_no_borders / img_height
interval_width = (watermark_width_no_borders - img_width * num_of_columns) / (num_of_columns - 1)
interval_height = (watermark_height_no_borders - img_height * num_of_rows) / (num_of_rows - 1)

logger.info('Watermark width no borders = {}'.format(watermark_width - 2 * current_x))
logger.info('Watermark height no borders = {}'.format(watermark_height - 2 * current_y))
logger.info('Number of columns = {}'.format(watermark_width_no_borders / img_width))
logger.info('Number of rows = {}'.format(watermark_height_no_borders / img_height))
logger.info('Interval width = {}'.format((watermark_width_no_borders - img_width * num_of_columns) / (num_of_columns - 1)))
logger.info('Interval height = {}'.format((watermark_height_no_borders - img_height * num_of_rows) / (num_of_rows - 1)))

def next_y(y):
    return y + img_height + interval_height

def next_x(x):
    return x + img_width + interval_width

def print_column(x, y):
    while y + img_height <= watermark_height_no_borders:
        print image_code_snippet.format(x, y, img_width, img_height)
        y = next_y(y)
        logger.info('y: {}; test y: {}'.format(y, y + img_width))
        
def print_jasper_code(x, y):
    while x + img_width <= watermark_width_no_borders:
        print_column(x, y)
        x = next_x(x)
        logger.info('x: {}; test x: {}'.format(x, x + img_width))

def main():
    print_jasper_code(current_x + buffer_x, current_y + buffer_y)

if __name__ == '__main__':
    main()
