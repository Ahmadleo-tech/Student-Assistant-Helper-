import webbrowser
import pyttsx3

engine = pyttsx3.init()

# Semester 1 =============================================================
def sem1(degree, subject):
    degree = degree.lower()
    subject = subject.lower()

    if degree == "cs":
        if subject == "pf":
            webbrowser.open("https://drive.google.com/drive/folders/1WFbB33MDYV9ooz92zr1_bffhEb8Pye1_")
        elif subject == "ict":
            webbrowser.open("https://drive.google.com/drive/folders/1yPk8VZbbB731S27JjBArGthtsJ89CiRS")
        else:
            print(f"{subject} is not a computing subject of 1st Semester of BSCS!")
    
    elif degree == "se":
        if subject == "pf":
            webbrowser.open("https://drive.google.com/drive/folders/1WFbB33MDYV9ooz92zr1_bffhEb8Pye1_")
        elif subject == "ict":
            webbrowser.open("https://drive.google.com/drive/folders/1yPk8VZbbB731S27JjBArGthtsJ89CiRS")
        else:
            print(f"{subject} is not a computing subject of 1st Semester of BSSE!")
    
    elif degree == "ai":
        if subject == "pf":
            webbrowser.open("https://drive.google.com/drive/folders/1WFbB33MDYV9ooz92zr1_bffhEb8Pye1_")
        elif subject == "ict":
            webbrowser.open("https://drive.google.com/drive/folders/1yPk8VZbbB731S27JjBArGthtsJ89CiRS")
        else:
            print(f"{subject} is not a computing subject of 1st Semester of BSAI!")
    
    elif degree == "ee":
        if subject == "pf":
            webbrowser.open("https://drive.google.com/drive/folders/1WFbB33MDYV9ooz92zr1_bffhEb8Pye1_")
        else:
            print(f"{subject} is not a computing subject of 1st Semester of BSEE!")
    
    else:
        print(f"{degree} not present!")

# Semester 2 =============================================================
def sem2(degree, subject):
    degree = degree.lower()
    subject = subject.lower()

    if degree == "cs":
        if subject == "oop":
            webbrowser.open("https://drive.google.com/drive/folders/1hgH7wC7H6if9s-95wpKbHiTfVpWOfdBw")
        else:
            print(f"{subject} is not a computing subject of 2nd Semester of BSCS!")
    
    elif degree == "se":
        if subject == "oop":
            webbrowser.open("https://drive.google.com/drive/folders/1hgH7wC7H6if9s-95wpKbHiTfVpWOfdBw")
        else:
            print(f"{subject} is not a computing subject of 2nd Semester of BSSE!")
    
    elif degree == "ai":
        if subject == "oop":
            webbrowser.open("https://drive.google.com/drive/folders/1hgH7wC7H6if9s-95wpKbHiTfVpWOfdBw")
        else:
            print(f"{subject} is not a computing subject of 2nd Semester of BSAI!")
    
    elif degree == "ee":
        if subject == "oop":
            webbrowser.open("OOP LINK")
        else:
            print(f"{subject} is not a computing subject of 2nd Semester of BSEE!")
    
    else:
        print(f"{degree} not present!")

# Semester 3 =============================================================
def sem3(degree, subject):
    degree = degree.lower()
    subject = subject.lower()

    if degree == "cs":
        if subject == "dsa":
            webbrowser.open("https://drive.google.com/drive/folders/1deuPO-sxgbUugS4eAxzm3JTabK_95Qzj")
        elif subject == "coal":
            webbrowser.open("https://drive.google.com/drive/folders/1ctNd4IFdayaaM1yQgV90z9lqgAJKjr3s")
        elif subject == "ds":
            webbrowser.open("https://drive.google.com/drive/folders/1XPMNyqYL6QFVDlDgTiepx9HkiqcNtTRx")
        else:
            print(f"{subject} is not a computing subject of 3rd Semester of BSCS!")
    
    elif degree == "se":
        if subject == "dsa":
            webbrowser.open("https://drive.google.com/drive/folders/1deuPO-sxgbUugS4eAxzm3JTabK_95Qzj")
        elif subject == "coal":
            webbrowser.open("https://drive.google.com/drive/folders/1ctNd4IFdayaaM1yQgV90z9lqgAJKjr3s")
        elif subject == "ds":
            webbrowser.open("https://drive.google.com/drive/folders/1XPMNyqYL6QFVDlDgTiepx9HkiqcNtTRx")
        else:
            print(f"{subject} is not a computing subject of 3rd Semester of BSSE!")
    
    elif degree == "ai":
        if subject == "dsa":
            webbrowser.open("https://drive.google.com/drive/folders/1deuPO-sxgbUugS4eAxzm3JTabK_95Qzj")
        elif subject == "coal":
            webbrowser.open("https://drive.google.com/drive/folders/1ctNd4IFdayaaM1yQgV90z9lqgAJKjr3s")
        elif subject == "ds":
            webbrowser.open("https://drive.google.com/drive/folders/1XPMNyqYL6QFVDlDgTiepx9HkiqcNtTRx")
        else:
            print(f"{subject} is not a computing subject of 3rd Semester of BSAI!")
    
    elif degree == "ee":
        if subject == "dsa":
            webbrowser.open("https://drive.google.com/drive/folders/1deuPO-sxgbUugS4eAxzm3JTabK_95Qzj")
        else:
            print(f"{subject} is not a computing subject of 3rd Semester of BSEE!")
    
    else:
        print(f"{degree} not present!")

