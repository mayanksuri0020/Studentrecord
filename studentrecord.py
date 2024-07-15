record1=['stdid','stdname','10th','age','hindi','maths','english','science','computer','total']
record2=['std101','ashish','10th','15','67','87','89','89','90','422']
record3=['st102','abhishek','10th','14','85','48','45','90','45','313']
record4=['st103','aman','10th','15','23','78','56','78','67','302']
record5=['st104','rahul','10th','14','45','45','67','45','56','258']
record6=['st105','ruby','10th','13','69','89','67','90','65','403']
record7=['st106','suman','10th','13','90','67','46','67','67','337']
record8=['st107','saurabh','10th','15','45','34','23','45','34','181']
record9=['st108','sumit','10th','14','23','67','45','78','90','303']
record10=['st109','kamlesh','10th','15','45','78','56','99','67','345']
record11=['st110','rohan','10th','15','34','24','12','45','56','171']
studentrecord =[record2,record3,record4,record5,record6,record7,record8,record9,record10,record11]
for row in studentrecord:
    print(row)
    
print("-------------------------------------------------------------------")

# display name of students whose marks in english is greater than 50

for rowindex in range(1,len(studentrecord)):
    if(studentrecord[rowindex][6]>"50"):
       print(studentrecord[rowindex][1])
print("-------------------------------------------------------------------")

# display student name and age of top 4 scorer of maths
top_scorer_count= 0
for student in studentrecord:
    if student[5]>"75":
         print(f"Name: {student[1]}")
         print(f"Age: {student[3]}")

         top_scorer_count +=1
         if top_scorer_count ==4:
             break

print("-------------------------------------------------------------------")

# display name,id,age who are bottom 3 scorer in computer

print("Bottom 3 Scorers in Computer:")

for i in range(min(3, len(studentrecord))): 
    name = studentrecord[1]
    id = studentrecord[0]
    age =studentrecord[3]
    computer_score = studentrecord[8]
    print(f"{i+1}. Name: {name}, ID: {id}, Age: {age}, Computer Score: {computer_score}")
