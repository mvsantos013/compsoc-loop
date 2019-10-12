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

