class WirelessModem:

    def connect(self):
        print("Connected through Wireless Modem")


class AudioSpeaker:

    def connect(self):
        print("Connected through Audio Speaker")


class SmartSpeaker(WirelessModem, AudioSpeaker):
    pass

speaker = SmartSpeaker()
speaker.connect()
print(SmartSpeaker.mro())