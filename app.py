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

    # Constructor
    def __init__(self, cuadrado):
        self.cuadrado = cuadrado
        self.ventana = tk.Tk()
        self.ventana.title("Damas españolas")
        self.ventana.iconbitmap(".ico.ico")
        self.ventana.geometry( f"{str(cuadrado * 8)}x{(str(cuadrado * 8))}")
        self.interfaz =tk.Canvas(self.ventana)
        self.interfaz.bind("<ButtonPress-1>",self.boton_presion) # Evento de clic
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
                if j == "b" or j == "br":
                    self.interfaz.create_oval(b*self.cuadrado, a*self.cuadrado, (b+1)*self.cuadrado, (a+1)*self.cuadrado, fill="white")
                if j == "n" or j == "nr":
                    self.interfaz.create_oval(b*self.cuadrado, a*self.cuadrado, (b+1)*self.cuadrado, (a+1)*self.cuadrado, fill="black")
                b = b + 1
            a = a + 1
    
    def inicio_juego(self):
        self.dibujar_tablero()
        self.dibujar_fichas()
    
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
            if self.tablero[y//70][x//70] == 'b' or self.tablero[y//70][x//70] == 'br':
                self.interfaz.create_oval(x//70*self.cuadrado, y//70*self.cuadrado, (x//70+1)*self.cuadrado, (y//70+1)*self.cuadrado, fill="white",outline='red')
                self.seleccionado=True
                self.seleccionado_x = y//70
                self.seleccionado_y = x//70
        else:
            if self.tablero[y//70][x//70] == 'n' or self.tablero[y//70][x//70] == 'nr':
                self.interfaz.create_oval(x//70*self.cuadrado, y//70*self.cuadrado, (x//70+1)*self.cuadrado, (y//70+1)*self.cuadrado, fill="black",outline='red')
                self.seleccionado=True
                self.seleccionado_x = y//70
                self.seleccionado_y = x//70
    
    def destino(self, x, y):
        x = x // 70
        y = y // 70
        if (self.turno or self.tablero[self.seleccionado_x][self.seleccionado_y] == 'br' or self.tablero[self.seleccionado_x][self.seleccionado_y] == 'nr') and self.seleccionado:  
            print(f'Origen: x:{self.seleccionado_x}, y:{self.seleccionado_y}')
            print(f'Destino: x:{y}, y:{x}')
            if y == self.seleccionado_x + 1 and (x == self.seleccionado_y - 1 or x == self.seleccionado_y + 1) and (self.tablero[y][x] != 'b' and self.tablero[y][x] != 'n'and self.tablero[y][x] != 'nr' and self.tablero[y][x] != 'br'):
                print('Se puede mover')
                if (y == 7 or self.tablero[self.seleccionado_x][self.seleccionado_x] == 'b') or self.tablero[self.seleccionado_x][self.seleccionado_x] == 'br':
                    self.tablero[y][x] = 'br'
                    self.turno = False
                    self.seleccionado = False
                elif self.tablero[self.seleccionado_x][self.seleccionado_y] == 'nr':
                    self.tablero[y][x] = 'nr'
                    self.turno = True
                    self.seleccionado = False
                else:    
                    self.tablero[y][x] = 'b'
                    self.turno = False
                    self.seleccionado = False
                self.tablero[self.seleccionado_x][self.seleccionado_y] = '-'
                self.imprimir_tablero()
                self.interfaz.delete("all")
                self.dibujar_tablero()
                self.dibujar_fichas()
            elif y == self.seleccionado_x + 2 and x == self.seleccionado_y - 2 and ((self.tablero[self.seleccionado_x][self.seleccionado_x] == 'b' and self.tablero[y-1][x+1] == 'n' or 'nr') or (self.tablero[self.seleccionado_x][self.seleccionado_x] == 'nr' and self.tablero[y-1][x+1] == 'b' or 'br')) and (self.tablero[y][x] != 'b' and self.tablero[y][x] != 'n' and self.tablero[y][x] != 'nr' and self.tablero[y][x] != 'br'): 
                print(f'Destino: x:{y}, y:{x}')
                print(f'A eliminar: x:{y-1}, y:{x-1}')
                if (y == 7 or self.tablero[self.seleccionado_x][self.seleccionado_x] == 'b') or self.tablero[self.seleccionado_x][self.seleccionado_x] == 'br':
                    self.tablero[y][x] = 'br'
                    self.turno = False
                    self.seleccionado = False
                elif self.tablero[self.seleccionado_x][self.seleccionado_y] == 'nr':
                    self.tablero[y][x] = 'nr'
                    self.turno = True
                    self.seleccionado = False
                else:    
                    self.tablero[y][x] = 'b'
                    self.turno = False
                    self.seleccionado = False
                self.tablero[y-1][x+1] = '-'
                self.tablero[self.seleccionado_x][self.seleccionado_y] = '-'
                self.imprimir_tablero()
                self.interfaz.delete("all")
                self.dibujar_tablero()
                self.dibujar_fichas()
            elif y == self.seleccionado_x + 2 and x == self.seleccionado_y + 2 and ((self.tablero[self.seleccionado_x][self.seleccionado_x] == 'b' and self.tablero[y-1][x-1] == 'n' or 'nr') or (self.tablero[self.seleccionado_x][self.seleccionado_x] == 'nr' and self.tablero[y-1][x-1] == 'b' or 'br')) and (self.tablero[y][x] != 'b' and self.tablero[y][x] != 'n' and self.tablero[y][x] != 'nr' and self.tablero[y][x] != 'br'):
                print(f'Destino: x:{y}, y:{x}')
                print(f'A eliminar: x:{y-1}, y:{x-1}')
                if (y == 7 or self.tablero[self.seleccionado_x][self.seleccionado_x] == 'b') or self.tablero[self.seleccionado_x][self.seleccionado_x] == 'br':
                    self.tablero[y][x] = 'br'
                    self.turno = False
                    self.seleccionado = False
                elif self.tablero[self.seleccionado_x][self.seleccionado_y] == 'nr':
                    self.tablero[y][x] = 'nr'
                    self.turno = True
                    self.seleccionado = False
                else:    
                    self.tablero[y][x] = 'b'
                    self.turno = False
                    self.seleccionado = False
                self.tablero[y-1][x-1] = '-'
                self.tablero[self.seleccionado_x][self.seleccionado_y] = '-'
                self.imprimir_tablero()
                self.interfaz.delete("all")
                self.dibujar_tablero()
                self.dibujar_fichas()
            else:
                print('No se puede mover')
        if (not self.turno or self.tablero[self.seleccionado_x][self.seleccionado_y] == 'br' or self.tablero[self.seleccionado_x][self.seleccionado_y] == 'nr') and self.seleccionado:
            print(f'Origen: x:{self.seleccionado_x}, y:{self.seleccionado_y}')
            print(f'Destino: x:{y}, y:{x}')
            if y == self.seleccionado_x - 1 and (x == self.seleccionado_y - 1 or x == self.seleccionado_y + 1) and (self.tablero[y][x] != 'b' and self.tablero[y][x] != 'n' and self.tablero[y][x] != 'nr' and self.tablero[y][x] != 'br'):
                print('Se puede mover')
                if (y == 0 or self.tablero[self.seleccionado_x][self.seleccionado_x] == 'n') or self.tablero[self.seleccionado_x][self.seleccionado_x] == 'nr':
                    self.tablero[y][x] = 'nr'
                    self.turno = True
                    self.seleccionado = False
                elif self.tablero[self.seleccionado_x][self.seleccionado_y] == 'br':
                    self.tablero[y][x] = 'br'
                    self.turno = False
                    self.seleccionado = False
                else:    
                    self.tablero[y][x] = 'n'
                    self.turno = True
                    self.seleccionado = False
                self.tablero[self.seleccionado_x][self.seleccionado_y] = '-'
                self.imprimir_tablero()
                self.interfaz.delete("all")
                self.dibujar_tablero()
                self.dibujar_fichas()
                
            elif y == self.seleccionado_x - 2 and x == self.seleccionado_y - 2 and ((self.tablero[self.seleccionado_x][self.seleccionado_x] == 'n' and self.tablero[y+1][x+1] == 'b' or 'br') or (self.tablero[self.seleccionado_x][self.seleccionado_x] == 'br' and self.tablero[y+1][x+1] == 'n' or 'nr')) and (self.tablero[y][x] != 'b' and self.tablero[y][x] != 'n' and self.tablero[y][x] != 'nr' and self.tablero[y][x] != 'br'): 
                print(f'Destino: x:{y}, y:{x}')
                print(f'A eliminar: x:{y-1}, y:{x-1}')
                if (y == 0 or self.tablero[self.seleccionado_x][self.seleccionado_x] == 'n') or self.tablero[self.seleccionado_x][self.seleccionado_x] == 'nr':
                    self.tablero[y][x] = 'nr'
                    self.turno = True
                    self.seleccionado = False
                elif self.tablero[self.seleccionado_x][self.seleccionado_y] == 'br':
                    self.tablero[y][x] = 'br'
                    self.turno = False
                    self.seleccionado = False
                else:    
                    self.tablero[y][x] = 'n'
                    self.turno = True
                    self.seleccionado = False
                self.tablero[y+1][x+1] = '-'
                self.tablero[self.seleccionado_x][self.seleccionado_y] = '-'
                self.imprimir_tablero()
                self.interfaz.delete("all")
                self.dibujar_tablero()
                self.dibujar_fichas()

            elif y == self.seleccionado_x - 2 and x == self.seleccionado_y + 2 and ((self.tablero[self.seleccionado_x][self.seleccionado_x] == 'n' and self.tablero[y+1][x-1] == 'b' or 'br') or (self.tablero[self.seleccionado_x][self.seleccionado_x] == 'br' and self.tablero[y+1][x-1] == 'n' or 'nr')) and (self.tablero[y][x] != 'b' and self.tablero[y][x] != 'n' and self.tablero[y][x] != 'nr' and self.tablero[y][x] != 'br'):
                print(f'Destino: x:{y}, y:{x}')
                print(f'A eliminar: x:{y-1}, y:{x-1}')
                if (y == 0 or self.tablero[self.seleccionado_x][self.seleccionado_x] == 'n') or self.tablero[self.seleccionado_x][self.seleccionado_x] == 'nr':
                    self.tablero[y][x] = 'nr'
                    self.turno = True
                    self.seleccionado = False
                elif self.tablero[self.seleccionado_x][self.seleccionado_y] == 'br':
                    self.tablero[y][x] = 'br'
                    self.turno = False
                    self.seleccionado = False
                else:    
                    self.tablero[y][x] = 'n'
                    self.turno = True
                    self.seleccionado = False
                self.tablero[y+1][x-1] = '-'
                self.tablero[self.seleccionado_x][self.seleccionado_y] = '-'
                self.imprimir_tablero()
                self.interfaz.delete("all")
                self.dibujar_tablero()
                self.dibujar_fichas()
            else:
                print('No se puede mover')
            
    def imprimir_tablero(self):
        print(self.tablero)

motordams = App(70)
motordams.inicio_juego()
motordams()
