#!/usr/bin/env python

import subprocess

print subprocess.Popen("/usr/bin/mpg321 /home/pi/Documents/audio_sandbox/for.KING.COUNTRY.-.The.Proof.Of.Your.Love.Official.Music.Video.mp3", shell=True, stdout=subprocess.PIPE).stdout.read()

