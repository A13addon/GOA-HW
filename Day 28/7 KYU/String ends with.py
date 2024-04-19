text = ('abc')
ending = ('bc')


def solution(text, ending):
    for char in ending:
        if text[-len(ending):] == ending:
            return True
        
        else:
            return False
        
print(solution(text, ending))
        