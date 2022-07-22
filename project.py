import streamlit as st
import sqlite3 as s3
import pandas as pd
import os.path

st.sidebar.header('내신등급 산출기')
MENU=st.sidebar.selectbox('MENU',options=['전 학년 내신등급 산출','학년 내신등급 산출','학기 내신등급 산출'])


if MENU == '전 학년 내신등급 산출':
    st.header('전 학년 내신등급 산출')
    st.info('학년별 내신등급과 내신반영비율을 입력하세요.')
    st.subheader('1학년')
    self_1 = st.number_input('1학년 내신등급을 입력하세요.',min_value=1.00,max_value=10.00,step=0.01)
    pro_1 = st.number_input('1학년 내신 반영비율을 입력하세요.(%)',min_value=0,step=5)
    st.subheader('2학년')
    self_2 = st.number_input('2학년 내신등급을 입력하세요.',min_value=1.00,max_value=10.00,step=0.01)
    pro_2 = st.number_input('2학년 내신 반영비율을 입력하세요.(%)',min_value=0,step=5)
    st.subheader('3학년')
    self_3 = st.number_input('3학년 내신등급을 입력하세요.',min_value=1.00,max_value=10.00,step=0.01)
    pro_3 = st.number_input('3학년 내신 반영비율을 입력하세요.(%)',min_value=0,step=5)
    if pro_1+pro_2+pro_3 == 100:
        go_btn = st.button('확인')
        if go_btn:
            st.success('당신의 내신등급은 '+str((self_1*pro_1)/100+(self_2*pro_2)/100+(self_3*pro_3)/100)+'등급입니다.')
            st.warning('주의 : 실제 내신등급과 차이가 있을 수 있습니다!')
    else:
        st.caption('내신 반영비율이 유효하지 않습니다.')


if MENU == '학년 내신등급 산출':
    st.header('학년 내신등급 산출')
    st.info('학기별 내신등급과 수강 단위수를 입력하세요.')
    st.subheader('1학기')
    se_1 = st.number_input('1학기 내신등급을 입력하세요.', min_value=1.00, max_value=10.00, step=0.01)
    pr_1 = st.number_input('1학기 수강 단위수를 입력하세요.',min_value=0, step=1)
    st.subheader('2학기')
    se_2 = st.number_input('2학기 내신등급을 입력하세요.', min_value=1.00, max_value=10.00, step=0.01)
    pr_2 = st.number_input('2학기 수강 단위수를 입력하세요.',min_value=0, step=1)
    if pr_1 != 0 and pr_2 != 0:
        g_btn = st.button('확인')
        if g_btn:
            st.success('당신의 내신등급은 '+str(round((se_1*pr_1)/(pr_1+pr_2)+(se_2*pr_2)/(pr_1+pr_2),2))+'등급입니다.')
            st.warning('주의 : 실제 내신등급과 차이가 있을 수 있습니다!')
    else:
        st.caption('수강 단위수가 유효하지 않습니다.')


if MENU == '학기 내신등급 산출':
    st.header('학기 내신등급 산출')
    st.info('과목별 내신등급과 수강 단위수를 입력하세요.')
    st.subheader('과목 1')
    sub1 = st.number_input('과목 1의 내신등급을 입력하세요.', min_value=1, max_value=9, step=1)
    pr1 = st.number_input('과목 1의 단위수를 입력하세요.',min_value=0, step=5)
    st.subheader('과목 2')
    sub2 = st.number_input('과목 2의 내신등급을 입력하세요.', min_value=1, max_value=9, step=1)
    pr2 = st.number_input('과목 2의 단위수를 입력하세요.',min_value=0, step=5)
    st.subheader('과목 3')
    sub3 = st.number_input('과목 3의 내신등급을 입력하세요.', min_value=1, max_value=9, step=1)
    pr3 = st.number_input('과목 3의 단위수를 입력하세요.',min_value=0, step=5)
    st.subheader('과목 4')
    sub4 = st.number_input('과목 4의 내신등급을 입력하세요.', min_value=1, max_value=9, step=1)
    pr4 = st.number_input('과목 4의 단위수를 입력하세요.',min_value=0, step=5)
    st.subheader('과목 5')
    sub5 = st.number_input('과목 5의 내신등급을 입력하세요.', min_value=1, max_value=9, step=1)
    pr5 = st.number_input('과목 5의 단위수를 입력하세요.',min_value=0, step=5)
    st.subheader('과목 6')
    sub6 = st.number_input('과목 6의 내신등급을 입력하세요.', min_value=1, max_value=9, step=1)
    pr6 = st.number_input('과목 6의 단위수를 입력하세요.',min_value=0, step=5)
    st.subheader('과목 7')
    sub7 = st.number_input('과목 7의 내신등급을 입력하세요.', min_value=1, max_value=9, step=1)
    pr7 = st.number_input('과목 7의 단위수를 입력하세요.',min_value=0, step=5)
    st.subheader('과목 8')
    sub8 = st.number_input('과목 8의 내신등급을 입력하세요.', min_value=1, max_value=9, step=1)
    pr8 = st.number_input('과목 8의 단위수를 입력하세요.',min_value=0, step=5)
    st.subheader('과목 9')
    sub9 = st.number_input('과목 9의 내신등급을 입력하세요.', min_value=1, max_value=9, step=1)
    pr9 = st.number_input('과목 9의 단위수를 입력하세요.',min_value=0, step=5)
    st.subheader('과목 10')
    sub10 = st.number_input('과목 10의 내신등급을 입력하세요.', min_value=1, max_value=9, step=1)
    pr10 = st.number_input('과목 10의 단위수를 입력하세요.',min_value=0, step=5)
    st.subheader('과목 11')
    sub11 = st.number_input('과목 11의 내신등급을 입력하세요.', min_value=1, max_value=9, step=1)
    pr11 = st.number_input('과목 11의 단위수를 입력하세요.',min_value=0, step=5)
    st.subheader('과목 12')
    sub12 = st.number_input('과목 12의 내신등급을 입력하세요.', min_value=1, max_value=9, step=1)
    pr12 = st.number_input('과목 12의 단위수를 입력하세요.',min_value=0, step=5)
    st.subheader('과목 13')
    sub13 = st.number_input('과목 13의 내신등급을 입력하세요.', min_value=1, max_value=9, step=1)
    pr13 = st.number_input('과목 13의 단위수를 입력하세요.',min_value=0, step=5)
    sum = pr1+pr2+pr3+pr4+pr5+pr6+pr7+pr8+pr9+pr10+pr11+pr12+pr13
    good = sub1*pr1 + sub2*pr2 + sub3*pr3 + sub4*pr4 + sub5*pr5 + sub6*pr6 + sub7*pr7 + sub8*pr8 + sub9*pr9 + sub10*pr10 + sub11*pr11 + sub12*pr12 + sub13*pr13
    if sum != 0:
        gbtn = st.button('확인')
        if gbtn:
            st.success('당신의 학기 수강 단위수는 '+str(sum)+'이며, '+'당신의 학기 내신등급은 '+str(round((good/sum),2))+'등급입니다.')
            st.warning('주의 : 실제 내신등급과 차이가 있을 수 있습니다!')
    else:
        st.caption('단위수가 유효하지 않습니다.')



