def solution(record):
    answer = []
    name = {}
    
    for i in record:
        array = i.split()
        keyword = array[0]
        if keyword == "Enter":
            name[array[1]] = array[2]
        elif keyword == "Change":
            name[array[1]] = array[2]
    for i in record:
        array = i.split()
        keyword = array[0]
        if keyword == "Enter":
            answer.append(name[array[1]]+"님이 들어왔습니다.")
        elif keyword == "Leave":
            answer.append(name[array[1]]+"님이 나갔습니다.")
            
    return answer