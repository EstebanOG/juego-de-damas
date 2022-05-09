import tkinter as tk


class App():
    tablero = [['-', 'b', '-', 'b', '-', 'b', '-', 'b'],
               ['b', '-', 'b', '-', 'b', '-', 'b', '-'],
               ['-', 'b', '-', 'b', '-', 'b', '-', 'b'],
               ['-', '-', '-', '-', '-', '-', '-', '-'],
               ['-', '-', '-', '-', '-', '-', '-', '-'],
               ['n', '-', 'n', '-', 'n', '-', 'n', '-'],
               ['-', 'n', '-', 'n', '-', 'n', '-', 'n'],
               ['n', '-', 'n', '-', 'n', '-', 'n', '-']]

    def __init__(self, cuadrado):
        self.cuadrado = cuadrado
        self.ventana = tk.Tk()
        self.ventana.title("Damas españolas")
        self.ventana.iconbitmap(".ico.ico")
        self.ventana.geometry( f"{str(cuadrado * 8)}x{(str(cuadrado * 8))}")
        self.interfaz =tk.Canvas(self.ventana)
        self.interfaz.bind("<ButtonPress-1>",self.boton_presion)
        self.seleccionado=False
        self.seleccionado_x = 0
        self.seleccionado_y = 0
        self.turno = True # True: Blancas - False: Negras
        self.interfaz.pack(fill="both", expand=True)

    def __call__(self):
        self.ventana.mainloop()

    def dibujar_tablero(self):
        for i in range (8):
            for j in range (8):
                if (i+j) % 2 == 0:
                    self.interfaz.create_rectangle(i*self.cuadrado, j*self.cuadrado, (i+1)*self.cuadrado, (j+1)*self.cuadrado, fill="#dfc07f")
                else:
                    self.interfaz.create_rectangle(i*self.cuadrado, j*self.cuadrado, (i+1)*self.cuadrado, (j+1)*self.cuadrado, fill="#7a4f37")
    
    def dibujar_fichas(self):
        a = 0
        for i in self.tablero:
            b = 0
            for j in i:
                if j == "b":
                    #print(f'Es ficha blanca en la pos [{a},{b}]')
                    self.interfaz.create_oval(b*self.cuadrado, a*self.cuadrado, (b+1)*self.cuadrado, (a+1)*self.cuadrado, fill="white")

                if j == "n":
                    #print(f'Es ficha negra en la pos [{a},{b}]')
                    self.interfaz.create_oval(b*self.cuadrado, a*self.cuadrado, (b+1)*self.cuadrado, (a+1)*self.cuadrado, fill="black")
                b = b + 1
            a = a + 1
    
    def inicio_juego(self):
        print(f'La celda selecionada es...')
    
    def boton_presion(self, evento):
        if self.seleccionado:
            self.origenx=evento.x
            self.origeny=evento.y
            self.destino(self.origenx,self.origeny)
        else:
            self.origenx=evento.x
            self.origeny=evento.y
            self.ficha_seleccionada(self.origenx, self.origeny)
        
    def ficha_seleccionada(self, x, y):
        if self.turno:
            if self.tablero[y//70][x//70] == 'b':
                self.interfaz.create_oval(x//70*self.cuadrado, y//70*self.cuadrado, (x//70+1)*self.cuadrado, (y//70+1)*self.cuadrado, fill="white",outline='red')
                self.seleccionado=True
                self.seleccionado_x = y//70
                self.seleccionado_y = x//70
        else:
            if self.tablero[y//70][x//70] == 'n':
                self.interfaz.create_oval(x//70*self.cuadrado, y//70*self.cuadrado, (x//70+1)*self.cuadrado, (y//70+1)*self.cuadrado, fill="black",outline='red')
                self.seleccionado=True
    
    def destino(self, x, y):
        x = x // 70
        y = y // 70
        if self.turno:  
            print(f'Origen: x:{self.seleccionado_x}, y:{self.seleccionado_y}')
            print(f'Destino: x:{y}, y:{x}')
            

    def imprimir_tablero(self):
        print(self.tablero)

motordams = App(70)
motordams.dibujar_tablero()
motordams.dibujar_fichas()
motordams.inicio_juego()
motordams()
