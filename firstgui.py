import tkinter as tk
import pytube as pt

app = tk.Tk()
app.title("youtube downloder")


#function to download video from youtube
def download():

    url = url_box.get("1.0","end")
    yt = pt.YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download()

label=tk.Label(app, text=("To Downnload Youtube Video"),font=("Areal,25,bold"))
label.pack() 



#for receving url from user
url_box=tk.Text(app, height=3, font=("Areal, 16"))
url_box.insert('end', "Enter your url discription here:")
url_box.pack(padx=20,pady=20)

#to download 
button=tk.Button(app, bd=30, bg="green", text="download",font=('Areal',18) ,command=download )
button.pack()

app.mainloop()