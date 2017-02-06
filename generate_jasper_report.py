#!/usr/bin/env python

image_code_snippet = """
<image hAlign="Center">
<reportElement mode="Opaque" x="{}" y="{}" width="{}" height="{}"/>
<imageExpression><![CDATA[$P{watermark}]]></imageExpression>
</image>
"""

starting_x = 10
starting_y = 10
img_width = 100
img_height = 100
watermark_width = 553
watermark_height = 726
interval_width = 10
interval_height = 10

def get_next_x(current_x):
    return current_x + img_width + interval_width

def get_next_y(current_y):
    return current_x + img_height + interval_width
