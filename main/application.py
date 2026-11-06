import uuid
import struct

import torch.multiprocessing as mp

from core.external_connections import ExternalConnections as EC
from core.ASRModels import Wav2Vec2 as WV
import core.speech_analyser as speech
import audio_functions as af


class Application():


    def __init__(self):
        mac_addr = uuid.getnode()
        mac_addr = f'{mac_addr:012x}'
        mac_addr = ":".join(mac_addr[i:i+2] for i in range(0, 11, 2))
        self.bluetooth_connection = EC(mac_addr)


    def connect(self):
        self.bluetooth_connection.connect()


    def start(self):
        ctx = mp.get_context("spawn")
        waveform = ctx.Queue()
        stream = ctx.Process(target=Application._audio_stream, args=(waveform, self.bluetooth_connection))
        transcript = ctx.Queue()
        speech_process = ctx.Process(Application._asr, args=(waveform, speech_process))
        analysis_process = ctx.Process(target=Application._analysis, args=(transcript))


    def _audio_stream(q: mp.Queue, conn: EC):
        """Unpacks and deserializes stream then puts it in a queue"""
        length = b''
        while len(length) < 4:
            length += conn.receive(4-len(length))
        length = struct.unpack('>I', length)
        buffer = b''
        while len(buffer) < length:
            buffer += conn.receive(length - len(buffer))
        q.put(af.deserialise_data(buffer))


    def _asr(waveform: mp.Queue, output: mp.Queue):
        """Turns waveform into transcript and puts it in a queue"""
        model = WV()
        output.put(model.decode(waveform=waveform, sample_rate=44100))


    def _analysis(transcript: mp.Queue):
        """Checks the transcript against a list of banned words and sends electric shock"""
        if speech.ban_check(transcript=transcript):
            print("Electric Shock")
        else:
            print("Words good")