#!/usr/bin/env python

image_code_snippet = """
<image hAlign="Center">
<reportElement mode="Opaque" x="{}" y="{}" width="{}" height="{}"/>
<imageExpression><![CDATA[$P{{watermark}}]]></imageExpression>
</image>
"""

current_x = 2
current_y = 2
buffer_x = 2
buffer_y = 4
img_width = 50
img_height = 50
watermark_width = 553
watermark_height = 726

watermark_width_no_borders = watermark_width - 2 * current_x
watermark_height_no_borders = watermark_height - 2 * current_y
num_of_columns = watermark_width_no_borders / img_width
num_of_rows = watermark_height_no_borders / img_height
interval_width = (watermark_width_no_borders - img_width * num_of_columns) / (num_of_columns - 1)
interval_height = (watermark_height_no_borders - img_height * num_of_rows) / (num_of_rows - 1)

def next_y(y):
    return y + img_height + interval_height

def next_x(x):
    return x + img_width + interval_width

def print_column(x, y):
    while y + img_height <= watermark_height_no_borders:
        print image_code_snippet.format(x, y, img_width, img_height)
        y = next_y(y)

def print_jasper_code(x, y):
    while x + img_width <= watermark_width_no_borders:
        print_column(x, y)
        x = next_x(x)
        # print 'x: {}'.format(x)
        # print 'sum: {}'.format(x + img_width)

def main():
    print_jasper_code(current_x + buffer_x, current_y + buffer_y)

if __name__ == '__main__':
    main()
