import tkinter as tk

def buy_bitcoin():
    # Add your code here for buying Bitcoin
    print("Buying Bitcoin")

def sell_bitcoin():
    # Add your code here for selling Bitcoin
    print("Selling Bitcoin")

# Create the main window
window = tk.Tk()
window.title("BTC GUI")

# Create buttons for buying and selling Bitcoin
buy_button = tk.Button(window, text="Buy Bitcoin", command=buy_bitcoin)
sell_button = tk.Button(window, text="Sell Bitcoin", command=sell_bitcoin)

# Add the buttons to the window
buy_button.pack()
sell_button.pack()

# Start the GUI event loop
window.mainloop()
