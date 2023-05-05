import subprocess

def cleanOrgName(orgName):
    for char in orgName:
        if char == " ":
            orgName = orgName.replace(' ', '%20')
        elif char == "!":
            orgName = orgName.replace('!', '%21')
        elif char == "#":
            orgName = orgName.replace('#', '%23')
        elif char == "$":
            orgName = orgName.relpace('$', '%24')
        elif char == "%":
            orgName = orgName.replace('%', '%25')
        elif char == "&":
            orgName = orgName.replace('&', '%26')
        elif char == "(":
            orgName = orgName.replace('(', '%28')
        elif char == ")":
            orgName = orgName.replace(')', '%29')
        elif char == "*":
            orgName = orgName.replace('*', '%2A')
        elif char == "+":
            orgName = orgName.replace('+', '%2B')
        elif char == ",":
            orgName = orgName.replace(',', '%2C')
        elif char == "-":
            orgName = orgName.replace('-', '%2D')
        elif char == ".":
            orgName = orgName.replace('.', '%2E')
        elif char == "/":
            orgName = orgName.replace('/', '%2F')

    # end for loop

    return orgName
# end def cleanOrgName()

done = False

while (not done):
    print("Input SV ID: ", end='')
    svID = input()

    while svID == "":
        print("Cannot be blank. Try again.")
        print("Input SV ID: ", end='')
        svID = input()

    print("Input Org ID: ", end='')
    orgID = input()

    while orgID == "":
        print("Cannot be blank. Try again.")
        print("Input Org ID: ", end='')
        orgID = input()

    print("Input Org Name: ", end='')
    orgName = input()

    while orgName == "":
        print("Cannot be blank. Try again.")
        print("Input Org Name: ", end='')
        orgName = input()
    

    cleanedOrgName = cleanOrgName(orgName)

    url = f"https://usu.co1.qualtrics.com/SE/?SID={svID}&OrgID={orgID}&OrgName={cleanedOrgName}"

    print("\n\n" + url)
    
    print("\n\nWould you like to copy to clipboard?: (y/n) ", end='')
    copy = input()
    
    positive = False
    while not positive:

        if copy.lower() == "y" or copy.lower() == "yes":
            subprocess.run("pbcopy", text=True, input=url)
            print("Copied to clipboard!")
            positive = True
        else:
            print("Please confirm previous response: (y/n) ", end='')
            copy = input()
            if copy.lower() != "y" or copy.lower() != "yes":
                print("Alrighty! You did not copy the link :'(")
                positive = True


    print("\nWould you like to generate another link? (y/n) ", end='')
    repeatProcess = input()

    if repeatProcess.lower() == "y" or repeatProcess.lower() == "yes":
        print("\nBegin Again!")
    else:
        print("\nAll Done!")
        done = True

