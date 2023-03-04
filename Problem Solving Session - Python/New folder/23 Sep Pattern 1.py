{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1\n",
    "11\n",
    "111\n",
    "1111\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "1\n",
      "11\n",
      "111\n",
      "1111\n",
      "11111\n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "row=1\n",
    "while row<=n:\n",
    "    col=1\n",
    "    while col<=row:\n",
    "        print(1,end=\"\")\n",
    "        col=col+1\n",
    "    row=row+1\n",
    "    print() "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Number Pattern 2\n",
    "Send Feedback\n",
    "Print the following pattern for the given N number of rows.\n",
    "Pattern for N = 4\n",
    "1\n",
    "11\n",
    "202\n",
    "3003"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "1\n",
      "11\n",
      "202\n",
      "3003\n",
      "40004\n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "print(1)\n",
    "row=1\n",
    "while row<n:  #  pattern row printed upto one less , for example N=4 then 3\n",
    "    col=0\n",
    "    while col<row+1: # row 1 has 2 cols, row 2 has 3 cols etc.\n",
    "        if(col==0 or col==row):\n",
    "            print(row,end=\"\")\n",
    "        else:\n",
    "            print(0,end=\"\")\n",
    "        col=col+1\n",
    "    row=row+1\n",
    "    print()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Number Pattern 3\n",
    "Send Feedback\n",
    "Print the following pattern for the given N number of rows.\n",
    "Pattern for N = 4\n",
    "1\n",
    "11\n",
    "121\n",
    "1221"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "1\n",
      "11\n",
      "121\n",
      "1221\n",
      "12221\n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "print(1)\n",
    "row=1\n",
    "while row<n:  #  pattern row printed upto one less , for example N=4 then 3\n",
    "    col=0\n",
    "    while col<row+1: # row 1 has 2 cols, row 2 has 3 cols etc.\n",
    "        if(col==0 or col==row):\n",
    "            print(1,end=\"\")\n",
    "        else:\n",
    "            print(2,end=\"\")\n",
    "        col=col+1\n",
    "    row=row+1\n",
    "    print()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Number Pattern\n",
    "Send Feedback\n",
    "Print the following pattern for the given N number of rows.\n",
    "Pattern for N = 4\n",
    "1234\n",
    "123\n",
    "12\n",
    "1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "12345\n",
      "1234\n",
      "123\n",
      "12\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "row=n\n",
    "while row>=1:\n",
    "    col=1\n",
    "    while col<=row:\n",
    "        print(col,end=\"\")\n",
    "        col=col+1\n",
    "    row=row-1\n",
    "    print() "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Alpha Pattern\n",
    "Send Feedback\n",
    "Print the following pattern for the given N number of rows.\n",
    "Pattern for N = 3\n",
    " A\n",
    " BB\n",
    " CCC"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "A\n",
      "BB\n",
      "CCC\n",
      "DDDD\n",
      "EEEEE\n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "num=64\n",
    "row=1\n",
    "while row<=n:\n",
    "    col=1\n",
    "    while col<=row:\n",
    "        print(chr(num+row),end=\"\")\n",
    "        col=col+1\n",
    "    row=row+1\n",
    "    print() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "A\n",
      "AB\n",
      "ABC\n",
      "ABCD\n",
      "ABCDE\n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "num=64\n",
    "row=1\n",
    "while row<=n:    \n",
    "    col=1\n",
    "    while col<=row:\n",
    "       # ch=chr(num)\n",
    "        print(chr(num+col),end=\"\")\n",
    "        col=col+1\n",
    "    row=row+1\n",
    "    print() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "55555\n",
      "55555\n",
      "55555\n",
      "55555\n",
      "55555\n"
     ]
    }
   ],
   "source": [
    "#Examples:\n",
    "N=int(input()) #Take user input, N= Number of Rows\n",
    "row=1; #The loop starts with the 1st row\n",
    "while row<=N: #Loop will on for N rows\n",
    "    col=1; #The loop starts with the first column in the current row\n",
    "    while col<=N: #Loop will on for N columns\n",
    "        print(N,end=\"\") #Printing a (*) in all columns\n",
    "        col=col+1 #Increment the current column (Inner Loop)\n",
    "    row=row+1 #Increment the current row (Outer Loop)\n",
    "    print() #Add a new Line after each row is printed"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "*\n",
      "**\n",
      "***\n",
      "****\n"
     ]
    }
   ],
   "source": [
    "#Code : Triangular Star Pattern\n",
    "#Send Feedback\n",
    "#Print the following pattern for the given N number of rows.\n",
    "#Pattern for N = 4\n",
    "N=int(input()) \n",
    "row=1; \n",
    "while row<=N: \n",
    "    col=1; \n",
    "    while col<=row: \n",
    "        print(\"*\",end=\"\") \n",
    "        col=col+1 \n",
    "    row=row+1 \n",
    "    print()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Code : Triangle Number Pattern\n",
    "Send Feedback\n",
    "Print the following pattern for the given N number of rows.\n",
    "Pattern for N = 4\n",
    "1\n",
    "22\n",
    "333\n",
    "4444"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "1\n",
      "22\n",
      "333\n",
      "4444\n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "i=1\n",
    "while i<=n:\n",
    "    j=1\n",
    "    while j<=i:\n",
    "        print(i, end='')\n",
    "        j=j+1\n",
    "    print()\n",
    "    i=i+1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Code : Reverse Number Pattern\n",
    "Send Feedback\n",
    "Print the following pattern for the given N number of rows.\n",
    "Pattern for N = 4\n",
    "1\n",
    "21\n",
    "321\n",
    "4321"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "1\n",
      "21\n",
      "321\n",
      "4321\n"
     ]
    }
   ],
   "source": [
    "N=int(input()) \n",
    "row=1; \n",
    "while row<=N: \n",
    "    col=1; \n",
    "    while col<=row: \n",
    "        print(row-col+1,end=\"\") \n",
    "        col=col+1 \n",
    "    row=row+1 \n",
    "    print()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Code : Character Pattern\n",
    "Send Feedback\n",
    "Print the following pattern for the given N number of rows.\n",
    "Pattern for N = 4\n",
    "A\n",
    "BC\n",
    "CDE\n",
    "DEFG"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "A\n",
      "BC\n",
      "CDE\n",
      "DEFG\n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "row=1\n",
    "while row<=n:\n",
    "    col=1# Inner loop\n",
    "    ch=65+row-1\n",
    "    while col<=row:\n",
    "        print(chr(ch+col-1),end=\"\")\n",
    "        col+=1\n",
    "    print()\n",
    "    row=row+1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Code : Interesting Alphabets\n",
    "Send Feedback\n",
    "Print the following pattern for the given number of rows.\n",
    "Pattern for N = 5\n",
    "E\n",
    "DE\n",
    "CDE\n",
    "BCDE\n",
    "ABCDE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "E\n",
      "DE\n",
      "CDE\n",
      "BCDE\n",
      "ABCDE\n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "row=1\n",
    "while row<=n:\n",
    "    col=1# Inner loop\n",
    "    ch=65+n-row\n",
    "    while col<=row:\n",
    "        print(chr(ch+col-1),end=\"\")\n",
    "        col+=1\n",
    "    print()\n",
    "    row=row+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
