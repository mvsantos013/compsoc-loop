import threading
from enum import Enum
import time


class Simulation:
    ''' Classe que gerencia a simulação '''
    def __init__(self, x, y, ball, progress_bar):
        self.x = x
        self.y = y
        self.ball = ball
        self.progress_bar = progress_bar
        self.range = self.y - self.x
        if self.range == 0:
            self.range = 1

        self.state = SimulationState.READY
        self.next_step_only = False

    def run(self):
        ''' Inicia a simulação '''
        if self.state == SimulationState.READY:
            SimulationThread(self).start()
        self.state = SimulationState.RUNNING

    def is_ready(self):
        ''' Retorna verdadeiro se a simulação está pronta para ser iniciada '''
        return self.state == SimulationState.READY

    def is_finished(self):
        ''' Retorna verdadeiro se a simulação terminou '''
        return self.state == SimulationState.FINISHED

    def is_paused(self):
        ''' Retorna verdadeiro se a simualação está pausada '''
        return self.state == SimulationState.PAUSED


class SimulationThread(threading.Thread):
    ''' Thread da simulação que contém o loop principal, evita que a aplicação gráfica trave, a simulação é controlada
        através de seus estados
    '''
    def __init__(self, simulation):
        threading.Thread.__init__(self)
        self.simulation = simulation

    def run(self):
        ''' Loop da simulação '''

        while True:

            # Espera ocupada enquanto a simulação está pausada
            if self.simulation.is_paused():
                continue

            # Desenha o movimento da bola
            self.draw()

            # Muda estado da simulação para finalizado caso número máximo de passos atingidos
            if self.simulation.x == self.simulation.y:
                self.simulation.state = SimulationState.FINISHED
                break

            # Atualiza progresso
            self.simulation.x += 1
            self.simulation.progress_bar["value"] = self.simulation.x * 100.0 / self.simulation.range

            # Pausa simulação caso seja para andar só um passo
            if self.simulation.next_step_only:
                self.simulation.next_step_only = False
                self.simulation.state = SimulationState.PAUSED
                continue

    def draw(self):
        ''' Lógica de movimentação da bola '''

        # A bola se encontra na posição inicial
        if self.simulation.ball.pos_x == 425 and self.simulation.ball.pos_y == 500:
            if self.simulation.y > 0:
                self.simulation.ball.move_to_sideway()
            else:
                self.simulation.ball.move_direct_to_end()

        # A bola se encontra em frente ao retorno
        if self.simulation.ball.pos_x == 335 and self.simulation.ball.pos_y == 280:
            if self.simulation.x < self.simulation.y:
                self.simulation.ball.move_around()
                self.simulation.ball.set_value(self.simulation.x+1)
            else:
                self.simulation.ball.move_to_end()


class SimulationState(Enum):
    ''' Estados possíveis da simulação '''
    READY = 1
    RUNNING = 2
    PAUSED = 3
    FINISHED = 4