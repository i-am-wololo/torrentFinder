
# Streams will be represented by an array of dictionaries with their quality and how much seeds they have

anime = ['nyaa']
movies = ['yts', 'leetxx']


qualities = ['720p', '480p', '1080p']

def sort_by_seed(array):
    return sorted(array, key=itemgetter('seed'))


def sort_by_quality(array):
    pass



def guess_quality(title):
    for i in qualities:
        if title.find(i)!= -1:
            return i

