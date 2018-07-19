import random
from PIL import Image, ImageFont, ImageDraw

class ComputerTextGenerator(object):
    @classmethod
    def generate(cls, text, font, text_color=-1, mode='L'):
        
        image_font = ImageFont.truetype(font=font, size=32)
        text_width, text_height = image_font.getsize(text)
        
        txt_img=None
        if mode == 'L':
            txt_img = Image.new(mode, (text_width, text_height), 255)    
            txt_draw = ImageDraw.Draw(txt_img)   
            if text_color < 0:
                text_color=random.randint(1, 80)
                
            txt_draw.text((0, 0), text, fill=text_color, font=image_font)
        elif mode == '1':
            txt_img = Image.new(mode, (text_width, text_height), 0)    
            txt_draw = ImageDraw.Draw(txt_img)    
            txt_draw.text((0, 0), text, fill=1, font=image_font)
        elif mode == 'RGBA':
            txt_img = Image.new(mode, (text_width, text_height))    
            txt_draw = ImageDraw.Draw(txt_img)
            if type(text_color)==int and text_color < 0:
                text_color=[random.randint(1, 80) for _ in range(3)]
                text_color.append(255)
                text_color=tuple(text_color)
            
            txt_draw.text((0, 0), text, fill=text_color, font=image_font)   
        elif mode == 'RGB':
            txt_img = Image.new(mode, (text_width, text_height))    
            txt_draw = ImageDraw.Draw(txt_img)
            if type(text_color)==int and text_color < 0:
                text_color=[random.randint(1, 80) for _ in range(3)]
                
            txt_draw.text((0, 0), text, fill=text_color, font=image_font)  
        else:
            raise Exception('mode error!')
        return txt_img
