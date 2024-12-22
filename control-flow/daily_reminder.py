task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()


match priority: 
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' ia a low priority task"
    case _:
        message = f"'{task}' has unspecified priority, choose among high, medium or low"
        print(message)
        exit()

if time_bound == "yes":
     message += " that requires immediate attention today!"
     print("Reminder: ", message)
elif time_bound == "no":
    message += ". Consider completing it when you have free time."
    print("Note: ", message)
else:
     message = "Invalid Input for time bound choose yes or no"
     print(message)
     exit()
     



