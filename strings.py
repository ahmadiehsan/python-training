student = 'ehsan'
score = 3 * 18

print('results of ' + student + ' in his last exam: ' + str(score) + ' point')  # very old
print('results of {} in his last exam: {} point'.format(student, score))  # old
print(f'results of {student} in his last exam: {score} point')  # new one
