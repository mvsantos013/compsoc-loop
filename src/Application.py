import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
from Ball import Ball
from Simulation import Simulation
from Simulation import SimulationState

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.set_window_config()
        self.set_widgets()
        self.simulation = None

    def set_window_config(self):
        ''' Configurações básica da janela como título e tamanho '''

        self.width = 900
        self.height = 600
        self.title('Loop básico interativo')
        self.geometry("%dx%d" % (self.width, self.height))
        self.minsize(self.width, self.height)
        self.resizable(width=False, height=False)
        self.grid_columnconfigure(12, weight=1)

    def set_widgets(self):
        ''' Componentes da janela '''

        self.sidebar = tk.Frame(self, bg='#f2f2f2', width=500, height=600, relief='sunken', borderwidth=0, padx="6", pady="10")
        self.sidebar.pack(expand=False, side='left', anchor='w')

        # Labels
        self.label_x = tk.Label(self.sidebar, text="X", width=15, anchor="w").grid(row=0, pady=(5, 0))
        self.label_y = tk.Label(self.sidebar, text="Y", width=15, anchor="w").grid(row=1, pady=(5, 0))
        self.label_delay = tk.Label(self.sidebar, text="Atraso (segundos)", width=15, anchor="w").grid(row=2, pady=(5,0))
        self.label_error = tk.Label(self.sidebar, text="", fg="red", width=30, anchor="w")
        self.label_error.grid(row=5, pady=(10,0), columnspan=2)

        # Inputs
        self.input_x = tk.Entry(self.sidebar, textvariable=tk.StringVar(self, value='0'))
        self.input_x.grid(row=0, column=1, pady=(5, 0))
        self.input_x.focus_set()
        self.input_y = tk.Entry(self.sidebar, textvariable=tk.StringVar(self, value='5'))
        self.input_y.grid(row=1, column=1, pady=(5, 0))
        self.input_delay = tk.Entry(self.sidebar, textvariable=tk.StringVar(self, value='0.5'))
        self.input_delay.grid(row=2, column=1, pady=(5, 0))

        # Botões
        self.btn_run = tk.Button(self.sidebar, text='Executar tudo', width="16", command=self.run)
        self.btn_run.grid(row=3, column=1, pady=(15, 0), sticky="w")
        self.btn_next_step = tk.Button(self.sidebar, text='Próximo passo', width="16", command=lambda:self.run(next_step_only=True))
        self.btn_next_step.grid(row=3, column=0, pady=(15, 0), padx=(0, 6), sticky="w")
        self.btn_reset = tk.Button(self.sidebar, text='Resetar', width="16", command=self.reset)
        self.btn_reset.grid(row=4, column=0, pady=(5, 0), sticky="w")

        # Barra de progresso
        self.stateBar = tk.Frame(self, bg='#f2f2f2', relief='sunken', borderwidth=0, padx="1", pady="1")
        self.stateBar.pack(expand=False, side='bottom', anchor='e')
        self.progress_label = tk.Label(self.stateBar, text="Progresso").grid(row=0, column=0)
        self.progress = ttk.Progressbar(self.stateBar, orient="horizontal", length=250, mode="determinate")
        self.progress["maximum"] = 100
        self.progress.grid(row=0, column=1)

        # Canvas
        self.canvas_frame = tk.Frame(self, bg='white')
        self.canvas_frame.pack(expand=True, fill='both', side='right')
        self.canvas = tk.Canvas(self.canvas_frame, bg='white')
        self.canvas.pack(expand=True, fill='both')

        # Pista
        self.img = ImageTk.PhotoImage(file='img/pista.png')
        self.canvas.create_image((0,0), image=self.img, anchor=tk.NW)

        # Adiciona a bola na pista
        self.ball = Ball(self.canvas, 425, 500)

        # Define texto que mostra valor em tempo real de X e Y
        self.x_text = self.canvas.create_text(40, 30, fill="white", font="Arial 20 bold", text="X=0")
        self.y_text = self.canvas.create_text(120, 30, fill="white", font="Arial 20 bold", text="Y=0")
