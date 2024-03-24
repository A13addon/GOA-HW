# Remove String Spaces


input = ("8 j 8   mBliB8g  imjB8B8  jl  B")

def no_space (input):
    final = ""
    for num in input:
        if num != " ":
            final += num
    return final

print(no_space(input))
        