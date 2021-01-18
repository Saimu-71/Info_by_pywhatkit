import pywhatkit as saimu

print("Showing some wiki summary")

topics1="Python"
topics2="Java"

saimu.info(topics1,lines=4)

print()
saimu.info(topics2,lines=4)