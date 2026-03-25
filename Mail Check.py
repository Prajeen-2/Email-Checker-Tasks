mail_check = input("Share the email :")
risky_words = ["Urgent", "Verify","Password","Bank","Click","Need","Help"]
if any(word in mail_check for word in risky_words):
       print("This Email May Me Risky!! Alert!!! ")
else:
    print("This Email Looks Safe")
    
