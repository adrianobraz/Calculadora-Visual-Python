import tkinter as tk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("360x350")
        self.window.resizable(False, False)

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width/2) - (300/2)
        y = (screen_height/2) - (300/2)
        self.window.geometry(f'+{int(x)}+{int(y)}')

        self.entry = tk.Entry(self.window, width=20, font=("Arial", 18))
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'DEL','0', '.', '+',
            'C', '='
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.window, text=button, width=5, font=("Arial", 18), bg="#4CAF50", fg="white", command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def click_button(self, button):
        if button == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif button == 'C':
            self.entry.delete(0, tk.END)
        elif button == 'DEL':
            current_text = self.entry.get()
            if current_text:
                new_text = current_text[:-1]
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, new_text)
        else:
            self.entry.insert(tk.END, button)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
