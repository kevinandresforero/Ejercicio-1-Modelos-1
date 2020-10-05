#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 07:47:15 2020

@author: KEV
"""

from marco import *
import tkinter as tk
from tkinter import Canvas

class ventana:
    def __init__():
        __marco__ = marco.__init__()
        ln = tk.Label(__marco__, text ="A continución digíte el grado de la Función",bg="black",fg="yellow").pack(
            padx=3,pady=3,ipadx=2,ipady=20,fill=tk.X)
        cn = tk.Entry(__marco__, bg="blue",fg="yellow")
        cn.pack()
        __marco__.mainloop()
    
        def cargarn():
    
            def cargarv():
                coe = list(range(labeln))
                for i in range(labeln):
                    coe[i] = camTex[i].get()
    
                lx = tk.Label(__marco__, text="Cargar el número a evaluar la función Función",bg="black",fg="yellow")
                lx.pack()
                lx.place(x=100,y= labeln*h+12*h+75)
                x = tk.Entry(__marco__,bg="blue",fg="yellow")
                x.pack()
                x.place(x=100,y= labeln*h+12*h+100)
    
                def evalua():
                    r=0
                    for i in range(labeln):
                        r = r + (float(x.get())**i) * float(coe[i])
                    lr = tk.Label(__marco__, text="El Resultado de la función evaluada en "+str(x.get())+" es : "+
                                              str(r),bg="black",fg="yellow")
                    lr.place(x=100,y= labeln*h+12*h+160)
    
    
                cargarx = tk.Button(__marco__, text="Evaluar",bg="Blue",fg="yellow",command=evalua)
                cargarx.place(x=100,y= labeln*h+12*h+125)
    
            lcoe = tk.Label(__marco__, text ="A continución digíte cada coeficiente de las variables",bg="Black",fg="yellow").pack(
                padx=3,pady=3,ipadx=2,ipady=20,fill=tk.X)
            labeln = int(cn.get())
            h = 15
            labelv = list(range(labeln))
            camTex = list(range(labeln))
            r = 0
            for i in range(labeln):
                labelv[i] = tk.Label(__marco__, text="X:"+str(i),bg="black",fg="red")
                labelv[i].pack()
                labelv[i].place(x=100,y=i*h+12*h)
                camTex[i] = tk.Entry(__marco__, bg="blue",fg="yellow")
                camTex[i].pack(ipady=30)
                camTex[i].place(x=167 , y= i*h+12*h)
            cargarv = tk.Button(__marco__, text="Cargar Variables",bg="Blue",fg="yellow",command=cargarv)
            cargarv.pack()
            cargarv.place(x=100,y= labeln*h+12*h+25)
    
        cargarn = tk.Button(__marco__, text="Cargar El Grado de la Función",bg="Blue",fg="yellow",command=cargarn).pack(pady=5)
    
        __marco__.mainloop()