from lv_utils import event_loop
import lvgl as lv

WIDTH = 800
HEIGHT = 480

event_loop = event_loop()
disp_drv = lv.sdl_window_create(WIDTH, HEIGHT)
mouse = lv.sdl_mouse_create()
keyboard = lv.sdl_keyboard_create()
#keyboard.set_group(self.group)

scr = lv.obj()
btn = lv.button(scr)
btn.align(lv.ALIGN.CENTER, 0, 0)

label = lv.label(btn)
label.set_text('Hello World!')
lv.screen_load(scr)

