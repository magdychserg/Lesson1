# Расчет зарпалаты с помощию скрипта
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('-o', '--output_in_hours', type = int) # Выроботка в часах
parser.add_argument('-r', '--hourly_rate', type = float) # ставка в час
parser.add_argument('-b', '--bonus', type = int, default = 0) # Премия

args = parser.parse_args()
salary = args.output_in_hours*args.hourly_rate + args.bonus

print(f'You salary {salary} rub.')
