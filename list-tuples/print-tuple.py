import operator

PEOPLE = [('Tim', 'Tebow', 7.85),
          ('Peyton', 'Manning', 3.626),
          ('Russell', 'Wilson', 10.603)]


def format_sort_records(list_of_tuples):
    output = []
    template = "{1:10} {0:10} {2:5.2f}"
    for person in sorted(list_of_tuples,
                         key=operator.itemgetter(1, 0)):
        output.append(template.format(*person))
    return output


print('\n'.join(format_sort_records(PEOPLE)))
