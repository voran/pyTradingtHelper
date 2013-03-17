#
# TradingHelper.py - an tool that helps you make smart investment decisions written in Python3
# Copyright (C) Yavor Stoychev 2012 <stoychev.yavor@gmail.com>
#
# TradingHelper is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TradingHelper is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.

#Usage
#######################
#TradingHelper.py <price@day1, price@day2, ... price@dayN>
#######################

import sys

if __name__ == "__main__":
  profit_possible = False 		#assume that profit isn't possible
	price = sys.argv				#get parsed arguments
	price.pop(0)					#remove first parsed argument, since it's the name of the script
	for i in range(len(price)):
		price[i] = int(price[i])
	buy = 0							#we buy on day 1 (0 because of 0-based arrays)
	sellOffset = [0]*len(price)		#array that holds the number of days we should hold the stock before selling for each buy day
	profitArr = [0]*len(price)		#array that holds the maximum profit to be made for each buy day

	for day in range(1, len(price)):
		if price[day] > price[day - 1]:		#if price today is higher than price yesterday
			profit_possible = True			#we are making profit
			sellOffset[buy] += 1				#and we won't be selling yet
			profitArr[buy] += (price[day] - price[day - 1])	#the maximum profit we can make is incremented by the overnight price difference
		else:
			buy = day		#if price today is lower than price yesterday, we sell, and start considering a new interval
	if profit_possible:		#if profit is possible
		buy_opt = profitArr.index(max(profitArr))		#the best time to buy is the time with the greatest profit
		sell_opt = buy_opt + sellOffset[buy_opt]	#the best time to sell is the time to buy + the "sell offset"
		print(str(buy_opt+1) + " " + str(sell_opt+1))	#print values (add 1 because of 0-based arrays
	else:
		print("0 0")
