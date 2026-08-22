def quiz():
    questions = [
       { "question":"Q1 shape of the earth",
         "options":["  A=round","  B=triangular","  C=square"],
         "answer":"A"
       },
       { "question":"Q2 color of the sky",
         "options":["  A=yellow","  B=red","  C=blue"],
         "answer":"C"
       }
     ]
    for a in questions:
     print(a["question"])
     for option in a["options"]:
        print(option)

     choice=input("Answer:")
     if choice==a["answer"]:
      print("correct")
     else:
      print("incorrect",a["answer"])
quiz()