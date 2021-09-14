##
import re
import csv
with open('sample.jeff.bezos - sample.jeff.bezos.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        x = str(row)
        first_name = "jeff"
        last_name = "bezos"
        match = re.search("^.*(" + first_name + ".?;? |" + last_name + ".?;? ).*$",x, re.IGNORECASE)
        match2 = re.search("^.*(thank.?;? |having me.?;? |being here.?;? |joining us.?;? |joins us.?;? |for coming.?;? |sitting down with.?;? |talking with us.?;? |joining with us.?;? |speaking with us.?;? |joins with us.?;? |speaks with us.?;? |" + first_name + " " + last_name + "'s here.?;? |" + first_name + " " + last_name + " with us.?;? |" + first_name + " " + last_name + " is here.?;? |that's " + first_name + " " + last_name + ".?;? |" + first_name + ";? you|mr. " + first_name + ".?;? |" + last_name + ";? you|mr. " + last_name + ".?;? |check in with.?;? |have you on.?;? |have you here.?;? |you're welcome.?;? |good to see you.?;? |our guest host today.?;? |special guest.?;? |good to have you.?;? ).*$",x, re.IGNORECASE)
        match3 = re.search("\'1\'",x)
        if match and match2 and match3:
            with open("new_file.csv", "a") as a_file:
                a_file.write("\n")
                a_file.write(x)