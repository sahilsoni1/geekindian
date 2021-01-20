import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-s', action='store', dest='simple_value',
                    help='Store a simple value')

parser.add_argument('-c', action='store_const', dest='constant_value',
                    const='value-to-store',
                    help='Store a constant value')

parser.add_argument('-t', action='store_true', default=False,
                    dest='boolean_switch',
                    help='Set a switch to true')
parser.add_argument('-f', action='store_false', default=False,
                    dest='boolean_switch',
                    help='Set a switch to false')

parser.add_argument('-a', action='append', dest='collection',
                    default=[],
                    help='Add repeated values to a list',
                    )
parser.add_argument('-v', action='count', default=0,dest='counts',
                    help='counts the number of times a keyword argument occurs'
                    )

parser.add_argument('-A', action='append_const', dest='const_collection',
                    const='value-2-to-append',
                    help='Add different values to list')

parser.add_argument('--version', action='version', version='%(prog)s 1.0')

results = parser.parse_args()
print( 'simple_value     =', results.simple_value)
print( 'constant_value   =', results.constant_value)
print( 'boolean_switch   =', results.boolean_switch)
print( 'collection       =', results.collection)
print('const_collection =', results.const_collection)
print('counts =', results.counts)
