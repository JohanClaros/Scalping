import pytesseract as tess
import pyautogui as pg
import time as tp
from PIL import Image
from datetime import datetime
from datetime import time


tess.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

#Variables que delimitan la hora
hora_inicio = time(11,0,0) 
hora_finalizacion = time(22,0,0) 


#Creacion de Hilos inf
while True:
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  
    if actual > hora_inicio and actual < hora_finalizacion:
        
        ganancia = 10
        capital = '10'

        #Captura las regiones de la pantalla y le da nombre de la imagen
        def capturareg(x,y,largo,ancho,name):
            captura_region = pg.screenshot(region=(x, y, largo,ancho,))
            captura_region.save('imagenes/'+name+'.png')
            my_image = Image.open('imagenes/'+name+'.png')
            invact = tess.image_to_string(my_image)
            return invact


        pg.click(x=1010, y=1050)
        pg.click(x=3, y=352)
        pg.scroll(-700)

        tp.sleep(1)

        precio = capturareg(21, 163, 110, 30,'exp')

        pg.click(x=532, y=320)

        tp.sleep(1)



        def comprar(m):
            pg.click(x=660, y=470)
            pg.typewrite(capital)
            pg.press('enter')
            pg.press('backspace')
            pg.press('backspace')
            pg.press('backspace')
            pg.press('backspace')
            print('comprado en:',m)
            return m


        def vender(m):
            print('Vendido en: ',m)
            pg.click(x=1245, y=470)
            pg.typewrite(capital)
            pg.press('enter')
            pg.press('backspace')
            pg.press('backspace')
            pg.press('backspace')
            pg.press('backspace')
            pg.press('backspace')
            return m

        com=0
        rentt = 0

        while True:
            try:
                precio = capturareg(21, 163, 110, 30,'precio')
                psincoma = float(precio[0:6].replace('.','').replace(' ','').replace(',',''))
                print(precio)
                psele = (psincoma + ganancia )
                if precio[6]=='.':
                    if com == 0:
                        com = comprar(psincoma)
                        compc = float(precio[0:6].replace('.','').replace(' ','').replace(',',''))
                        vent = 0
                    if precio[0]=='9': 
                        print('encontro 9')       
                    else:
                        while psele > psincoma:
                            precio = capturareg(21, 163, 110, 30,'bucle')
                            if precio[6]=='.':
                                psincoma = float(precio[0:6].replace('.','').replace(' ','').replace(',',''))
                                print(psincoma)
                        if psincoma > compc:
                            if vent == 0:
                                vent = vender(psincoma)
                                rentabilidad = vent - com
                                print('La rentabilidad fue de: ',rentabilidad)
                                rentt = rentt + rentabilidad
                                print('rentabilidad total fue de: ',rentt)
                                tp.sleep(10)
                                com = 0
                else:
                    print('Valor no :p')
            except:
                tp.sleep(2)
                print('valor no valido')





    else:
        print('Hora del bot de binarias')


