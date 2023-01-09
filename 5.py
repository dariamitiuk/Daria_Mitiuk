def friends_list(s):
    s, arr, result = s.split(';'), [], "" #розділяємо на "пари", прибравши роздільник ";"
    for elem in s:
        arr.append(elem.split(':')) #створюємо списки з цих "пар" всередині одного списку
    for x in range(len(arr)):
        arr[x][0], arr[x][1] = arr[x][1], arr[x][0]  #міняєм кожну "пару" місцями 
    new_arr = sorted(arr, key=lambda point: (point[0], point[1])) #сортуємо
    for x in range(len(new_arr)):
        result = result + '(' + str(new_arr[x][0]).upper() + ', ' + str(new_arr[x][1]).upper() + ')'
    return result

if __name__ == '__main__':
    print('friends_list("Fred:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill") -> \n', friends_list("Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"))