# Semester 4 =============================================================
def sem4(degree, subject):
    degree = degree.lower()
    subject = subject.lower()

    if degree == "cs":
        if subject == "db":
            webbrowser.open("https://drive.google.com/drive/folders/13zs9uv5t0L33gaxPRPEx4aDqhJpkWPFn")
        elif subject == "os":
            webbrowser.open("https://drive.google.com/drive/folders/1XU_aEyVGhvWx5VFB8erMym_BICPbiy31")
        else:
            print(f"{subject} is not a computing subject of 4th Semester of BSCS!")
    
    elif degree == "se":
        if subject == "db":
            webbrowser.open("https://drive.google.com/drive/folders/13zs9uv5t0L33gaxPRPEx4aDqhJpkWPFn")
        elif subject == "os":
            webbrowser.open("https://drive.google.com/drive/folders/1XU_aEyVGhvWx5VFB8erMym_BICPbiy31")
        else:
            print(f"{subject} is not a computing subject of 4th Semester of BSSE!")
    
    elif degree == "ai":
        if subject == "db":
            webbrowser.open("https://drive.google.com/drive/folders/13zs9uv5t0L33gaxPRPEx4aDqhJpkWPFn")
        elif subject == "os":
            webbrowser.open("https://drive.google.com/drive/folders/1XU_aEyVGhvWx5VFB8erMym_BICPbiy31")
        else:
            print(f"{subject} is not a computing subject of 4th Semester of BSAI!")
    
    elif degree == "ee":
        if subject == "db":
            webbrowser.open("https://drive.google.com/drive/folders/13zs9uv5t0L33gaxPRPEx4aDqhJpkWPFn")
        elif subject == "os":
            webbrowser.open("https://drive.google.com/drive/folders/1XU_aEyVGhvWx5VFB8erMym_BICPbiy31")
        else:
            print(f"{subject} is not a computing subject of 4th Semester of BSEE!")
    
    else:
        print(f"{degree} not present!")

# Semester 5 =============================================================
def sem5(degree, subject):
    degree = degree.lower()
    subject = subject.lower()

    if degree == "cs":
        if subject == "sw":
            webbrowser.open("SW LINK")
        elif subject == "wd":
            webbrowser.open("WD LINK")
        else:
            print(f"{subject} is not a computing subject of 5th Semester of BSCS!")
    
    elif degree == "se":
        if subject == "sw":
            webbrowser.open("SW LINK")
        elif subject == "wd":
            webbrowser.open("WD LINK")
        else:
            print(f"{subject} is not a computing subject of 5th Semester of BSSE!")
    
    elif degree == "ai":
        if subject == "sw":
            webbrowser.open("SW LINK")
        elif subject == "wd":
            webbrowser.open("WD LINK")
        else:
            print(f"{subject} is not a computing subject of 5th Semester of BSAI!")
    
    else:
        print(f"{degree} not present!")

# Semester 6 =============================================================
def sem6(degree, subject):
    degree = degree.lower()
    subject = subject.lower()

    if degree == "cs":
        if subject == "cn":
            webbrowser.open("CN LINK")
        elif subject == "mad":
            webbrowser.open("MAD LINK")
        else:
            print(f"{subject} is not a computing subject of 6th Semester of BSCS!")
    
    elif degree == "se":
        if subject == "cn":
            webbrowser.open("CN LINK")
        elif subject == "mad":
            webbrowser.open("MAD LINK")
        else:
            print(f"{subject} is not a computing subject of 6th Semester of BSSE!")
    
    elif degree == "ai":
        if subject == "cn":
            webbrowser.open("CN LINK")
        elif subject == "mad":
            webbrowser.open("MAD LINK")
        else:
            print(f"{subject} is not a computing subject of 6th Semester of BSAI!")
    
    else:
        print(f"{degree} not present!")

