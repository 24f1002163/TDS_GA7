Three artifacts, each hiding one value. Download them and extract all three — none of this needs an AI model, but all of it needs correct signal handling.

1. Image — least-significant-bit payload
A 128×128 PNG of random noise. An ASCII string is hidden in the least significant bit of the blue channel, one bit per pixel, in row-major order (left→right, top→bottom), most-significant bit of each byte first. The string ends at the first NUL byte. Recover it.



2. Audio — tone sequence
A mono 16-bit WAV at 8000 Hz. It contains 8 tones of 250 ms each, separated by 40 ms of silence. Each tone is a pure sine wave whose frequency maps to one hex digit:

0 =  400 Hz     1 =  560 Hz     2 =  720 Hz     3 =  880 Hz
4 = 1040 Hz     5 = 1200 Hz     6 = 1360 Hz     7 = 1520 Hz
8 = 1680 Hz     9 = 1840 Hz     a = 2000 Hz     b = 2160 Hz
c = 2320 Hz     d = 2480 Hz     e = 2640 Hz     f = 2800 Hz
Report the 8 hex digits in order (lower-case).

3.  Frames — scene changes
A sprite sheet of 24 video frames sampled at 1 fps, laid out 6 across and 4 down in playback order. Consecutive frames belonging to the same scene share a base colour; each frame carries ±6 of per-pixel noise, which never changes the base colour. Count the scene changes — the number of positions where frame n and frame n+1 belong to different scenes.

Answer as token|digits|count — for example TDS-1A2B3C|0f3a91cd|5