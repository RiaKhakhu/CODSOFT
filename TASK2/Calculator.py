import tkinter as tk
from tkinter import ttk

"""
A basic calculator that performs simple arithmetic calculations with live feedback and error handling.

Author: Khakhu Ria
Version: 23/09/2024
"""


class Calculator:
    def __init__(self):
        # Initialize the main application window
        self.root_frame = tk.Tk()
        self.root_frame.geometry("450x350")
        self.root_frame.title("Calculator")
        self.instructions = tk.Label(self.root_frame, text = "This calculator is limited to arithmetic "
                                                             "calculations of 2 numbers.")
        self.instructions.pack(side = tk.TOP)

        # Create variables for storing input numbers and operation
        self.current_input = ""
        self.operation = None
        self.num1 = None

        # Create a label to display the current operation and result
        self.display = tk.Label(self.root_frame, text="", anchor='e', font=('Arial', 24), bg="white", fg="black")
        self.display.pack(fill=tk.BOTH, padx=10, pady=10)

        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(self.root_frame)
        self.button_frame.pack()

        # Dictionary to store button text and their respective commands
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('÷', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('x', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('+', 4, 3), ('=', 4, 2),
        ]

        # Loop to create and place the buttons in a grid
        for (text, row, col) in buttons:
            button = ttk.Button(self.button_frame, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, ipadx=10, ipady=10, padx=5, pady=5)

    def on_button_click(self, char):
        """Handle button press events"""
        if char.isdigit():
            # If the button pressed is a digit, append it to the current input
            self.current_input += char
            self.update_display(self.current_input)
        elif char in "+-x÷":
            # If an operation button is pressed, store the first number and operation
            if self.current_input:
                self.num1 = eval(self.current_input)
                self.operation = char
                self.current_input = ""
                self.update_display(f"{self.num1} {self.operation}")
        elif char == "=":
            # If equals is pressed, calculate the result
            self.calculate_result()
        elif char == "C":
            # If clear is pressed, reset everything
            self.clear()

    def update_display(self, value):
        """Update the display label"""
        self.display.config(text=value)

    def calculate_result(self):
        """Perform the calculation based on the operation"""
        try:
            num2 = eval(self.current_input)
            if self.operation == '+':
                result = self.num1 + num2
            elif self.operation == '-':
                result = self.num1 - num2
            elif self.operation == 'x':
                result = self.num1 * num2
            elif self.operation == '÷':
                if num2 == 0:
                    result = "Error (Div by 0)"  # Division by zero check
                else:
                    result = self.num1 / num2
            else:
                result = "Invalid Operation"

            self.update_display(result)  # Show the result
            self.current_input = str(result)  # Reset for chaining calculations
        except ValueError:
            self.update_display("Error")  # Invalid input case

    def clear(self):
        """Clear all inputs and reset the calculator"""
        self.current_input = ""
        self.num1 = None
        self.operation = None
        self.update_display("")

    def run(self):
        """Start the application main loop"""
        self.root_frame.mainloop()


def main():
    calculator = Calculator()
    calculator.run()


if __name__ == "__main__":
    main()
