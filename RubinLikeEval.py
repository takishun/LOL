import tkinter
import tkinter.messagebox

def close_window():
	tki.destroy()
	
def point_cal():
	total = 0
	for i in s:
		total+=i.get()
	print(total)
	return total

def judge_point(n):
	"""
	点数評価をする関数
	点数により評価を振り分ける
	"""
	if n == 0:
		txt = "何とも思っていない"
		return txt
	elif 0<n<6:
		txt = "割と好きかな"
		return txt
	elif 5<n<11:
		txt = "好き！"
		return txt
	elif 10<n<19:
		txt = "超大好き！"
		return txt
	else:
		return "error"
	return 0

def btn_click():
	num = point_cal()
	eval_txt = judge_point(num)
	return text_str.set(judge_point(num))

tki = tkinter.Tk()
tki.geometry('500x800')
tki.title('ルービンの好意尺度測定アプリ')
ybar = tkinter.Scrollbar(tki,orient=tkinter.VERTICAL,)

select = ['そう思わない','まあ、そう思う','すごくそう思う']

#status of radio button
select_var = tkinter.IntVar()
s = [0] * 12
for i in range(0,12):
	s[i] = tkinter.IntVar()
	s[i].set(0)

for i in range(len(select)):

	text_str_1 = tkinter.StringVar()
	text_str_1.set('1.OOさんはとっても適応力がある人だと思う。')
	text1 = tkinter.Label(textvariable=text_str_1)
	text1.place(x=30,y=10)
	rdo1 = tkinter.Radiobutton(tki,value=i,variable=s[0],text=select[i])
	rdo1.place(x=50+i*125,y=30)
	
	text_str_2 = tkinter.StringVar()
	text_str_2.set('2.OOさんは責任ある仕事に推薦できる人だと思う。')
	text2 = tkinter.Label(textvariable=text_str_2)
	text2.place(x=30,y=70)
	rdo2 = tkinter.Radiobutton(tki,value=i,variable=s[1],text=select[i])
	rdo2.place(x=50+i*125,y=90)
		
	text_str_3 = tkinter.StringVar()
	text_str_3.set('3.OOさんをすごくよくできた人だと思う。')
	text3 = tkinter.Label(textvariable=text_str_3)
	text3.place(x=30,y=130)
	rdo3 = tkinter.Radiobutton(tki,value=i,variable=s[2],text=select[i])
	rdo3.place(x=50+i*125,y=150)
	
	text_str_4 = tkinter.StringVar()
	text_str_4.set('4.OOさんは判断力があり、すごく信頼している。')
	text4 = tkinter.Label(textvariable=text_str_4)
	text4.place(x=30,y=190)
	rdo4 = tkinter.Radiobutton(tki,value=i,variable=s[3],text=select[i])
	rdo4.place(x=50+i*125,y=210)

	text_str_5 = tkinter.StringVar()
	text_str_5.set('5.グループでなにかの選挙があれば、OOさんに投票する。')
	text5 = tkinter.Label(textvariable=text_str_5)
	text5.place(x=30,y=250)	
	rdo5 = tkinter.Radiobutton(tki,value=i,variable=s[4],text=select[i])
	rdo5.place(x=50+i*125,y=270)

	text_str_6 = tkinter.StringVar()
	text_str_6.set('6.OOさんはみんなから尊敬される人だと思う。')
	text6 = tkinter.Label(textvariable=text_str_6)
	text6.place(x=30,y=310)
	rdo6 = tkinter.Radiobutton(tki,value=i,variable=s[5],text=select[i])
	rdo6.place(x=50+i*125,y=330)
	
	text_str_7 = tkinter.StringVar()
	text_str_7.set('7.OOさんはとても頭がいいと思う。')
	text7 = tkinter.Label(textvariable=text_str_7)
	text7.place(x=30,y=370)	
	rdo7 = tkinter.Radiobutton(tki,value=i,variable=s[6],text=select[i])
	rdo7.place(x=50+i*125,y=390)
	
	text_str_8 = tkinter.StringVar()
	text_str_8.set('8.私はOOさんみたいな人になりたいと思う。')
	text8 = tkinter.Label(textvariable=text_str_8)
	text8.place(x=30,y=430)
	rdo8 = tkinter.Radiobutton(tki,value=i,variable=s[7],text=select[i])
	rdo8.place(x=50+i*125,y=450)

	text_str_9 = tkinter.StringVar()
	text_str_9.set('9.OOさんはみんなから尊敬される人物だと思う。')
	text9 = tkinter.Label(textvariable=text_str_9)
	text9.place(x=30,y=490)	
	rdo9 = tkinter.Radiobutton(tki,value=i,variable=s[8],text=select[i])
	rdo9.place(x=50+i*125,y=510)

btn = tkinter.Button(tki,text='診断',command=btn_click)
btn.place(x=160,y=600)
text_str = tkinter.StringVar()
text_str.set('ボタンを押してください。')
text = tkinter.Label(textvariable=text_str)
text.place(x=160,y=650)

btn_quit = tkinter.Button(tki,text = '終了',command=close_window)
btn_quit.place(x=250,y=600)

tki.mainloop()
