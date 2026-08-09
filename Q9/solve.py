from PIL import Image
import wave
import struct
import math

# Part 1: Image
img = Image.open("forensics-image.png")
rgb = img.convert("RGB")
w, h = img.size
bits = []
for y in range(h):
    for x in range(w):
        r, g, b = rgb.getpixel((x, y))
        bits.append(b & 1)

chars = []
for i in range(0, len(bits), 8):
    byte_bits = bits[i:i+8]
    if len(byte_bits) < 8:
        break
    val = 0
    for bit in byte_bits:
        val = (val << 1) | bit
    if val == 0:
        break
    chars.append(chr(val))

token = "".join(chars)
print("Part 1:", token)

# Part 2: Audio
with wave.open("forensics-audio.wav", "rb") as wf:
    sr = wf.getframerate()
    nframes = wf.getnframes()
    data = wf.readframes(nframes)
    
samples = struct.unpack(f"<{nframes}h", data)

freqs_map = {
    400: '0', 560: '1', 720: '2', 880: '3',
    1040: '4', 1200: '5', 1360: '6', 1520: '7',
    1680: '8', 1840: '9', 2000: 'a', 2160: 'b',
    2320: 'c', 2480: 'd', 2640: 'e', 2800: 'f'
}

hex_digits = []
tone_samples = int(sr * 0.25)
silence_samples = int(sr * 0.04)

for i in range(8):
    start = i * (tone_samples + silence_samples)
    end = start + tone_samples
    chunk = samples[start:end]
    
    best_f = None
    best_mag = -1
    
    # Compute DFT magnitude for each target frequency
    for f in freqs_map:
        omega = 2 * math.pi * f / sr
        sum_cos = 0.0
        sum_sin = 0.0
        for n, s in enumerate(chunk):
            sum_cos += s * math.cos(omega * n)
            sum_sin += s * math.sin(omega * n)
        mag = sum_cos**2 + sum_sin**2
        if mag > best_mag:
            best_mag = mag
            best_f = f
            
    hex_digits.append(freqs_map[best_f])

digits = "".join(hex_digits)
print("Part 2:", digits)

# Part 3: Frames
img_frames = Image.open("forensics-frames.png")
rgb_frames = img_frames.convert("RGB")
wf, hf = rgb_frames.size
cols = 6
rows = 4
frame_w = wf // cols
frame_h = hf // rows

def get_frame_avg(i):
    r_idx = i // cols
    c_idx = i % cols
    x0 = c_idx * frame_w
    y0 = r_idx * frame_h
    
    r_sum, g_sum, b_sum = 0, 0, 0
    count = 0
    for y in range(y0, y0+frame_h, 5):
        for x in range(x0, x0+frame_w, 5):
            r, g, b = rgb_frames.getpixel((x, y))
            r_sum += r
            g_sum += g
            b_sum += b
            count += 1
    return (r_sum/count, g_sum/count, b_sum/count)

scene_changes = 0
prev_avg = get_frame_avg(0)

for i in range(1, 24):
    avg = get_frame_avg(i)
    diff = sum((avg[j] - prev_avg[j])**2 for j in range(3)) ** 0.5
    if diff > 15:
        scene_changes += 1
    prev_avg = avg

print("Part 3:", scene_changes)

print(f"Final Output: {token}|{digits}|{scene_changes}")
