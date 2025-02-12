import tkinter as tk

class Timer:
    btn_font = ("Arial", 10)
    lbl_font = ('Arial', 50)
    LBL_COLOR = "#227B94"
    BACKGROUND_COLOR = '#16325B'

    def __init__(self):
        # to controll the griding and destroiing the start btn
        self.enter_to_start = 1
        self.window = tk.Tk()
        self.window.config(background=self.BACKGROUND_COLOR)
        self.is_running = False
        self.window.title('Timer')
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.lbl_hour = tk.Label(
            master=self.window,
            text=f'{self.hour:02}',
            fg=self.LBL_COLOR,
            font=self.lbl_font,
            bg=self.BACKGROUND_COLOR,
        )
        self.lbl_colon1 = tk.Label(
            master=self.window,
            text=':',
            fg=self.LBL_COLOR,
            font=self.lbl_font,
            bg=self.BACKGROUND_COLOR,
        )
        self.lbl_minute = tk.Label(
            master=self.window,
            text=f'{self.minute:02}',
            fg=self.LBL_COLOR,
            font=self.lbl_font,
            bg=self.BACKGROUND_COLOR,
        )
        self.lbl_colon2 = tk.Label(
            master=self.window,
            text=':',
            fg=self.LBL_COLOR,
            font=self.lbl_font,
            bg=self.BACKGROUND_COLOR,
        )
        self.lbl_second = tk.Label(
            master=self.window,
            text=f'{self.second:02}',
            fg=self.LBL_COLOR,
            font=self.lbl_font,
            bg=self.BACKGROUND_COLOR,
        )
        self.btn_start = tk.Button(
            master=self.window,
            text='Start',
            font=self.btn_font,
            command=lambda: self.window.after(1, self.start_counting),
        )
        self.btn_pause = tk.Button(
            master=self.window,
            text='Stop',
            font=self.btn_font,
            command=lambda: self.stop_counting(),
        )
        self.btn_start_again = tk.Button(
            master=self.window,
            text='Start Again',
            font=self.btn_font,
            command=lambda: self.reset_counting(),
        )
        self.btn_continue = tk.Button(
            master=self.window,
            text='Continue',
            font=self.btn_font,
            command=lambda: self.continue_counting(),
        )

    def start_counting(self):
        if (not self.is_running) and self.enter_to_start == 1:
            self.is_running = True
            self.btn_start.destroy()
            self.btn_pause.grid(row=1, column=0, columnspan=5, pady=(0, 8))
            self.enter_to_start += 1
            self.window.after(1, self.start_counting)

        elif self.is_running:
            self.second += 1
            self.minute = self.second // 60
            self.hour = self.minute // 60
            self.lbl_second.config(text=f'{self.second % 60:02}')
            self.lbl_minute.config(text=f'{self.minute:02}')
            self.lbl_hour.config(text=f'{self.hour:02}')
            self.window.after(1000, self.start_counting)

    def stop_counting(self):
        self.is_running = False
        self.btn_pause.destroy()
        self.btn_start_again.grid(row=1, column=0,columnspan=2, pady=(0, 8))
        self.btn_continue.grid(row=1, column=4,columnspan=2, pady=(0, 8))

    def reset_counting(self):
        self.hour = 0
        self.second = 0
        self.minute = 0
        self.lbl_hour.config(text = f'{self.hour:02}')
        self.lbl_minute.config(text = f'{self.minute:02}')
        self.lbl_second.config(text = f'{self.second:02}')
        self.btn_continue.destroy()
        self.btn_start_again.destroy()
        # reseting values and rebuild destroied buttons 
        self.enter_to_start = 1
        self.is_running = False
        self.create_destoried_buttons()
        self.btn_start.grid(row=1, column=0, columnspan=5, pady=(0, 8))

    def continue_counting(self):
        self.btn_continue.destroy()
        self.btn_start_again.destroy()
        self.create_destoried_buttons()
        self.is_running = True
        self.btn_pause.grid(row=1, column=0, columnspan=5, pady=(0, 8))
        # trigger the start button automaticly
        self.btn_start.invoke()
    
    def create_destoried_buttons(self):
        self.btn_start = tk.Button(
            master=self.window,
            text='Start',
            font=self.btn_font,
            command=lambda: self.window.after(1, self.start_counting),
        )
        self.btn_pause = tk.Button(
            master=self.window,
            text='Stop',
            font=self.btn_font,
            command=lambda: self.stop_counting(),
        )
        self.btn_start_again = tk.Button(
            master=self.window,
            text='Start Again',
            font=self.btn_font,
            command=lambda: self.reset_counting(),
        )
        self.btn_continue = tk.Button(
            master=self.window,
            text='Continue',
            font=self.btn_font,
            command=lambda: self.continue_counting(),
        )
    def run(self) -> None:
        self.lbl_hour.grid(row=0, column=0)
        self.lbl_colon1.grid(row=0, column=1)
        self.lbl_minute.grid(row=0, column=2)
        self.lbl_colon2.grid(row=0, column=3)
        self.lbl_second.grid(row=0, column=4)
        self.btn_start.grid(row=1, column=0, columnspan=5, pady=(0, 8))
        self.window.mainloop()


if __name__ == '__main__':
    app = Timer()
    app.run()
