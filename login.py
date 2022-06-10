####카카오톡 로그인하기 + 회원가입하기(tkinter 사용)####

​

from tkinter import * #GUI 관련 모듈을 제공해주는 라이브러리

import tkinter.messagebox #메시지 창 사용

​

window = Tk() #윈도우 창 생성

window.title("카카오톡 로그인하기") #윈도우 창에 제목 표시

window.geometry("500x700") #윈도우 창 크기

window.resizable(width = FALSE, height = FALSE) #가로와 세로의 크기가 변경 되지 않도록 설정

window.option_add("*Font", "굴림 20") #윈도우 창의 기본 글꼴 설정

​

ididid = ""

pwpwpw = ""

​

tkinter.messagebox.showinfo("회원가입", "회원가입을 먼저 하세요.")

​

def erase(event) : #클릭 했을때 입력창에 있는 temp@temp.com 예시를 다 지우는 함수

if enter_id.get() == "subin@subin.com" : #만약 입력한 아이디가 subin@subin.com 이면

enter_id.delete(0, len(enter_id.get())) #subin@subin.com의 처음 글자 부터 길이 지우기

​

def login_id_password_right() : #로그인한 아이디와 비밀번호가 일치하는지 확인하는 함수

if enter_id.get() == ididid and enter_pw.get() == pwpwpw: #입력한 아이디와 비밀번호가 설정한 아이디와 비밀번호가 일치하면

tkinter.messagebox.showinfo("로그인", "로그인을 성공하였습니다.") #로그인을 성공하였습니다 메시지창 띄우기

else:

tkinter.messagebox.showinfo("로그인", "아이디/비밀번호가 틀렸습니다. 다시 로그인 하세요.") #로그인 실패 메시지창 띄우기

​

​

def signup() : #회원가입 함수

window2 = Tk() #윈도우 창 생성

window2.title("카카오톡 회원가입하기") #윈도우 창에 제목 표시

window2.geometry("300x100") #윈도우 창 크기

window2.resizable(width = FALSE, height = FALSE) #가로와 세로의 크기가 변경 되지 않도록 설정

window2.option_add("*Font", "굴림 10") #윈도우 창의 기본 글꼴 설정

​

def clickbtn(event):

global ididid #login_id_password_right 함수에서 ididid 변수 사용하기위해 전역 변수를 씀

global pwpwpw #login_id_password_right 함수에서 pwpwpw 변수 사용하기 위해 전역 변수를 씀

ididid=enter_new_id.get() #문자열로 변환 후 전역변수에 대입(아이디)

pwpwpw=enter_new_pw.get() #문자열로 변환 후 전역변수에 대입(비밀번호)

​

if ididid == "" or pwpwpw == "":

tkinter.messagebox.showinfo("오류", "아이디와 비밀번호는 한 글자 이상이어야 합니다.")

else :

tkinter.messagebox.showinfo("로그인", "회원가입을 완료하였습니다.")

​

#window.destroy() #메세지 출력 후 창닫기

​

new_id = Label(window2, text = "새로 만들 아이디를 입력하세요 : ") #새로 만들 아이디를 입력하세요 입력 받아 변수에 저장

new_id.pack() #새로 만들 아이디 문구 출력

enter_new_id = Entry(window2) #아이디 입력 창에 입력

enter_new_id.pack() #입력 받은 아이디 출력

​

new_pw = Label(window2, text = "새로 만들 비밀번호를 입력하세요 : ") #새로 만들 비밀번호를 입력하세요 입력 받아 변수에 저장

new_pw.pack() #새로 만들 비밀번호 문구 출력

enter_new_pw = Entry(window2, show = "*") #비밀번호 입력할때 *모양으로 출력됨

enter_new_pw.pack() #입력 받은 비밀번호 출력

​

btn = Button(window2, text = "회원가입하기") #회원가입하기 버튼 생성

btn.pack() #회원가입하기 버튼 출력

​

btn.bind("<Button>", clickbtn) #마우스 클릭하면 마우스 작동

btn.pack(expand = 1, anchor = CENTER) #마우스 버튼 출력

​

#윈도우 창의 카카오톡 이미지 

label = Label(window) #라벨 만들기

img = PhotoImage(file = "카카오.gif") #카카오톡 이미지를 img 변수에 저장

label.config(image=img) 

label.pack()

​

id_label = Label(window) #아이디 라벨 만듬

id_label.config(text = "아이디") #라벨에 아이디라는 글자 표시

id_label.pack() #'아이디' 출력

​

enter_id = Entry(window) #아이디 입력창

enter_id.insert(0, "subin@subin.com") #subin@subin.com의 위치가 0(처음(가장 왼쪽))에 표시

enter_id.bind("<Button>", erase) #아이디 입력창에 누르면 subin@subin.com 사라짐

enter_id.pack() #입력한 아이디 출력

​

pw_label = Label(window) #비밀번호 라벨 만듬

pw_label.config(text = "비밀번호") #라벨에 비밀번호라는 글자 표시

pw_label.pack() #'비밀번호' 출력

​

enter_pw = Entry(window) #비밀번호 입력창

enter_pw.config(show = "*") #비밀번호 입력할 때 개인정보 보호를 위해 "*"모양으로 표시

enter_pw.pack() #출력

​

button1 = Button(window, text = "회원가입 하기") #회원가입하는 버튼 생성

button1.config(command = signup)

button1.pack() #출력

​

button2 = Button(window, text = "로그인") #로그인하는 버튼 생성

button2.config(command = login_id_password_right) #로그인할때 아이디와 비번이 일치하는지 확인

button2.pack() #출력

​

​

window.mainloop()
