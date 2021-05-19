from urllib.request import urlopen
from bs4 import BeautifulSoup
import telebot

URL = 'https://www.singaporepools.com.sg/DataFileArchive/Lottery/Output/toto_result_top_draws_en.html?v' \
      '=2021y5m19d12h45m '
DATE = 'Thu, 20 May 2021'  # set your preferred date here
TICKETS = [[4, 8, 11, 27, 30, 35], [2, 4, 12, 16, 26, 34], [2, 16, 20, 36, 39, 49], [9, 15, 19, 33, 37, 44],
           [1, 11, 14, 27, 30, 48]
    , [2, 8, 25, 28, 31, 41], [9, 10, 14, 17, 19, 33], [4, 24, 30, 31, 36, 45], [11, 22, 33, 37, 46, 48]
    , [17, 28, 32, 38, 42, 44], [14, 15, 25, 28, 32, 35], [1, 23, 27, 38, 39, 46], [3, 14, 22, 27, 29, 37]
    , [8, 11, 15, 16, 27, 29], [15, 16, 34, 40, 42, 48], [9, 13, 21, 27, 42, 44], [3, 18, 23, 28, 33, 44]
    , [3, 11, 22, 28, 46, 49], [1, 7, 12, 37, 45, 49], [2, 7, 13, 22, 39, 48], [4, 13, 24, 34, 43, 44]
    , [15, 21, 22, 25, 35, 45], [10, 12, 17, 18, 20, 21, 26], [7, 10, 11, 25, 43, 36], [3, 8, 19, 20, 34, 41]
    , [8, 16, 18, 33, 37, 40], [2, 4, 11, 18, 34, 35], [5, 14, 19, 29, 31, 40], [14, 15, 22, 30, 32, 40]]
# enter your toto numbers here, a list of lists
RESULTS_TO_SEND = ""


def get_winning_numbers(webpage, current_index):
    global RESULTS_TO_SEND

    winning_numbers = []
    winning_number_start_index = current_index + 3
    additional_number_start_index = current_index + 10
    for i in range(winning_number_start_index, winning_number_start_index + 6):
        winning_numbers.append(int(webpage[i]))
    winning_numbers.append(int(webpage[additional_number_start_index]))
    RESULTS_TO_SEND += f'Winning numbers:{winning_numbers[:6]}, Additional number: {int(webpage[additional_number_start_index])}' + '\n' * 2
    return winning_numbers


def check_winning_numbers(winning_numbers, ticket):
    global RESULTS_TO_SEND
    additional_number = winning_numbers[-1]
    winning_numbers = winning_numbers[:6]
    print(winning_numbers)
    RESULTS_TO_SEND += f'Checking ticket:{ticket}' + '\n'
    total_points = 0.0

    won_numbers = list(set(winning_numbers).intersection(ticket))
    won_numbers.sort()
    total_points += len(won_numbers)
    if len(won_numbers) >= 3:
        RESULTS_TO_SEND += f'{len(won_numbers)} numbers TIO! {won_numbers}' + '\n'
    if additional_number in ticket:
        RESULTS_TO_SEND += f'ADDITIONAL NUMBER TIO:{additional_number}' + '\n'
        total_points += 0.5

    return total_points


def get_result_from_points(points):
    switcher = {
        6.0: 'GROUP 1 JACKPOT! HUAT ALR LO!',
        5.5: 'GROUP 2 PRIZE! 8% of prize pool',
        5.0: 'GROUP 3 PRIZE! 5.5% of prize pool',
        4.5: 'GROUP 4 PRIZE! 3% of prize pool',
        4.0: 'GROUP 5 PRIZE! $50',
        3.5: 'GROUP 6 PRIZE! $25',
        3.0: 'GROUP 7 PRIZE! $10'
    }

    return switcher.get(points, 'KI HONG GAN NEVER WIN MONEY LA!')


def check_results(webpage):
    global RESULTS_TO_SEND
    webpage = webpage.split('\n')
    webpage = [elem for elem in webpage if elem.strip()]
    while True:
        telebot.send_check_message(f'Starting TOTO scraper...')
        for i in range(len(webpage)):
            if DATE in webpage[i]:
                RESULTS_TO_SEND += f'FOUND DATE! [{DATE}]' + '\n' * 2
                winning_numbers = get_winning_numbers(webpage, i)
                RESULTS_TO_SEND += f'NUMBER OF TICKETS: {len(TICKETS)}' + '\n' * 2
                for ticket in TICKETS:
                    points = check_winning_numbers(winning_numbers, ticket)
                    result = get_result_from_points(points)
                    RESULTS_TO_SEND += result + '\n' * 2
                telebot.send_message(RESULTS_TO_SEND)
                return


page = urlopen(URL)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
check_results(soup.get_text())
