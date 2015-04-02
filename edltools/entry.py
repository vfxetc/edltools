class Entry(object):

    def __init__(self, index=None, reel=None, channels=None, edit=None,
        src_in=None, src_out=None, dst_in=None, dst_out=None, meta=None,
        extra=None
    ):
        self.index = int(index) if index else None
        self.reel = reel
        self.channels = channels
        self.edit = edit
        self.src_in = src_in
        self.src_out = src_out
        self.dst_in = dst_in
        self.dst_out = dst_out
        self.meta = meta or {}
        self.extra = extra or []

    def __repr__(self):
        return '<edltools.Entry %03d %8s %s %s %s %s %s>' % (
            self.index or 0,
            self.reel,
            self.src_in,
            self.src_out,
            self.dst_in,
            self.dst_out,
            self.meta,
        )
