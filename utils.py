
# Streams will be represented by an array of dictionaries with their quality and how much seeds they have

anime = ['nyaa']
movies = ['yts', 'leetxx']


qualities = ['720p', '480p', '1080p', '2160p']


# def sort_by_seed(array):
#     return sorted(array, key=itemgetter('seed'))


def sort_by_seed(result):

    result = sorted(result, key=lambda d: d['magnet']['seed'], reverse=True)
    return result


def guess_quality(title):
    for i in qualities:
        if title.find(i)!= -1:
            return i

