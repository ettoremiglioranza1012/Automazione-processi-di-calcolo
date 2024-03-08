def ins_mark():

    print("How many exam/exams do you have attended until now?")
    num_exam = int(input())

    return num_exam

def ins_marks(num_exam):
    
    marks_grade = []
    marks_weight = []
    marks_and_weights = []
    credits = [3,6,8,12]
    
    for i in range(num_exam):
        print('How much did you take?')
        mark_grade = int(input())
        
        if mark_grade < 18 or mark_grade > 31:
            raise ValueError('OPS, It seems your mark is not an existing value')
        
        marks_grade.append(mark_grade)
        print('How many credits did it weight?')
        mark_weight = int(input())
        
        if mark_weight not in credits:
            raise ValueError('OPS, it seems your credit value is\'t an existing value')
        
        marks_weight.append(mark_weight)
        marks_and_weights += [[mark_grade,mark_weight]]

    return marks_grade, marks_weight, marks_and_weights

def marks_analysis(marks_grade, marks_weight):
    
    sum_mark_pond = 0
    sum_mark = 0
    sum_cred = 0
    
    for i in range(len(marks_grade)): # or marks_weight
        sum_mark_pond += marks_grade[i]*marks_weight[i]
        sum_mark += marks_grade[i]
        sum_cred += marks_weight[i]
    pond_mean = sum_mark_pond/sum_cred
    arit_mean = sum_mark/len(marks_grade)
    
    return pond_mean, arit_mean, sum_mark_pond, sum_cred

def more_analysis(credits, sum_mark_pond, sum_cred):
    
    print('How many credits will your next exame weight?')
    credit = int(input())
    
    if credit not in credits:
        raise ValueError('Ops, seems like your digit was wrong!')
    lista_new_mean_pond = []
    i = 0
    
    while i < 13:
        lista_new_mean_pond.append((sum_mark_pond + (18 + i)*credit)/ (sum_cred + credit))
        i += 1
    print(f'After the next exames you have 14 possibilities of means outcomes: {[round(x,2) for x in lista_new_mean_pond]}')
        
            
def main():    

    credits = [3,6,8,12]
    num_exam = ins_mark()
    marks_grade, marks_weight, marks_and_weights = ins_marks(num_exam)
    
    print(f'Your exams until now got the next marks:{marks_grade}')
    print(f'And the following weights: {marks_weight}')
    print(f'Shortly, that\'s your CURRICOLA, until now: {marks_and_weights}')
    print('Let\'s procede to calculate some data!')
    
    pond_mean, arit_mean, sum_mark_pond, sum_cred = marks_analysis(marks_grade, marks_weight)
    
    print(f'Your mean (ponderata) is: {round(pond_mean,2)}.\nMeanwhile, your aritemic mean is: {round(arit_mean,2)}')
    print('Do you want to know how your statistics would change with other votes?')
    
    response = str(input()).lower()
    
    if response == 'yes':
        more_analysis(credits, sum_mark_pond, sum_cred)
    
    elif response == 'no':
        print('All right! See you later...')
    
    else:
        raise ValueError('Ops, I can\'t response to that.')


if __name__ == "__main__":
    main()








