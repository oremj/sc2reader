class SC2ReaderError(Exception):
    pass

class ReadError(SC2ReaderError):
    pass

class ProcessError(SC2ReaderError):
    pass

class FileError(SC2ReaderError):
    pass


class ParseError(Exception):
    def __init__(self, message, replay, event, bytes):
        self.message = message
        self.replay = replay
        self.event = event
        self.bytes = bytes
        
    def __str__(self):
        return """ParseError %s
            %s - %s
            %s""" % (self.message, self.event.type, self.event.code, self.bytes)
        
    def __repr__(self):
        return str(self)
