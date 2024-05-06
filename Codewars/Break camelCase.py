def solution(s):
    final_output = ""
    for char in s:
        if char.isupper():
            final_output += " " + char
        else:
            final_output += char
    return final_output.strip()