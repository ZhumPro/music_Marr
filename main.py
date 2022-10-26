import pygame
from music_sample.Dahai import Dahai
from music_sample.cannonInC import CannonC
from music_sample.cannonRepair import CannonR
from music_sample.demo import Demo
from music_sample.littleStar import LittleStar
from music_sample.sakuratears import SakuraTears
from music_sample.thespectre import TheSpectre


def play(mname):
    """
       # freq = 44100  # audio CD quality
       # bit_size = -16  # unsigned 16 bit
       # channels = 2  # 1 is mono, 2 is stereo
       # buffer = 2048  # number of samples (experiment to get right sound)
    """
    midi_music = ""
    music_name = mname.lower()
    if music_name == "sakuratears":
        midi_music = SakuraTears()
    elif music_name == "littlestar":
        midi_music = LittleStar()
    elif music_name == "dahai":
        midi_music = Dahai()
    elif music_name == "cannonc":
        midi_music = CannonC()
    elif music_name == "cannonr":
        midi_music = CannonR()
    elif music_name == "thespectre":
        midi_music = TheSpectre()
    elif music_name == "demo":
        midi_music = Demo()
    else:
        pass

    music = midi_music.generator()
    pygame.mixer.init(buffer=2048)
    clock = pygame.time.Clock()
    print("#" * 10 + "开始演奏" + "#" * 10)
    pygame.mixer.music.load(music)
    print("#" * 10 + "加载完成" + "#" * 10)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(30)
    print("#" * 10 + "结束演奏" + "#" * 10)


if __name__ == "__main__":
    music_title = input("输入歌曲：")
    play(music_title)
