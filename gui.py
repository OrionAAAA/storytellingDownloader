from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askdirectory
from downloadCore import downloadCore
import time
class GUI():
    window = Tk()  # 创建顶层窗口
    downlader=downloadCore()
    var_album_num_text=""
    def __init__(self):
        self.init_Window()
        self.first_interface()
        self.window.mainloop

    def init_Window(self):#初始化窗口
        self.window.title('粤语评书下载器')
        screen_width = self.window.winfo_screenwidth()  # 屏幕尺寸
        screen_height = self.window.winfo_screenheight()
        window_width, window_height = 600, 450
        x, y = (screen_width - window_width) / 2, (screen_height - window_height) / 3
        size = '%dx%d+%d+%d' % (window_width, window_height, x, y)
        self.window.geometry(size)  # 初始化窗口大小
        self.window.resizable(False, False)  # 窗口长宽不可变
        # window.maxsize(600, 450)
        # window.minsize(300, 240)

    def first_interface(self):
        #第一页界面
        print("打开第一个页面")
        label_album_num = Label(self.window, text='请输入作品编号', cursor='xterm')
        self.var_album_num_text = StringVar()
        entry_album_num = Entry(self.window, relief=RAISED, fg='gray', bd=2, width=58, textvariable=self.var_album_num_text, cursor='xterm')
        button_to_2step=Button(self.window, text='下一步',command=self.second_interface,height=1, width=15, relief=RAISED, bd=4, activebackground='pink',
                      activeforeground='white', cursor='hand2')
                      
        label_album_num.place(relx=0.12, rely=0.12, anchor=CENTER)
        entry_album_num.place(relx=0.56, rely=0.12, anchor=CENTER)
        button_to_2step.place(relx=0.80, rely=0.30, anchor=CENTER)

    def second_interface(self):
        print("打开第二个页面")
        self.downlader.get_album_info(self.var_album_num_text.get())
        self.refresh()
        #第二页界面
        label_album_num = Label(self.window, text=self.downlader.title, cursor='xterm')
        # self.var_album_num_text = StringVar()
        # entry_album_num = Entry(self.window, relief=RAISED, fg='gray', bd=2, width=58, textvariable=self.var_album_num_text, cursor='xterm')
        # button_to_2step=Button(self.window, text='下一步',command=self.second_interface,height=1, width=15, relief=RAISED, bd=4, activebackground='pink',
        #               activeforeground='white', cursor='hand2')
                      
        label_album_num.place(relx=0.12, rely=0.12, anchor=CENTER)
        # entry_album_num.place(relx=0.56, rely=0.12, anchor=CENTER)
        # button_to_2step.place(relx=0.80, rely=0.30, anchor=CENTER)

    def refresh(self):
        self.window.destroy()
        self.window=Tk()
        self.init_Window()


g=GUI()
# g.var_album_num_text

