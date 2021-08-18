"""
*Author : Revanth Sai Nandamuri
*GitHUB : https://github.com/RevanthNandamuri1341b0
*Date of update : 18 August 2021
*Project name : My First calculator 2.0
*Domain : PYTHON
*Description : This code generates a Hard code for the calculator code
*File Name : generator.py
*File ID : 115173
*Modified by : #your name#
"""


def add(n):
    for i in range(n+1):
        for j in range(n+1):
            print("if num1 == ", i, " and sign == '+' and num2 == ", j, ":")
            print("\tprint('", i, "+", j, "=", i+j, "')")


def sub(n):
    for i in range(n+1):
        for j in range(n+1):
            print("if num1 == ", i, " and sign == '-' and num2 == ", j, ":")
            print("\tprint('", i, "-", j, "=", i-j, "')")


def mul(n):
    for i in range(n+1):
        for j in range(n+1):
            print("if num1 == ", i, " and sign == '*' and num2 == ", j, ":")
            print("\tprint('", i, "*", j, "=", i*j, "')")


def div(n):
    for i in range(n+1):
        for j in range(n+1):
            print("if num1 == ", i, " and sign == '/' and num2 == ", j, ":")
            if j == 0:
                print("\tprint('Cant be divided with 0')")
                continue
            else:
                print("\tprint('", i, "/", j, "=", i/j, "')")


n = int(input("Enter The Limit of your calculator input : "))
print("=================COPY BELOW CODE==================\n")
add(n)
sub(n)
mul(n)
div(n)
print("\n==================================================")
