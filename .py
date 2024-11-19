from InquirerPy import inquirer

nome = inquirer.text('qual é o seu nome?').execute()
cor = inquirer.select("qual é sua cor favorita?", choices = ["Azul","Verde","vermelho"]).execute()