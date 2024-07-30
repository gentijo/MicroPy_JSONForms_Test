from JSONForms_Renderer import JSONForms_Renderer
from JSONForms_Style import JSONForms_Style
from JSONForms_Driver import JSONForms_Driver

from lv_utils import event_loop
import lvgl as lv

WIDTH = 800
HEIGHT = 480

event_loop = event_loop()
disp_drv = lv.sdl_window_create(WIDTH, HEIGHT)
mouse = lv.sdl_mouse_create()
keyboard = lv.sdl_keyboard_create()

#keyboard.set_group(self.group)

#JSONFormRenderer.enableTestMode()
JSONForms_Style.parseStyleDefinitionFromJSONFile("schema.json")
JSONForms_Style.parseStyleDefinitionFromJSONFile("styles.json")
#JSONForms_Style.dumpParsedStyles()


#scr = lv.obj()
#btn = lv.button(scr)
#btn.align(lv.ALIGN.CENTER, 0, 0)
#label = lv.label(btn)
#label.set_text('Hello World!')
#lv.screen_load(scr)

JSONForms_Renderer.parseLayoutDefinitionFromJSONFile("ui-schema.json")
    