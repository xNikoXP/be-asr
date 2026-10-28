import struct
import pickle

import torch.multiprocessing as mp

from external_connections import ExternalConnections as ec
from ASRModels import Wav2Vec2 as wv
import speech_analyser as sa


def getAudio(q: mp.Queue):
    """Multiprocesssing method to recieve audio

    Gets the audio from client, deserializes it, and puts it in the process
    queue

    Args:
        q: The Process Queue
    
    """
    while(True):
        if q is None:
            break
        buffer = b''
        while len(buffer) < 4:
            packet = ec.recieveData(bufsize=4-len(buffer))
            if not packet:
                return None;
            buffer += packet
        header = buffer[:4]
        header = struct.unpack('>I',header)[0]
        data = b''
        while len(buffer) < header:
            packet = ec.recieveData(bufsize=header-len(data))
        data = pickle.loads(data)
        q.put(data)
    

def transcript(waveform: mp.Queue, q: mp.Queue, sample_rate):
    """Get's the written transcript and puts it in the process queue

    Args:
        waveform: Audio data  
        q: The Process Queue
        sample_rate: Sample rate of waveform
    """
    while waveform is not None:
        decoder = wv.decode(waveform=q, sample_rate=sample_rate)
        q.put(q)


def speech_check(transcript: mp.Queue):
    """Checks if transcript contains banned words"""
    while transcript != None:
        if sa.ban_check(transcript):
            send_pulse()


def send_pulse():
    """Sends an electric shock"""
    print("ELECTRIC SHOCK!!!")