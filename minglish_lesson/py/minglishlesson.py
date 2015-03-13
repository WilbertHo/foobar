"""
Minglish lesson
===============

Welcome to the lab, minion. Henceforth you shall do the bidding of
Professor Boolean. Some say he's mad, trying to develop a zombie serum and
all... but we think he's brilliant! 

First things first - Minions don't speak English, we speak Minglish. Use
the Minglish dictionary to learn! The first thing you'll learn is how to
use the dictionary.

Open the dictionary. Read the page numbers, figure out which pages come
before others. You recognize the same letters used in English, but the
order of letters is completely different in Minglish than English (a < b <
c < ...).

Given a sorted list of dictionary words (you know they are sorted because
you can read the page numbers), can you find the alphabetical order of the
Minglish alphabet? For example, if the words were ["z", "yx", "yz"] the
alphabetical order would be "xzy," which means x < z < y. The first two
words tell you that z < y, and the last two words tell you that x < z.

Write a function answer(words) which, given a list of words sorted
alphabetically in the Minglish alphabet, outputs a string that contains
each letter present in the list of words exactly once; the order of the
letters in the output must follow the order of letters in the Minglish
alphabet. 

The list will contain at least 1 and no more than 50 words, and each word
will consist of at least 1 and no more than 50 lowercase letters [a-z]. It
is guaranteed that a total ordering can be developed from the input
provided (i.e. given any two distinct letters, you can tell which is
greater), and so the answer will exist and be unique.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string list) words = ["y", "z", "xy"]
Output:
    (string) "yzx"

Inputs:
    (string list) words = ["ba", "ab", "cb"]
Output:
    (string) "bac"
"""
from itertools import islice
from collections import deque


class DAG(object):
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, key):
        self.vertices.update({key: Vertex(key)})

    def __getitem__(self, val):
        return self.vertices.get(val, None)

    def iteritems(self):
        return self.vertices.iteritems()

    def get(self, val):
        return self.__getitem__(val)


class Vertex(object):
    def __init__(self, key=None):
        self.key = key
        self.neighbors = list()

    def add_neighbor(self, edge):
        self.neighbor.append(edge)

    # def __repr__(self):
    #     return "{neighbors}".format(
    #             neighbors=', '.join(map(str, self.neighbors)))


def answer(words):
    """ Given a sorted list of words, output the corresponding alphabet.

        ["ba", "ab", "cb"]
        Sliding window of 2 over the list:
        (ba, ab) : '' + b, '' + a, create A, B vertexes, edge B -> A
        (ab, cb) : '' + a, '' + c, create C vertex, edge A -> C
        B -> A (B < A), A -> C (A < C) == BAC

        [C, CAC, CB, BCC, BA]
        (C, CAC) : '' + C, '' + C, create C and A vertexes
        (CAC, CB) : C + A, C + B, create B vertex, edge A -> B (A < B)
        (CB, BCC) : '' + C, '' + B, edge C -> B (C < B)
        (BCC, BA) : B + C, B + A, edge C -> A (C < A)

        C < A, A < B, C < B == CAB
    """
    return topological_sort(construct_graph(words))


def construct_graph(words):
    graph = DAG()

    for a, b in zip(*(islice(words, i, None) for i in range(2))):
        for letter in set(list(a) + list(b)):
            if not graph[letter]:
                graph.add_vertex(letter)

        vertex, neighbor = get_neighbor(a, b)
        if vertex and neighbor:
            graph[vertex].neighbors.append(neighbor)

    return graph


def get_neighbor(a, b):
    """ Parse a pair of words and return the edge, if it exists

        Reduce the two words to a length equal to the shortest of
        the two, then search for the first non-matching character,
        if one exists.

        Ex: 'C', 'CAC' --> max length 1, 'C', 'CAC'[:1]
        'C' <-> 'C', no non-matching tokens

        'CAC', 'CB' --> max length 2, 'CAC'[:2], 'CB'
        'CA' <-> 'CB', 'A' will be connected to 'B'.
    """
    max_length = min(map(len, [a, b]))   
    for _a, _b in zip(a[:max_length], b[:max_length]):
        if _a != _b:
            return _a, _b

    return None, None


def topological_sort(graph):
    def visit(node):
        if node in temp:
            raise Exception("Not a directed acyclic graph.")
        if node not in visited:
            temp.add(node)
            for neighbor in graph[node].neighbors:
                visit(neighbor)
            visited.add(node)
            temp.remove(node)
            alphabet.appendleft(node)

    alphabet = deque()
    temp = set()
    visited = set()

    for node, neighbors in graph.iteritems():
        if node not in visited:
            visit(node)

    return ''.join(list(alphabet))


def main():
    print answer(['c', 'cac', 'cb', 'bcc', 'ba'])
    print answer("y, z, xy".split(', '))
    print answer("ba, ab, cb".split(', '))


if __name__ == '__main__':
    main()
