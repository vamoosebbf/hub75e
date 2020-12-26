# generate a c table that can convert rgb565 to rgb444
def rgb565torgb444():
    arr = []
    for i in range(65536):
        r = i >> 11 & 0x1f
        r = (r * 16 + 16) // 32
        if( r == 16):
            r = 15
        g = (i >> 5) & 0x3f
        g = (g * 16 + 32) // 64
        if(g == 16):
            g = 15
        b = i & 0x1f
        b = (b * 16 + 16) // 32
        if(b == 16):
            b = 15
        rgb444 = (r << 8) | (g << 4) | b
        arr.append(rgb444)
    return arr

def format_arr(arr):
    s = str("unsigned short rgb565_to_rgb444[65536] = {")
    for i in arr:
        s = s + str("0x%x"%i) + ","
    s = s + "};"
    return s

def rgb444_pwm():
    arr_pwm = []
    for i in range(16):
        arr = []
        for j in range(4096):
            # red
            r = j >> 8
            tr = 1 if(r - i > 0) else 0
            # green
            g = j >> 4 & 0x0f
            tg = 1 if(g - i > 0) else 0
            # blue
            b = j & 0x0f
            tb = 1 if(b - i > 0) else 0
            t = (tr << 7) | (tg << 6) | tb << 5
            arr.append(t)
        arr_pwm.append(arr)
    return arr_pwm

def format_arr_pwm(arr_pwm):
    s = str("unsigned char pwm_table[16][4096] = {")
    for i in arr_pwm:
        s = s + "{"
        for j in i:
            s = s + "0x{:x},".format(j)
        s = s + "},"
    s = s + "};"
    return s

if __name__ == "__main__":
    fo = open("color_table.c", "w")
    rgb444 = rgb565torgb444()
    pwm = rgb444_pwm()
    print(len(rgb444))
    print(len(pwm))
    fo.write("#include \"color_table.h\"\n\n")
    fo.write(str(format_arr(rgb444)))
    fo.write(str("\n\n\n\n" + format_arr_pwm(pwm)))
    fo.close()
