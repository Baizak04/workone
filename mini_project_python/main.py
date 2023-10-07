from utils import get_random_word_from_file, shuffle_word, save_player_score, get_statistics_from_file


def main():
    
    user_score = 0
    
    print("Введите ваше имя ")
    user_name = input()
    
    words = get_random_word_from_file()
    
    for word in words:
        
        word_shuffled = shuffle_word(word)
        print(f"Угадайте слово {word_shuffled}")
        
        user_input = input()
        
        if user_input == word:
            user_score += 10
            print("Верно! Вы получаете 10очков")
        else:
            print(f"Неверно! Верный ответ {word}.")
        
        save_player_score(user_name, user_score)
        
        stats = get_statistics_from_file()
        
        print(f"Всего игр сыграно: {stats.get('len')}")
        print(f"Максимальный рекорд: {stats.get('max')}")
       
    
main()