with open('Text_5_02.txt') as file:
    line_st = file.readlines()
    for i, st in enumerate(line_st):
        count_st = len(st.split())
        print(f'*{i+1} - {count_st} words')
