def rgb(r, g, b):
    r = hex(255 if r > 255 else (0 if r < 0 else r))[2:]
    g = hex(255 if g > 255 else (0 if g < 0 else g))[2:]
    b = hex(255 if b > 255 else (0 if b < 0 else b))[2:]

    return str(r.zfill(2) + g.zfill(2) + b.zfill(2)).upper()
