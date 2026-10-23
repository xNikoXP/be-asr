import torch
import torchaudio as ta

class Wav2Vec2:

    def __init__(self):
        print(torch.__version__)
        print(ta.__version__)
        self.bundle = ta.pipelines.WAV2VEC2_ASR_BASE_960H
        print("Sample Rate:", self.bundle.sample_rate)
        print("Labels:", self.bundle.get_labels())
        self.device = torch.device("cpu")
        self.model = self.bundle.get_model().to(self.device)
        print(self.model.__class__)

    def decode(self, waveform, sample_rate):
        with torch.inference_mode():
            emission, _ = self.model(waveform)
        decoder = self.GreedyCTCDecoder(labels=self.bundle.get_labels())
        return decoder(emission[0])

    class GreedyCTCDecoder(torch.nn.Module):
        def __init__(self, labels, blank=0):
            super().__init__()
            self.blanks = labels
            self.blank = blank

        def forward(self, emission: torch.Tensor)->str:
            indices = torch.argmax(emission, dim=-1)
            indices = torch.unique_consecutive(indices, dim=-1)
            indices = [i for i in indices if i != self.blank]
            return "".join([self.labels[i] for i in indices])