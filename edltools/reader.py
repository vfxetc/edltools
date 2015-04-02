import re

from edltools.entry import Entry


class Reader(object):

    def __init__(self, source):
        self.source = source
        self._parse_headers()

    def _parse_headers(self):
        self.headers = {}
        for line in self.source:
            line = line.strip()
            if line:
                key, value = line.split(':', 1)
                self.headers[key.strip().upper()] = value.strip()
            else:
                break

    def __iter__(self):
        return self

    def next(self):

        line = next(self.source)
        m = re.match(r'''
            (\d+)\s+ # index
            (\w+)\s+ # reel
            (\w+)\s+ # channels
            (\w+)\s+ # edit
            (\d\d:\d\d:\d\d:\d\d)\s+ # src in
            (\d\d:\d\d:\d\d:\d\d)\s+ # src out
            (\d\d:\d\d:\d\d:\d\d)\s+ # dst in
            (\d\d:\d\d:\d\d:\d\d)\s+ # dst out
        ''', line, re.VERBOSE)

        if not m:
            raise StopIteration()

        entry = Entry(*m.groups())

        for line in self.source:
            line = line.strip()
            if not line:
                break

            if line.startswith('*'):
                key, value = line[1:].split(':', 1)
                entry.meta[key.strip().upper()] = value.strip()
                continue

            entry.extra.append(line)

        return entry


if __name__ == '__main__':

    import sys

    reader = Reader(sys.stdin)
    for entry in reader:
        if entry.meta.get('FROM CLIP NAME', '').endswith('R3D'):
            print entry

