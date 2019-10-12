import time

class Ball:
    ''' Esta classe representa a bola na pista '''
    def __init__(self, canvas, pos_x, pos_y):
        self.canvas = canvas
        self.initial_pos_x = pos_x
        self.initial_pos_y = pos_y
        self.pos_x = self.initial_pos_x
        self.pos_y = self.initial_pos_y

        self.value = 0
        self.size = 50
        self.move_delay = 0.5

        self.ball = self.canvas.create_oval(self.pos_x, self.pos_y, self.pos_x + self.size, self.pos_y + self.size,
                                            outline="#ffffff", fill="#32a852", width=1)

        self.text = self.canvas.create_text(self.pos_x + self.size/2, self.pos_y + self.size/2,
                                            fill="white", font="Arial 20 bold", text=str(self.value))

    def set_value(self, value):
        ''' Define valor da bola
            :param int value: valor da bola
        '''
        self.canvas.itemconfig(self.text, text=str(value))
        self.value = value

    def get_value(self):
        ''' Retorna valor da bola '''
        return self.value

    def set_delay(self, delay):
        ''' Define atrasdo na animação da bola
            :param int delay: valor do atraso em segundos
        '''
        self.move_delay = delay

    def reset_pos(self):
        ''' Coloca a bola na posição inicial '''
        self.canvas.move(self.ball, self.initial_pos_x - self.pos_x, self.initial_pos_y - self.pos_y)
        self.canvas.move(self.text, self.initial_pos_x - self.pos_x, self.initial_pos_y - self.pos_y)
        self.pos_x = self.initial_pos_x
        self.pos_y = self.initial_pos_y

    def move(self, x, y):
        ''' Move a bola na pista
            :param int x: Move a bola para a coordenada x
            :param int y: Move a bola para a coordenada y
        '''
        self.canvas.move(self.ball, x - self.pos_x, y - self.pos_y)
        self.canvas.move(self.text, x - self.pos_x, y - self.pos_y)
        self.pos_x = x
        self.pos_y = y
        time.sleep(self.move_delay)

    def move_direct_to_end(self):
        ''' Quando Y é zero a bola vai direto para o fim da pista '''
        self.move(475, 460)
        self.move(510, 390)
        self.move(510, 300)
        self.move(510, 180)
        self.move(465, 100)
        self.move(425, 20)

    def move_to_sideway(self):
        ''' Move a bola para o início do retorno '''
        self.move(365, 450)
        self.move(335, 360)
        self.move(335, 280)

    def move_around(self):
        ''' Move a bola através do retorno '''
        self.move(320, 200)
        self.move(240, 145)
        self.move(145, 150)
        self.move(80, 220)
        self.move(100, 330)
        self.move(200, 370)
        self.move(290, 340)
        self.move(335, 280)

    def move_to_end(self):
        ''' Move a bola para o fim da pista '''
        self.move(335, 190)
        self.move(355, 130)
        self.move(405, 80)
        self.move(425, 20)