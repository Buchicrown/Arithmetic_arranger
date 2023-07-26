def arithmetic_arranger(problems, show_solutions=False):
    
    arranged_problems = ""
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""

    if len(problems) > 5:
        return "Error: Too many problems."
    
    for problem in problems:
        segment = problem.split()

        if segment[1]  not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        
        if not segment[0].isdigit() or not segment[2].isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(segment[0]) > 4 or len(segment[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        #print(segment)   
        
        gap = max(len(segment[0]), len(segment[2])) + 2
        first_line += segment[0].rjust(gap) + "    "
        second_line += segment[1]  + " " + segment[2].rjust(gap-2) + "    "
        third_line += '-' * gap + "    "

    #if show_solutions:
            
        if segment[1] == "+":
                solution = str(int(segment[0]) + int(segment[2]))
        else:
                solution = str(int(segment[0]) - int(segment[2]))
            
        fourth_line += solution.rjust(gap) + "    "

    arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + third_line.rstrip()
         
    
    """arranged_problems += first_line + "\n"
    arranged_problems += second_line.rstrip() + "\n"
    arranged_problems += third_line.rstrip()"""


    if show_solutions:
        arranged_problems += "\n" + fourth_line.rstrip()
          


    return arranged_problems


print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))


