from PIL import Image
img_frames = Image.open("forensics-frames.png")
rgb_frames = img_frames.convert("RGB")
wf, hf = rgb_frames.size
cols = 6
rows = 4
frame_w = wf // cols
frame_h = hf // rows

for i in range(24):
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
    
    print(f"Frame {i:2d}: {r_sum/count:.1f}, {g_sum/count:.1f}, {b_sum/count:.1f}")

