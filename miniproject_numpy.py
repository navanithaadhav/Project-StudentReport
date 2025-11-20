import numpy as np

# #Student mark analysis
# 1.Average marks of each student and subject
# 2.highest and lowest marks in each subject
# 3.Number of students passed and failed in each subject
# 4.overall class topper and subject topper
# 5.which subject is most difficult based on average marks
# 6.stusend ranking based on total marks

np.random.seed(40)  # For reproducibility
marks= np.random.randint(20,101,size=(20,5))


# 1.Average marks of each student and subject
student_avg=np.mean(marks,axis=1)
subject_avg=np.mean(marks,axis=0)

#2.highest and lowest marks in each subject
tamil,english,maths,science,social=np.max(marks,axis=0)
tamil_low,english_low,maths_low,science_low,social_low=np.min(marks,axis=0)

# 3.Number of students passed and failed in each subject
pass_mark=marks>=35
tamil_pass=np.sum(pass_mark[:,0])
english_pass=np.sum(pass_mark[:,1])
maths_pass=np.sum(pass_mark[:,2])
science_pass=np.sum(pass_mark[:,3]) 
social_pass=np.sum(pass_mark[:,4])

#4.overall class topper and subject topper
overall_topper_index=np.argmax(np.sum(marks,axis=1))

# 5.which subject is most difficult based on average marks
most_difficult_subject_index=np.argmin(subject_avg)

#6.stusend ranking based on total marks
total_marks=np.sum(marks,axis=1)
ranking_indices=np.argsort(-total_marks)
ranks=total_marks[ranking_indices]


print ("Marks of 20 students in 5 subjects:\n",marks)
print("\nAverage marks of each student:\n",student_avg)
print("\nAverage marks of each subject:\n",subject_avg)
print("\nHighest marks in each subject:\n Tamil:",tamil," English:",english," Maths:",maths," Science:",science," Social:",social)
print("\nLowest marks in each subject:\n Tamil:",tamil_low," English:",english_low," Maths:",maths_low," Science:",science_low," Social:",social_low)
print("\nNumber of students passed in Tamil:",tamil_pass)
print("Number of students passed in English:",english_pass)
print("Number of students passed in Maths:",maths_pass)
print("Number of students passed in Science:",science_pass)
print("Number of students passed in Social:",social_pass)
print("\nOverall class topper is student number:",overall_topper_index+1,"with total marks:",np.sum(marks[overall_topper_index]))
print("Most difficult subject is subject number:",most_difficult_subject_index+1,"with average marks:",subject_avg[most_difficult_subject_index])
print("\nStudent rankings based on total marks:",ranks)

for rank, index in enumerate(ranking_indices, start=1):
    print(f"Rank {rank}: Student {index+1} with total marks {total_marks[index]}")
