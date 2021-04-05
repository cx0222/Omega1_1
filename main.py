import cut
import yagmail
import matplotlib.pyplot
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
from tkinter import *
from PIL import Image, ImageTk

ver, OS = '1.1', 'macOS 11'


def plot(triangle_plot):
    triangle_count = triangle_plot.__len__()
    matplotlib.pyplot.figure('多边形分割结果')
    for j in range(0, triangle_count):
        triangle_x = [triangle_plot[j][0][0], triangle_plot[j][1][0], triangle_plot[j][2][0], triangle_plot[j][0][0]]
        triangle_y = [triangle_plot[j][0][1], triangle_plot[j][1][1], triangle_plot[j][2][1], triangle_plot[j][0][1]]
        matplotlib.pyplot.fill(triangle_x, triangle_y, 'o-')
    matplotlib.pyplot.show()


# noinspection PyGlobalUndefined
def window():
    window0 = Tk()
    window0.title('多边形分割小程序  1.1 macOS 版')
    window0.geometry('800x400')
    window0.resizable(False, False)
    canvas1 = tk.Canvas(window0, highlightthickness=0, width=800, height=400, bg='white')
    canvas1.pack(fill=BOTH, expand=YES)

    def _info_():
        str0 = '\n基于Python 3开发的 多边形分割小程序（测试版）\n' \
               ' -------- -------- -------- -------- -------- -------- -------- --------\n\n' \
               ' [开发团队] \n' \
               ' DLK  湖北省孝感市\n' \
               ' Nova cx0222  山东省济南市\n' \
               ' [联系方式] \n' \
               ' 2913026224@qq.com, 1929842479@qq.com\n' \
               ' -------- -------- -------- -------- -------- -------- -------- --------\n' \
               ' [当前版本] \n' \
               ' 1.1 macOS 版  2021年4月4日  北京市昌平区\n' \
               ' [早期版本] \n' \
               ' 1.0 macOS 版  2021年4月4日  北京市昌平区\n' \
               ' 0.1 macOS 版  2021年4月3日  北京市昌平区\n' \
               ' -------- -------- -------- -------- -------- -------- -------- --------\n' \
               ' [运行环境] \n' \
               ' macOS 11.2.2 or later \n' \
               ' Ubuntu Linux 20.04 or later \n' \
               ' Windows 7 or later \n'
        return str0

    def _exit_():
        window0.quit()
        window0.destroy()

    def _all_():
        window1 = tk.Toplevel()
        window1.geometry('800x400')
        window1.resizable(False, False)
        tk.Label(window1, text=_info_(), font=('Arial', 16)).pack()
        window1.mainloop()

    def _about_():
        window2 = tk.Toplevel()
        window2.geometry('800x400')
        window2.resizable(False, False)
        bg0 = ImageTk.PhotoImage(Image.open('ver1_1_about.gif'))
        canvas0 = tk.Canvas(window2, width=800, height=400, bg='white')
        canvas0.create_image(400, 200, image=bg0)
        canvas0.pack()
        window2.mainloop()

    def _report_():
        window9 = tk.Toplevel()
        window9.title('多边形分割小程序  1.1版  反馈系统')
        window9.geometry('800x600')
        window9.resizable(False, False)
        bg0 = ImageTk.PhotoImage(Image.open('ver1_1_report.gif'))
        canvas0 = tk.Canvas(window9, width=800, height=400, bg='white')
        canvas0.create_image(400, 200, image=bg0)
        title9_1 = tk.Label(window9,
                            text='请输入您遇到的问题，我们将认真考虑您的意见与建议！',
                            font=('Arial', 18))
        entry1 = tk.Entry(window9, width=80)
        title2 = tk.Label(window9,
                          text='如果您愿意，请您留下您的联系方式，我们将会与您联系。',
                          font=('Arial', 18))
        entry2 = tk.Entry(window9, width=80)
        report1 = tk.Button(window9, text='发送至官方邮箱', command=lambda: _sent_(entry1.get(), entry2.get()))

        canvas0.pack(), title9_1.pack(), entry1.pack(), title2.pack(), entry2.pack()
        report1.place(relheight=0.05, relwidth=0.15, relx=0.425, rely=0.90)
        window9.mainloop()

    def _main_(split, view_mode):
        list_input = _read_(split=split)
        triangle_list, point_extinguish = [], []
        while True:
            print(list_input)
            triangle_list.append(cut.cut_once(list_input=list_input))
            list_input_1 = []
            for i in range(0, list_input.__len__()):
                if list_input[i] != triangle_list[-1][1]:
                    list_input_1.append(list_input[i])
            list_input = list_input_1
            if view_mode == 1:
                plot(triangle_plot=triangle_list)
            if list_input.__len__() == 2:
                plot(triangle_plot=triangle_list)
                break

    # noinspection PyGlobalUndefined
    def _read_(split):
        file_name = tkinter.filedialog.askopenfilename()
        point_read = []
        if split == 0:
            char = ','
        elif split == 2:
            char = ', '
        elif split == 3:
            char = ' ,'
        else:
            char = ' '
        if split != 1:
            with open('{0}'.format(file_name), 'r') as file:
                for point in file.readlines():
                    coordinate = point.split(char)
                    point_read.append([float(coordinate[0]), float(coordinate[1])])
                print(point_read)
        else:
            with open('{0}'.format(file_name), 'r') as file:
                for point in file.readlines():
                    coordinate = point.split()
                    point_read.append([float(coordinate[0]), float(coordinate[1])])
                print(point_read)
        return point_read

    def Control_r(event):
        _main_(split=get_delimiter(), view_mode=get_mode())

    def Control_f(event):
        _report_()

    def get_delimiter():
        delimiter_get = delimiter.get()
        return delimiter_get

    def get_mode():
        mode_get = mode.get()
        return mode_get

    def _sent_(str0, str1):
        report_ask = tkinter.messagebox.askokcancel(
            title='请问您确定发送吗？', message='本报告仅存储软件版本、运行环境以及您的意见、建议，不包含任何隐私信息。')
        if report_ask:
            yag = yagmail.SMTP('gdsb7770002@163.com', 'QMMYHEMPBVPHYAII', 'smtp.163.com')
            yag.send(['2913026224@qq.com', '1929842479@qq.com'], '{0}版本用户反馈'.format(ver),
                     ['意见建议：{0}\n'.format(str0),
                      '联系方式：{0}\n'.format(str1),
                      '版本信息：{0} based on {1}\n'.format(ver, OS)])
            tkinter.messagebox.showinfo(
                title='您已发出，感谢您的反馈！', message='您已成功发送！')
        else:
            tkinter.messagebox.showinfo(
                title='您已取消发送！', message='您已取消发送！')

    title0 = tk.Label(
        canvas1, text='\n基于Python 3开发的 多边形分割小程序（测试版）', font=('Arial', 25))
    title0.place(height=60, width=650, x=80, y=0)
    title1 = tk.Label(
        canvas1, text='\n1.1 macOS 版  2021年4月4日  北京市昌平区，湖北省荆州市荆州区', font=('Arial', 17))
    title1.place(height=40, width=650, x=80, y=55)

    menu0 = tk.Menu(window0)
    window0.config(menu=menu0)
    menu_1 = tk.Menu(menu0, tearoff=False)
    menu0.add_cascade(label='操作', menu=menu_1)
    menu_1.add_command(label='分割  ',
                       command=lambda: _main_(split=get_delimiter(), view_mode=get_mode()),
                       accelerator='Command+r')
    menu_1.add_separator()
    menu_1.add_command(label='退出  ', command=_exit_, accelerator='Control+q')
    menu_2 = tk.Menu(menu0, tearoff=False)
    menu_2.add_command(label='说明  ', command=_about_)
    menu_2.add_command(label='关于  ', command=_all_)
    menu_2.add_command(label='反馈  ', command=_report_, accelerator='Command+f')
    menu0.add_cascade(label='帮助  ', menu=menu_2)

    about0 = tk.Button(canvas1, text='说    明', command=_about_)
    about0.place(height=30, width=120, x=230, y=120)
    note0 = tk.Button(canvas1, text='关    于', command=_all_)
    note0.place(height=30, width=120, x=450, y=120)

    delimiter_group = LabelFrame(canvas1, text=' 请选择分割符：')
    delimiter_group.place(height=130, width=180, x=282.5, y=170)
    delimiter = IntVar()
    delimiter.set(0)
    delimiter0 = Radiobutton(delimiter_group, text='英文逗号', variable=delimiter, value=0, command=get_delimiter)
    delimiter0.place(x=10, y=8)
    delimiter1 = Radiobutton(delimiter_group, text='半角空格', variable=delimiter, value=1, command=get_delimiter)
    delimiter1.place(x=10, y=30)
    delimiter2 = Radiobutton(delimiter_group, text='英文逗号+半角空格', variable=delimiter, value=2, command=get_delimiter)
    delimiter2.place(x=10, y=52)
    delimiter3 = Radiobutton(delimiter_group, text='半角空格+英文逗号', variable=delimiter, value=3, command=get_delimiter)
    delimiter3.place(x=10, y=74)

    mode_group = LabelFrame(canvas1, text=' 请选择显示模式：')
    mode_group.place(height=130, width=180, x=500, y=170)
    mode = IntVar()
    mode.set(0)
    mode0 = Radiobutton(mode_group, text='只显示最终结果', variable=mode, value=0, command=get_mode)
    mode0.place(x=10, y=19)
    mode1 = Radiobutton(mode_group, text='显示整个过程', variable=mode, value=1, command=get_mode)
    mode1.place(x=10, y=57)

    cut0 = tk.Button(canvas1, text='分    割', command=lambda: _main_(split=get_delimiter(), view_mode=get_mode()))
    cut0.place(height=30, width=120, x=120, y=220)
    cut0.bind_all('<Command-r>', Control_r)
    cut0.bind_all('<Control-r>', Control_r)
    report0 = tk.Button(canvas1, text='反    馈', command=_report_)
    report0.place(height=30, width=120, x=230, y=326)
    report0.bind_all('<Command-f>', Control_f)
    report0.bind_all('<Control-f>', Control_f)
    exit0 = tk.Button(canvas1, text='退    出', command=_exit_)
    exit0.place(height=30, width=120, x=450, y=326)

    window0.mainloop()


window()
