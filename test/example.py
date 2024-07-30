WIDTH = 800
HEIGHT = 480

import lvgl as lv
lv.init()

display = lv.sdl_window_create(WIDTH, HEIGHT)

scr = lv.obj()
btn = lv.button(scr)
btn.align(lv.ALIGN.CENTER, 0, 0)

label = lv.label(btn)
label.set_text('Hello World!')
lv.screen_load(scr)
