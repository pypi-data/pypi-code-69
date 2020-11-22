from warnings import *

from .containers import *
from .events import *
from struct import unpack, pack
from .constants import *
from .util import *


class FileReader(object):
    def read(self, midifile):
        pattern = self.parse_file_header(midifile)
        for track in pattern:
            self.parse_track(midifile, track)
        return pattern

    def parse_file_header(self, midifile):
        # First four bytes are MIDI header
        magic = midifile.read(4)
        if magic != b"MThd":
            raise TypeError("Bad header in MIDI file.")
        # next four bytes are header size
        # next two bytes specify the format version
        # next two bytes specify the number of tracks
        # next two bytes specify the resolution/PPQ/Parts Per Quarter
        # (in other words, how many ticks per quater note)
        data = unpack(">LHHH", midifile.read(10))
        hdrsz = data[0]
        format = data[1]
        tracks = [Track() for x in range(data[2])]
        resolution = data[3]
        # XXX: the assumption is that any remaining bytes
        # in the header are padding
        if hdrsz > DEFAULT_MIDI_HEADER_SIZE:
            midifile.read(hdrsz - DEFAULT_MIDI_HEADER_SIZE)
        return Pattern(tracks=tracks, resolution=resolution, format=format)

    def parse_track_header(self, midifile):
        # First four bytes are Track header
        magic = midifile.read(4)
        if magic != b"MTrk":
            raise TypeError("Bad track header in MIDI file: " + magic)
        # next four bytes are track size
        tracksize = unpack(">L", midifile.read(4))[0]
        return tracksize

    def parse_track(self, midifile, track):
        self.RunningStatus = None
        tracksize = self.parse_track_header(midifile)
        trackdata = iter(midifile.read(tracksize))
        while True:
            try:
                event = self.parse_midi_event(trackdata)
                track.append(event)
            except StopIteration:
                break

    def parse_midi_event(self, trackdata):
        # first datum is varlen representing delta-time
        tick = read_varlen(trackdata)
        # next byte is status message
        stsmsg = next(trackdata)
        # is the event a MetaEvent?
        if MetaEvent.is_event(stsmsg):
            cmd = next(trackdata)
            if cmd not in EventRegistry.MetaEvents:
                warn("Unknown Meta MIDI Event: " + repr(cmd), Warning)
                cls = UnknownMetaEvent
            else:
                cls = EventRegistry.MetaEvents[cmd]
            datalen = read_varlen(trackdata)
            data = [next(trackdata) for x in range(datalen)]
            return cls(tick=tick, data=data, metacommand=cmd)
        # is this event a Sysex Event?
        elif SysexEvent.is_event(stsmsg):
            data = []
            while True:
                datum = next(trackdata)
                if datum == 0xF7:
                    break
                data.append(datum)
            return SysexEvent(tick=tick, data=data)
        # not a Meta MIDI event or a Sysex event, must be a general message
        else:
            key = stsmsg & 0xF0
            if key not in EventRegistry.Events:
                assert self.RunningStatus, "Bad byte value"
                data = []
                key = self.RunningStatus & 0xF0
                cls = EventRegistry.Events[key]
                channel = self.RunningStatus & 0x0F
                data.append(stsmsg)
                data += [next(trackdata) for x in range(cls.length - 1)]
                return cls(tick=tick, channel=channel, data=data)
            else:
                self.RunningStatus = stsmsg
                cls = EventRegistry.Events[key]
                channel = self.RunningStatus & 0x0F
                data = [next(trackdata) for x in range(cls.length)]
                return cls(tick=tick, channel=channel, data=data)
        raise Warning("Unknown MIDI Event: " + repr(stsmsg))


class FileWriter(object):
    def write(self, midifile, pattern):
        self.write_file_header(midifile, pattern)
        for track in pattern:
            self.write_track(midifile, track)

    def write_file_header(self, midifile, pattern):
        # First four bytes are MIDI header
        packdata = pack(">LHHH", 6, pattern.format, len(pattern), pattern.resolution)
        midifile.write(b"MThd" + packdata)

    def write_track(self, midifile, track):
        buf = b""
        self.RunningStatus = None
        for event in track:
            buf += self.encode_midi_event(event)
        buf = self.encode_track_header(len(buf)) + buf
        midifile.write(buf)

    def encode_track_header(self, tracklength):
        return b"MTrk" + pack(">L", tracklength)

    def encode_midi_event(self, event):
        ret = b""
        ret += write_varlen(event.tick)
        # is the event a MetaEvent?
        if isinstance(event, MetaEvent):
            ret += bytearray([event.statusmsg]) + bytearray([event.metacommand])
            ret += write_varlen(len(event.data))
            ret += bytearray(event.data)
        # is this event a Sysex Event?
        elif isinstance(event, SysexEvent):
            ret += bytearray([0xF0])
            ret += bytearray(event.data)
            ret += bytearray([0xF7])
        # not a Meta MIDI event or a Sysex event, must be a general message
        elif isinstance(event, Event):
            if (
                not self.RunningStatus
                or self.RunningStatus.statusmsg != event.statusmsg
                or self.RunningStatus.channel != event.channel
            ):
                self.RunningStatus = event
                ret += bytearray([event.statusmsg | event.channel])
            ret += bytearray(event.data)
        else:
            raise ValueError("Unknown MIDI Event: " + str(event))
        return ret


def write_midifile(midifile, pattern):
    if type(midifile) in (str, str):
        midifile = open(midifile, "wb")
    writer = FileWriter()
    return writer.write(midifile, pattern)


def read_midifile(midifile):
    if type(midifile) in (str, str):
        midifile = open(midifile, "rb")
    reader = FileReader()
    return reader.read(midifile)
