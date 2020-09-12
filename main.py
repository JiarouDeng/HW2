# Author: Jiarou Deng dpj5243@psu.edu
def getGradePoint(g):
  p=0
  if g == "A":
   p = 4.0
  elif g == "A-":
   p = 3.67
  elif g == "B+":
   p = 3.33
  elif g == "B":
   p = 3.0
  elif g == "B-":
   p = 2.67
  elif g == "C+":
   p = 2.33
  elif g == "C":
   p = 2.0
  elif g == "D":
   p = 1.0
  else:
   p = 0.0
  return p
def run():
 g = input("Enter your course 1 letter grade: ")
 c = float(input("Enter your course 1 credit: "))
 print(f"Grade point for course 1 is: {getGradePoint(g)}")
 GPA= getGradePoint(g)*float(c)
 C= float(c)
 g = input("Enter your course 2 letter grade: ")
 c = float(input("Enter your course 2 credit: "))
 print(f"Grade point for course 2 is: {getGradePoint(g)}")
 GPA= GPA+getGradePoint(g)*float(c)
 C= C+float(c)
 g = input("Enter your course 3 letter grade: ") 
 c = float(input("Enter your course 3 credit: "))
 print(f"Grade point for course 3 is: {getGradePoint(g)}")
 GPA= GPA+getGradePoint(g)*float(c)
 C= C+float(c)
 GPAALL= GPA/C
 print(f"Your GPA is: {GPAALL}")

if __name__ == "__main__":
 run()