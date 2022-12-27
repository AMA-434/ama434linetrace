sof = 0
fast = 0
slow = 0
right = 0
left = 0
count = 0
inc = 0
isPrevRight = 0
isPrevPrevRight = 0

def on_forever():
    global sof, fast, slow, right, left, count, inc, isPrevRight, isPrevPrevRight
    music.set_tempo(240)
    music.set_volume(96)
    sof = 60
    fast = 55
    slow = 10
    right = -60
    left = 60
    if cuteBot.tracking(cuteBot.TrackingState.L_R_LINE):
        count = 0
        inc = -10
        cuteBot.motors(fast, fast)
        isPrevRight = 0
    elif cuteBot.tracking(cuteBot.TrackingState.L_UNLINE_R_LINE):
        cuteBot.motors(sof, slow)
        isPrevRight = 1
        isPrevPrevRight = 1
    elif cuteBot.tracking(cuteBot.TrackingState.L_LINE_R_UNLINE):
        cuteBot.motors(slow, sof)
        isPrevRight = 2
        isPrevPrevRight = 2
    elif cuteBot.tracking(cuteBot.TrackingState.L_R_UNLINE):
        if isPrevRight == 1:
            cuteBot.motors(left, right)
        elif isPrevRight == 2:
            cuteBot.motors(right, left)
        elif isPrevRight == 0:
            if count == 0:
                cuteBot.move_time(cuteBot.Direction.FORWARD, 100, 0.05)
                count = 1
            else:
                if isPrevPrevRight == 2:
                    music.play_tone(1050, music.beat(BeatFraction.EIGHTH))
                    cuteBot.motors(Math.constrain(inc, -10, 30), 60)
                    inc += 0.2
                    if inc == 0:
                        cuteBot.motors(100, 60)
                        inc += 0.2
                elif isPrevPrevRight == 1:
                    music.play_tone(2100, music.beat(BeatFraction.EIGHTH))
                    cuteBot.motors(60, Math.constrain(inc, -10, 30))
                    inc += 0.2
                    if inc == 0:
                        cuteBot.motors(60, 100)
                        inc += 0.2
basic.forever(on_forever)
