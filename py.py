def main():
    '''Main Function'''
    input1 = input()
    input2 = input()
    output = (str(input1) + str(input2)) + " + " + (str(input2) + str(input1)) + " = " + str(int(str(input1 + input2)) + int(str(input2 + input1)))
    print(output)

main()