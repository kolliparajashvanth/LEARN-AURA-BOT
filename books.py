def get_textbook_links(class_num):
    base = f"https://ncert.nic.in/textbook/pdf"
    subjects = {
        6: ["Math", "Science", "English", "Hindi", "Sanskrit", "SocialScience"],
        7: ["Math", "Science", "English", "Hindi", "Sanskrit", "SocialScience"],
        8: ["Math", "Science", "English", "Hindi", "Sanskrit", "SocialScience"],
        9: ["Math", "Science", "English", "Hindi", "Sanskrit", "SocialScience"],
        10: ["Math", "Science", "English", "Hindi", "Sanskrit", "SocialScience"],
        11: ["Math", "Physics", "Chemistry", "Biology", "English", "Economics"],
        12: ["Math", "Physics", "Chemistry", "Biology", "English", "Economics"],
    }


    books = []
    for sub in subjects.get(class_num, []):
        code = sub[:3].lower()
        download = f"{base}/{code}{class_num}cc.zip"
        online = f"https://ncert.nic.in/textbook.php?{code}{class_num}"
        books.append({"subject": sub, "download": download, "online": online})
    return books


