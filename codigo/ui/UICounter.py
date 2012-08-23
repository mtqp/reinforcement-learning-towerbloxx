#coding=utf-8

from UIObject import UIObject
from Constants import * 

class UICounter(object):
    def __init__(self, name):
        zero = COUNTER_PATH + "0" + IMAGE_EXTENSION
        images = [zero, zero, zero]
        self.ui_objects = []
        for img in images:
            self.ui_objects.append(UIObject(name, img))

    #se ponen uno al lado del otro... quizas sirve mas uno abajo del otro, no se
    def place(self, x_axis, y_axis):
        last_x = x_axis
        #last_y = y_axis
        
        for ui_object in self.ui_objects:
            ui_object.place(last_x, y_axis)
            last_x += ui_object.get_width()
            
    def set_state(self, state):
        height = state.tower.height
        ui_objs_count = len(self.ui_objects)
        
        if height < 10**ui_objs_count:
            str_height = str(height)
            while len(str_height) < ui_objs_count:
                str_height = "0" + str_height
            
            for i in range(ui_objs_count-1,-1,-1):
                str_number = str_height[i]
                self.ui_objects[i].set_image(COUNTER_PATH + str_number + IMAGE_EXTENSION)
        else:
            raise Exception("No se permite mas de " + str(ui_objs_count -1) + " pisos")

    def draw(self, screen):
        for ui_object in self.ui_objects:
            screen.blit(ui_object.surface, ui_object.rectangle)

    #quizas lo necesito para q no tire excepcion, sino borrar
    def move(self):
        pass

