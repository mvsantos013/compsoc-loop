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


class SimulationState(Enum):
    ''' Estados possíveis da simulação '''
    READY = 1
    RUNNING = 2
    PAUSED = 3
    FINISHED = 4