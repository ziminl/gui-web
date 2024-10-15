import tkinter as tk
from tkhtmlview import HTMLLabel

root = tk.Tk()
root.title("HTML Viewer")

with open("index.html", "r") as html_file:
    html_content = html_file.read()

html_label = HTMLLabel(root, html=html_content)
html_label.pack(fill="both", expand=True)

root.mainloop()
