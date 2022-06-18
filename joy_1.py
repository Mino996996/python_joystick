#!/usr/bin/env python3

import pygame


# pygame初期化
pygame.init()
try:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print('Joystickの名称: ' + joystick.get_name())
    print('ボタン数: ' + str(joystick.get_numbuttons())) 
except pygame.error:
    print('Joystickが見つかりませんでした')

# ジョイスティックの出力数値を調整
def map_axis(val):
    val = round(val, 2)
    in_min = -1
    in_max = 1
    out_min = -100
    out_max = 100
    return int((val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


# ジョイスティックの出力数値を調整(L2 R2ボタン)
def map_axis_t(val):
    val = map_axis(val)
    if val <= 0 and val >= -100:
        in_min = -100
        in_max = 0
        out_min = 0
        out_max = 50
        return int((val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
    else:
        in_min = 0
        in_max = 100
        out_min = 50
        out_max = 100
        return int((val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


def main():
    while True:
        # イベントチェック
        if pygame.event.get():
            gamepad_data = {
                # "joy_lx": map_axis(joystick.get_axis(0)),
                "joy_ly": -map_axis(joystick.get_axis(1)),
                "joy_rx": map_axis(joystick.get_axis(2)),
                # "joy_ry": -map_axis(joystick.get_axis(3)),
                # "joy_lt": map_axis_t(joystick.get_axis(4)),
                # "joy_rt": map_axis_t(joystick.get_axis(5)),
                # "hat_x": joystick.get_hat(0)[0],
                # "hat_y": joystick.get_hat(0)[1],
                # "btn_1": joystick.get_button(0),
                # "btn_2": joystick.get_button(1),
                # "btn_3": joystick.get_button(2),
                # "btn_4": joystick.get_button(3),
                # "btn_5": joystick.get_button(4),
                # "btn_6": joystick.get_button(5),
                # "btn_7": joystick.get_button(6),
                # "btn_8": joystick.get_button(7),
                # "btn_9": joystick.get_button(8),
                # "btn_10": joystick.get_button(9),
                "btn_11": joystick.get_button(10),
                "btn_12": joystick.get_button(11),
                # "btn_guide": joystick.get_button(8),
                # "btn_joyl": joystick.get_button(9),
                # "btn_joyr": joystick.get_button(10)
            }
            print(gamepad_data)


if __name__ == '__main__':
    main()