# Semester 7 =============================================================
def sem7(degree, subject):
    degree = degree.lower()
    subject = subject.lower()

    if degree == "cs":
        if subject == "st":
            webbrowser.open("ST LINK")
        elif subject == "ai":
            webbrowser.open("AI LINK")
        else:
            print(f"{subject} is not a computing subject of 7th Semester of BSCS!")
    
    elif degree == "se":
        if subject == "st":
            webbrowser.open("ST LINK")
        elif subject == "ai":
            webbrowser.open("AI LINK")
        else:
            print(f"{subject} is not a computing subject of 7th Semester of BSSE!")
    
    elif degree == "ai":
        if subject == "st":
            webbrowser.open("ST LINK")
        elif subject == "ai":
            webbrowser.open("AI LINK")
        else:
            print(f"{subject} is not a computing subject of 7th Semester of BSAI!")
    
    else:
        print(f"{degree} not present!")

# Semester 8 =============================================================
def sem8(degree, subject):
    degree = degree.lower()
    subject = subject.lower()

    if degree == "cs":
        if subject == "cp":
            webbrowser.open("CP LINK")
        elif subject == "ec":
            webbrowser.open("EC LINK")
        else:
            print(f"{subject} is not a computing subject of 8th Semester of BSCS!")
    
    elif degree == "se":
        if subject == "cp":
            webbrowser.open("CP LINK")
        elif subject == "ec":
            webbrowser.open("EC LINK")
        else:
            print(f"{subject} is not a computing subject of 8th Semester of BSSE!")
    
    elif degree == "ai":
        if subject == "cp":
            webbrowser.open("CP LINK")
        elif subject == "ec":
            webbrowser.open("EC LINK")
        else:
            print(f"{subject} is not a computing subject of 8th Semester of BSAI!")
    
    else:
        print(f"{degree} not present!")


def main1():
    engine.say("Enter Semester Number (1 - 8): ")
    engine.runAndWait() 
    semester = int(input("Enter Semester Number (1 - 8): "))

    match semester:
        case 1:
            degree = str(input("Enter Degree Name (CS, SE, AI, EE): "))
            subject = str(input("Enter Subject Name (PF , ICT) : "))
            engine.say(f"Successfully input in BS{degree.upper()} and {subject.upper()} for Semester {semester}")
            engine.runAndWait()
            sem1(degree, subject)

        case 2:
            degree = str(input("Enter Degree Name (CS, SE, AI, EE): "))
            subject = str(input("Enter Subject Name (OOP) : "))
            engine.say(f"Successfully input in BS{degree.upper()} and {subject.upper()} for Semester {semester}")
            engine.runAndWait()
            sem2(degree, subject)

        case 3:
            degree = str(input("Enter Degree Name (CS, SE, AI, EE): "))
            subject = str(input("Enter Subject Name (COAL , DS , DSA) : "))
            engine.say(f"Successfully input in BS{degree.upper()} and {subject.upper()} for Semester {semester}")
            engine.runAndWait()
            sem3(degree, subject)

        case 4:
            degree = str(input("Enter Degree Name (CS, SE, AI, EE): "))
            subject = str(input("Enter Subject Name  (DB , OS) : "))
            engine.say(f"Successfully input in BS{degree.upper()} and {subject.upper()} for Semester {semester}")
            engine.runAndWait()
            sem4(degree, subject)

        case 5:
            degree = str(input("Enter Degree Name (CS, SE, AI): "))
            subject = str(input("Enter Subject Name  (SW , WD) : "))
            engine.say(f"Successfully input in BS{degree.upper()} and {subject.upper()} for Semester {semester}")
            engine.runAndWait()
            sem5(degree, subject)

        case 6:
            degree = str(input("Enter Degree Name (CS, SE, AI): "))
            subject = str(input("Enter Subject Name  (CN , MAD) : "))
            engine.say(f"Successfully input in BS{degree.upper()} and {subject.upper()} for Semester {semester}")
            engine.runAndWait()
            sem6(degree, subject)

        case 7:
            degree = str(input("Enter Degree Name (CS, SE, AI): "))
            subject = str(input("Enter Subject Name (AI , ST) : "))
            engine.say(f"Successfully input in BS{degree.upper()} and {subject.upper()} for Semester {semester}")
            engine.runAndWait()
            sem7(degree, subject)

        case 8:
            degree = str(input("Enter Degree Name (CS, SE, AI): "))
            subject = str(input("Enter Subject Name (CE , CP) : "))
            engine.say(f"Successfully input in BS{degree.upper()} and {subject.upper()} for Semester {semester}")
            engine.runAndWait()
            sem8(degree, subject)

        case _:
            engine.say("Error: Invalid Input!")
            engine.runAndWait()


if __name__ == "__main__":
    main1