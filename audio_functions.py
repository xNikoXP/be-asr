import pickle
import struct

def serialise_data(data)->bytes:
    """Serializes the data
    
    Serializes the data and adds leading bits that indicate how long
    the packet is
    

    Args:
        data: The data that needs to be serialised
    """
    packet = pickle.dumps(data)
    length = struct.pack('>I', len(packet))
    return length + packet

def deserialise_data(packet):
    """Deserializes the data"""
    return pickle.loads(packet)
