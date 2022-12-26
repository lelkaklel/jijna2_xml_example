#!/usr/bin/env python3
# coding: utf-8

from jinja2 import Environment, FileSystemLoader, select_autoescape
from csv import DictReader
# open file in read mod

def parse(filename):
    data = []
    with open(filename, 'r') as f:
        dict_reader = DictReader(f)
        data = list(dict_reader)
    return data


def generate(file_out, file_template, data):
    env = Environment(
        loader = FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml']),
        trim_blocks=True,
        lstrip_blocks=True
    )
    template = env.get_template('template.xml')
    with open(file_out, 'w+') as f:
        for row in template.generate(data=data):
            f.write(row)



def main():
    data = {}
    data['counteragents'] = parse('counteragents.csv')
    data['sku'] = parse('sku.csv')
    data['units'] = parse('units.csv')
    generate('result.xml', 'template.xml', data)

if __name__ == '__main__':
    main()
