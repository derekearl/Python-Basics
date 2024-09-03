# Open other file in the lesson 11 folder
with open ('lesson11/hr_system.txt') as pay_info:

    # loop to dispaly all of the data
    for i in pay_info:

        # Clean up white space
        line = i.strip()
        # Split the line with " " as the seprerator
        label = line.split(" ")
        
        # Save the data into specific variables
        name = label[0]
        id_number = label[1]
        title = label[2]
        salary = float(label[3])

        # Determines paycheck amount
        pay_amount = salary / 24

        # Adds the engineering bonus
        if title.lower() == "engineer":
            pay_amount += 1000

        print(f"{name} (ID: {id_number}), {title} - ${pay_amount:.2f}")