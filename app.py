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
                    print(f'Es ficha blanca en la pos [{a},{b}]')

                if j == "n":
                    print(f'Es ficha negra en la pos [{a},{b}]')
                b = b + 1
            a = a + 1
motordams = App(70)
motordams.dibujar_tablero()
motordams.dibujar_fichas()
motordams()
