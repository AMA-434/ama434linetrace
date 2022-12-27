let sof = 0
let fast = 0
let slow = 0
let right = 0
let left = 0
let count = 0
let inc = 0
let isPrevRight = 0
let isPrevPrevRight = 0
basic.forever(function () {
    music.setTempo(240)
    music.setVolume(96)
    sof = 60
    fast = 55
    slow = 10
    right = -60
    left = 60
    if (cuteBot.tracking(cuteBot.TrackingState.L_R_line)) {
        count = 0
        inc = -10
        cuteBot.motors(fast, fast)
        isPrevRight = 0
    } else if (cuteBot.tracking(cuteBot.TrackingState.L_unline_R_line)) {
        cuteBot.motors(sof, slow)
        isPrevRight = 1
        isPrevPrevRight = 1
    } else if (cuteBot.tracking(cuteBot.TrackingState.L_line_R_unline)) {
        cuteBot.motors(slow, sof)
        isPrevRight = 2
        isPrevPrevRight = 2
    } else if (cuteBot.tracking(cuteBot.TrackingState.L_R_unline)) {
        if (isPrevRight == 1) {
            cuteBot.motors(left, right)
        } else if (isPrevRight == 2) {
            cuteBot.motors(right, left)
        } else if (isPrevRight == 0) {
            if (count == 0) {
                cuteBot.moveTime(cuteBot.Direction.forward, 100, 0.05)
                count = 1
            } else if (isPrevPrevRight == 2) {
                music.playTone(1050, music.beat(BeatFraction.Eighth))
                cuteBot.motors(Math.constrain(inc, -10, 30), 60)
                inc += 0.2
            } else if (isPrevPrevRight == 1) {
                music.playTone(2100, music.beat(BeatFraction.Eighth))
                cuteBot.motors(60, Math.constrain(inc, -10, 30))
                inc += 0.2
            }
        }
    }
})
