task= input("Enter your task:")
priority=input("Priority (high/medium/low):")
time_bound=input("Is it time-bound? (yes/no):").lower()
reminder =task
match priority:
    case 'high':
        reminder += " is a high priority task."
    case 'medium':
        reminder += " is a medium priority task."
    case 'low':
            reminder += " is a low priority task."
    case _:
        reminder += " has a not recognized Priority level."

if time_bound == 'yes':
    reminder="Reminder: "+reminder
    reminder=reminder[0,len(reminder-1)]
    reminder += " That requires immediate attention today!"
elif time_bound == 'no':
    reminder="Note: "+reminder
    reminder += " Consider completing it when you have free time."
print(reminder)
