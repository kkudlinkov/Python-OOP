import pickle
with open("lop.pickle", "rb") as f2:
    student1 = pickle.load(f2)
    student2 = pickle.load(f2)
    student3 = pickle.load(f2)
    student4 = pickle.load(f2)
    student5 = pickle.load(f2)
    teacher1 = pickle.load(f2)
    teacher2 = pickle.load(f2)
    teacher3 = pickle.load(f2)
    group1 = pickle.load(f2)
    teacher1.change("Мастер финансовых наук")
    print(teacher1)

