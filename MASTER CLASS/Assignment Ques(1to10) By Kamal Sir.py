{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "960a3466",
   "metadata": {},
   "source": [
    "### Q1: A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dc1a8b0c",
   "metadata": {},
   "outputs": [],
   "source": [
    "S=int(input(\"Enter Your Salary:  \"))\n",
    "YOS=float(input(\"Enter Your Total Year Of Services:  \"))     ### YOS=Year Of Services\n",
    "Bonus=(S*5/100) \n",
    "\n",
    "\n",
    "if(YOS>5):\n",
    "    print(\"Congratulation! On your More Than Service Of 5 Years,You Have Been Given A Bonus Of 5% On Your Salary.\")\n",
    "    print(\"Your Net Bonus Amount is {:}\".format(Bonus))\n",
    "else:\n",
    "    print(\"Sorry! On your Less Than Service Of 5 Years,You Have not Been Given Any Bonus Of 5% On Your Salary\")\n",
    "    \n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "75f0ce19",
   "metadata": {},
   "source": [
    "### Q2: Take values of length and breadth of a rectangle from user and check if it is square or not"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1edb70d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter The Length:  36\n",
      "Enter The Breath:  56\n",
      "Length And Breath Are 36.0 And 56.0 Resp.\n",
      "The Length (36.0) And Breath(56.0) Are Not Equal,Hence Its A Rectangle\n"
     ]
    }
   ],
   "source": [
    "L=float(input(\"Enter The Length:  \"))\n",
    "B=float(input(\"Enter The Breath:  \"))\n",
    "\n",
    "print(\"Length And Breath Are {:} And {:} Resp.\".format(L,B))\n",
    "\n",
    "if(L==B):\n",
    "    print(\"The Length ({:}) And Breath({:}) Both Are Equal,Hence Its A Square\".format(L,B))\n",
    "else:\n",
    "    print(\"The Length ({:}) And Breath({:}) Are Not Equal,Hence Its A Rectangle\".format(L,B))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ea495a53",
   "metadata": {},
   "source": [
    "### Q3. Take two int values from user and print greatest among them.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e2de9847",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter The Value Of A:  5\n",
      "Enter The Value Of B:  4\n",
      "A(5) Is Greater Than B(4)\n"
     ]
    }
   ],
   "source": [
    "A=int(input(\"Enter The Value Of A:  \"))\n",
    "B=int(input(\"Enter The Value Of B:  \"))\n",
    "\n",
    "if(A>B):\n",
    "    print(\"A({:}) Is Greater Than B({:})\".format(A,B))\n",
    "else:\n",
    "    print(\"B({:}) Is Greater Than A({:})\".format(B,A))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3d94fc59",
   "metadata": {},
   "source": [
    "### 10 % discount on purchae of more than 1000 rs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b71e83e6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter The Total Items Or Units You Purchase:  50\n",
      "Each Quantity Cost 100 Rs.\n",
      "Congratulation! On Purchase of More than 1000 Rs.,you have been given A 10% Discount.\n",
      "Your Withou Discount Cost is: 5000\n",
      "Now,You Have To pay:  4500.0\n"
     ]
    }
   ],
   "source": [
    "Q=int(input(\"Enter The Total Items Or Units You Purchase:  \")) ##Quantity\n",
    "\n",
    "print(\"Each Quantity Cost 100 Rs.\")\n",
    "\n",
    "CPQ=Q*100   ###COQ=Cost Per Quantity\n",
    "Discount=CPQ-(CPQ*10/100)\n",
    "\n",
    "if(CPQ>1000):\n",
    "    print(\"Congratulation! On Purchase of More than 1000 Rs.,you have been given A 10% Discount.\")\n",
    "    print(\"Your Withou Discount Cost is: {:}\".format(CPQ))\n",
    "    print(\"Now,You Have To pay:  {:}\".format(Discount))\n",
    "else:\n",
    "    (\"You Will Not Get any Discount,As your Purchase Is less Than 1000\")\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a7403ac0",
   "metadata": {},
   "source": [
    "### Grading System"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "89cabec3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Your Marks:  52\n",
      "You Have Secured 52 % and You Got C grade\n"
     ]
    }
   ],
   "source": [
    "G=int(input(\"Enter Your Marks:  \"))\n",
    "\n",
    "if (G==100 and G>80):\n",
    "    print(\"You Have Secured {:} % and You Got A grade\".format(G))\n",
    "\n",
    "elif (G<=80 and G>60):\n",
    "    print(\"You Have Secured {:} % and You Got B grade\".format(G))\n",
    "\n",
    "elif (G<=60 and G>50):\n",
    "    print(\"You Have Secured {:} % and You Got C grade\".format(G))\n",
    "\n",
    "elif (G<=50 and G>45):\n",
    "    print(\"You Have Secured {:} % and You Got D grade\".format(G))\n",
    "\n",
    "elif (G<=45 and G>=25):\n",
    "    print(\"You Have Secured {:} % and You Got E grade\".format(G))\n",
    "\n",
    "elif (G<25):\n",
    "    print(\"You Have Secured {:} % and You are Failed \".format(G))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a5d19a44",
   "metadata": {},
   "source": [
    "### Insert 3 ages and Tell Whos is youngest And Older"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "21c7c957",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Your Age: a = 55\n",
      "Enter Your Age: b = 66\n",
      "Enter Your Age: c = 95\n",
      "c is oldest\n",
      "a is youngest\n"
     ]
    }
   ],
   "source": [
    "a = int(input(\"Enter Your Age: a = \"))\n",
    "b = int(input(\"Enter Your Age: b = \"))\n",
    "c = int(input(\"Enter Your Age: c = \"))\n",
    "if a > b and a > c :\n",
    "    if b > c :\n",
    "        print(\"a is oldest\")\n",
    "        print(\"c is youngest\")\n",
    "    else :\n",
    "        print(\"a is oldest\")\n",
    "        print(\"b is youngest\")\n",
    "elif b > a and b > c:\n",
    "    if a > c:\n",
    "        print(\"b is oldest\")\n",
    "        print(\"c is youngest\")\n",
    "    else :\n",
    "        print(\"b is oldest\")\n",
    "        print(\"a is youngest\")\n",
    "elif c > a and c > b:\n",
    "    if a > b:\n",
    "        print(\"c is oldest\")\n",
    "        print(\"b is youngest\")\n",
    "    else :\n",
    "        print(\"c is oldest\")\n",
    "        print(\"a is youngest\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a345453e",
   "metadata": {},
   "source": [
    "### Absolute Value "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "ee154153",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the Number:  -5\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "A=int(input(\"Enter the Number:  \"))\n",
    "Abs_Num=abs(A)\n",
    "print(Abs_Num)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c3c3fb3d",
   "metadata": {},
   "source": [
    "### More than 75% attandance,Student is eligible for exam"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "439d9f1e",
   "metadata": {},
   "outputs": [],
   "source": [
    "C=int(input(\"Enter Total Class Held In Annual Year:  \"))\n",
    "A=int(input(\"Enter Your Attandance:  \"))\n",
    "      \n",
    "\n",
    "      \n",
    "PCA=A/C\n",
    "print(\"Your Class Attandance is  {:%}\".format(PCA))\n",
    "\n",
    "PA=PCA*100\n",
    "    \n",
    "if(PA>=75):\n",
    "        print(\"You Are Eligible For Exam, As Your attandace is more than 75% (i.e) {:%}\".format(PCA))\n",
    "else:\n",
    "        print(\"Your Attandance is Less (i.e) {:%} , You Are Not Eligible For Exam \".format(PCA))\n",
    "\n",
    "      \n",
    "      "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "793486ff",
   "metadata": {},
   "source": [
    "### Check Leap Year Or Not ?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "f6d7b097",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter The Year:  2020\n",
      "Enter The Month2\n",
      "2 Month of 2020 Year Has 29 Days, Hence It is A leap Year. \n"
     ]
    }
   ],
   "source": [
    "Year=int(input(\"Enter The Year:  \"))\n",
    "M=int(input(\"Enter The Month\"))\n",
    "\n",
    "if(M==2):\n",
    "    if(Year%4==0):\n",
    "        if(Year%100==0):\n",
    "            if(Year%400==0):\n",
    "                print(\"{:} Month of {:} Year Has 29 Days, Hence It is A leap Year. \".format(M,Year))\n",
    "            else:\n",
    "                 print(\"{:} Month of {:} Year Has 28 Days, Hence It is not a leap Year. \".format(M,Year))\n",
    "        else:\n",
    "            print(\"{:} Month of {:} Year Has 29 Days, Hence It is A leap Year. \".format(M,Year))\n",
    "    else:\n",
    "        print(\"{:} Month of {:} Year Has 28 Days, Hence It is not a leap Year. \".format(M,Year))\n",
    "        \n",
    "else:\n",
    "    print(\"Enter Valid Month,This Month Cannot Come In Leap Month\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "90041d24",
   "metadata": {},
   "source": [
    "### Employ(Male And Female)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3845d07f",
   "metadata": {},
   "outputs": [],
   "source": [
    "A=int(input(\"Enter Your Age:  \"))\n",
    "\n",
    "print(\"For Female use 'F' and For Male Use 'M' \")\n",
    "\n",
    "S=str(input(\"Enter Your Sex:  \"))\n",
    "\n",
    "M=str(input(\"Your Maritial Status:  \"))\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "if(S=='F'):\n",
    "    print(\"You Are {:},You Work Only in Urban Areas\".format(S))\n",
    "elif(S=='M' and A>=20 and A<=40):\n",
    "    print(\"You are {:} of Age{:},You may work Anywhere\".format(S,A))\n",
    "elif(S=='M' and A>=40 and A<=60):\n",
    "    print(\"You are {:} of Age{:},You may work in Urban Areas Only\".format(S,A))\n",
    "else:\n",
    "    print(\"Error,No jobs For you,Sorry!\")\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
