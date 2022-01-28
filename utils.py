
# Streams will be represented by an array of dictionaries with their quality and how much seeds they have




def sort_by_seed(array):
    return sorted(array, key=itemgetter('seed'))


def sort_by_quality(array):
    pass
