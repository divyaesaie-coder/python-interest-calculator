#Write a program to calculate simple and compound interest.

p=int(input("ENTER THE PRINCIPAL AMOUNT:"))
r=float(input("ENTER THE RATE OF INTREST:"))
t=int(input("ENTER HOW MANY YEARS :"))
simple_intrest=(p*r*t)/100
amt=p*(1+t/100)**t
compound_intrest=amt-p
print("SIMPLE INTREST:",simple_intrest)
print("COMPOUND INTREST:",compound_intrest)
