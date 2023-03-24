def isDiv3(n):
    # getting the int number
    s =str(n)
    # converting number int string

    sum =0
    for x in s:
        sum =sum+int(x)
# looping through the string
    if sum>9:
        return isDiv3(sum);
    elif sum==3 or sum==6 or sum==9:
        return True;
# checking the sum is > 9 then repeat the loop untill for getting single digit
     #return sum%3 == 0
if __name__ == "__main__":
    number = 771
    print(f"{number} is {'' if isDiv3(number) else 'not'} divisble by three")