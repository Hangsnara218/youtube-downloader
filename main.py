import tkinter
import customtkinter
from pytube import YouTube


def initDownload():
    try:
        ytLink = link.get()
        ytObj = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObj.streams.get_highest_resolution()
        title.configure(text=ytObj.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!")
    except: 
        finishLabel.configure(text="Error!", text_color="red")
    
    
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100

    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

# update progress bar
    progressBar.set(float(percentage_of_completion) / 100)    

# system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# app frame

app = customtkinter.CTk()
app.geometry("700x400")
app.title("Download from Youtube")

# ui elements

title = customtkinter.CTkLabel(app, text="Enter youtube link")
title.pack(padx=10, pady=10)

# link output
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=400, height=45, textvariable=url_var)
link.pack()

# download finished
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# progress pct
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()


progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0.0)
progressBar.pack(padx=10, pady=10)

# button to download
download = customtkinter.CTkButton(app, text="Download", command=initDownload)
download.pack(padx=10, pady=10)

# run application
app.mainloop()