from django import template

register = template.Library()


def get_chunks(array, evenly_by):
    for i in range(0, len(array), evenly_by):
        yield array[i:i + evenly_by]


register.filter('get_chunks', get_chunks)
