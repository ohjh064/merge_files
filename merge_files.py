#파일 리스트
filenames  = ['C:\\Users\\ohjh0\\OneDrive\\바탕 화면\\수능 문장모음\\2019-11-수능-문장-영어.txt', 
                'C:\\Users\\ohjh0\\OneDrive\\바탕 화면\\수능 문장모음\\2020-11-수능-문장-영어.txt',
                'C:\\Users\\ohjh0\\OneDrive\\바탕 화면\\수능 문장모음\\2021-11-수능-문장-영어.txt']

with open('C:\\Users\\ohjh0\\OneDrive\\바탕 화면\\19-21_수능_문장_영어.txt', 'w') as outfile:
    for filename in filenames:
        with open(filename) as file:
            for line in file:
                outfile.write(line)