import flet
from flet import (ElevatedButton, Text,
                  TextField)


def main(page):
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Пожалуйста, введите ваше имя:"
            page.update()
        else:
            name = txt_name.value
            page.clean()
            page.add(Text(f"Добро пожаловать: {name}"))
            
    txt_name = TextField(label="Ваше имя")
    page.add(txt_name, ElevatedButton("Здраствуйте", on_click=btn_click))
    
    
flet.app(target=main)