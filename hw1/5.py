List1 = ['morning', 'afternoon', 'night']
List2 = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

result = []
for days in List2:
    for times in List1:
        result.extend([days + '-' + times])

print(result)

