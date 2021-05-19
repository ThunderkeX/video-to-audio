# -----------------------------------------------------
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox 
from ttkthemes import ThemedTk
import moviepy.editor
import time
import os
import tkinter.messagebox 
def x():
	question=messagebox.askquestion('Question','Are You Sure To Quit?')
	if question=='yes':
		import sys
		sys.exit()
	else:
		None
r=ThemedTk(themebg=True)
r.set_theme('arc')
r.protocol('WM_DELETE_WINDOW',x)
saved_file_path = ttk.Label(r)

saved_file_path.place(x=1  , y=150)
convert_button = ttk.Button(r, text='Convert To Audio',state=DISABLED)
convert_button.place(x=175+2 , y=100)
open_file_path=ttk.Label(r)
open_file_path.place(x=1,y=175)
def video_to_audio():
    global asking_file_to_save 
    global star__
    messagebox.showwarning('Warning!',' Remember Put In Small Letters File Extension At The End Of The File Name') # image converter,insertation of a mp3 to a mp4 # advance sppech recognization
    asking_file_to_save=filedialog.asksaveasfile('wb',title='Save As',filetypes=(('mp3','*.mp3',),("mp3","*.mp3"),('wav','*.wav'),('ogg','*.ogg')))
    if asking_file_to_save==None:
    	saved_file_path.config(text='')
    	tkinter.messagebox.showwarning('Info','File Not Saved!')
    if asking_file_to_save!=None:
    	star__=asking_file_to_save.name 
    	sre=str(os.path.basename(star__))    
    	user_video=moviepy.editor.VideoFileClip(star_a)
    	try:
    		print('Converting... Depents On Your HDD Or SSD Read Write Speed!')
    		audio=user_video.audio.write_audiofile(str(asking_file_to_save.name))
    		os.startfile(str(asking_file_to_save.name))
    		saved_file_path.config(text=f'Saved File Path:-{asking_file_to_save.name}')
    	except ValueError:
    		tkinter.messagebox.showwarning('Info','Please Put File Extension Or Correct File Extension At The End Of Filename Or Only wav,ogg,mp3 Can Be Saved!')
    		saved_file_path.config(text='')
def dialog_video():
    global extesntion_
    global star_a
    global path_opend_file_
    filename_=filedialog.askopenfile('rb',filetype=(("mp4","*.mp4"),('mp4','*.mp4'),('ogv','*.ogv'),('MOV','*.MOV'),('avi','*.avi')),title='Open Mp4 File')
    if filename_==None:
    	open_file_path.config(text='')
    	tkinter.messagebox.showwarning('Info','File Not Imported!')
    try:
        path_opend_file_=(filename_.name)
        star_a=str(path_opend_file_)
        check=(star_a.endswith('.mp4'))
        check_=(star_a.endswith('.avi'))
        check_1=(star_a.endswith('.ogv'))
        check_1=(star_a.endswith('.MOV'))
        if check==True:
            convert_button.config(command=video_to_audio)
            convert_button.config(state=NORMAL)
            open_file_path.config(text=f'Opened File Path:-{path_opend_file_}')
        if check_==True:
            convert_button.config(command=video_to_audio)
            convert_button.config(state=NORMAL)
            open_file_path.config(text=f'Opened File Path:-{path_opend_file_}')
        if check_1==True:
            convert_button.config(command=video_to_audio)
            convert_button.config(state=NORMAL)
            open_file_path.config(text=f'Opened File Path:-{path_opend_file_}')
    except Exception :
        convert_button.config(state=DISABLED)
r.minsize(500,200) 
r.maxsize(500,200)
r.title('Video To Audio')
r.geometry('500x200')
heading=ttk.Label(r,text='Video File to Audio File ',font=('Font',10))
heading.place(x=100+25+5+5+5+15,y=1)
browse_mp4=ttk.Button(r,text='Browse A Video File',command=dialog_video)
browse_mp4.place(x=172,y=55)
mainloop()
# -----------------------------------------------------
#