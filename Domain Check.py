WebPageA = input("Enter web Name: ").lower()
WebPageB = input("Insert web Name : ").lower()

if WebPageA == WebPageB:
    print("Domains look same")
elif WebPageA in WebPageB or WebPageB in WebPageA:
    print("Suspicious Web Page")
else:
    print("Web Page look different")
