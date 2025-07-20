import torchaudio
import torch
from noisereduce.torchgate import TorchGate as TG
from os import environ

def reduce_file_noise(filename="files/input.wav"):
    waveform, sample_rate = torchaudio.load(filename)
    device = torch.device(environ['DEVICE'])

    tg = TG(sr=sample_rate, nonstationary=True, n_thresh_nonstationary=1.15).to(device)

    enhanced_speech = tg(waveform)
    
    torchaudio.save(filename, enhanced_speech, sample_rate)