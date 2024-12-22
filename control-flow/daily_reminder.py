task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()


match priority: 
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task} ia a low priority task'"
    case _:
        message = f"'{task} has unspecified priority, choose among high, medium or low'"

if time_bound == "yes":
    message += " that requires immediate attention today!"
    print("\n Reminder: ", message)
else:
     message += ". Consider completing it when you have free time."
     print("\n Note:", message)


