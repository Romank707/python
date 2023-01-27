def personal_data(*, firstname, lastname, birth_year, city, email, phone_number):
    return print(f"Имя: {firstname} Фамилия: {lastname} Год рождения: {birth_year} "
                 f"Город проживания: {city} Email: {email} Телефон: {phone_number}")


personal_data(firstname=input('Имя: '), lastname=input('Фамилия: '), birth_year=input('Год Рождения: '),
    city=input('Город проживания: '), email=input('email: '), phone_number=input('phone: '))








































