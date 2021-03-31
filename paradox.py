import os
import random


class Paradox:
	s_door_h = {1,2,3}
	door_car = set()
	chosen_door = set()
	door_diff = set()
	door_goats = set()
	door_show_goat = 0
	second_choice = 0

	def __init__(self):
		self.door_car = set()
		self.chosen_door = set()

	def __str__(self):
		res = ''
		res += f's_door_h: {self.s_door_h}\n'
		res += f'door_car: {self.door_car}\n'
		res += f'chosen_door: {self.chosen_door}\n'
		res += f'door_diff: {self.door_diff}\n'
		res += f'door_show_goat: {self.door_show_goat}\n'
		res += f'door_goats: {self.door_goats}\n'
		res += f'second_choice: {self.second_choice}\n'
		return res

	def clear_screen(self):
		if os.name == 'nt':
			os.system('cls')  # For Windows
		else:
			os.system('clear')  # For Linux/OS X

	def difference(self):
		self.door_diff = self.s_door_h.difference(self.chosen_door)
		self.door_goats = self.s_door_h.difference(self.door_car)
		temp_door_goats = self.door_goats.difference(self.chosen_door)
		self.door_show_goat = random.choice(list(temp_door_goats))
		self.door_diff.discard(self.door_show_goat)
		for x in range(1,4):
			if x in self.door_diff:
				self.second_choice = x

	def hide_car(self):
		self.door_car.clear()
		self.door_car.add(int(random.randint(1,3)))

	def choice_door(self):
		self.chosen_door.clear()
		self.chosen_door.add(int(input('choise door number:')))
		self.difference()

	def decorate_doors(self, doors, stage) -> str:
		goat = '¥'
		# goat = 'Ÿ'
		car = '©'
		for door in doors:
			if stage>=2 and door == self.door_show_goat:
				doors[door] = goat
			if stage>2 and door in self.door_goats:
				doors[door] = goat
			if stage>2 and door in self.door_car:
				doors[door] = car

	def show_doors(self, stage=0):
		print('Welcome to game "Let’s Make a Deal"')
		print('\n'+'='*11+' Stage #'+str(stage)+' '+'='*11)
		print(' 1 - 2 - 3 ')
		doors = {
			1: '|',
			2: '|',
			3: '|',
		}
		self.decorate_doors(doors, stage)
		print(f'[{doors[1]}]-[{doors[2]}]-[{doors[3]}]')

	def show_player(self):
		pos_player = {
			1: '_',
			2: '_',
			3: '_',
		}
		for pos in pos_player:
			if pos in self.chosen_door:
				pos_player[pos] = '☺'
		print(f'_{pos_player[1]}___{pos_player[2]}___{pos_player[3]}_\n')

	def change_you_choice(self):
		answer = input('Do you want to change your choice? [y/n]: ')
		if answer.lower() == 'y':
			self.chosen_door.clear()
			self.chosen_door.add(self.second_choice)

	def show_time(self, stage=0):
		self.clear_screen()
		self.show_doors(stage)
		self.show_player()
		if stage==3:
			if self.chosen_door == self.door_car:
				print('winner! winner! chicken dinner!\n')
			else:
				print('You loser!\n')


if __name__=='__main__':
	par = Paradox()
	while True:
		par.hide_car()
		#1
		par.show_time(1)
		#2
		par.choice_door()
		par.show_time(2)
		#3
		par.change_you_choice()
		par.show_time(3)
		par.__init__()
		answer = input('Try again? [y/n]: ')
		if answer.lower() != 'y':
			break

	# print(par)
