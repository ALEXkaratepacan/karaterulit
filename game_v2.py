""""Игра угадай число.Компьютер сам загадывает и угадывает число"""
import numpy as np
def random_predict(number:int=1) -> int:
    """Рандомно угадываем число
    Args:
        number(int,optional):Загаданное число. Defaults to 1.
    Returns:
      int:Число попыток
      """
    count=0
    while True:
        count+=1
        predict_number=np.random.randint(1,101)# предпалогаемое число
        if number==predict_number:
            break#выход из цикла
    return(count)

def score_game(random_predict)-> int:
    """За какое количестов попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    
    Returns:
      int:среднее количетсо попыток
    """
    count_ls=[]
    np.random.seed(1)
    random_array=np.random.randint(1, 101, size=(1000))#загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    score=int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


score_game(random_predict)
    
    
      
    

#print(f'Количество попыток{random_predict(10)}')
    

        