from function import gui

"""Main function to run the application."""
def main():
    # Create the GUI
    root = gui.createGui()
    # Create a button to select the Word files for analysis.
    btn = gui.tk.Button(root, text="Click me", command=lambda: gui.processMultipleFiles(gui.selectFiles()))
    # Set the position of the button
    btn.pack()
    # Run the main loop of the GUI
    root.mainloop()

if __name__ == "__main__":
    main()

