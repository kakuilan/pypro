#!/usr/bin/python3
# coding: utf-8
# 随机发牌游戏

from random import shuffle

values = list(range(1, 11)) + 'Jack Queen King'.split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['{} of {}'.format(v,s) for v in values for s in suits]
shuffle(deck)

print('Game`s begining...\n')
while(len(deck)>0):
  chk = input('Do you continue? y/n ').strip()
  if(chk=='n'):
    print(chk, 'Game`s over!')
    break

  print("Your car is [{card}] , residue [{rem}] \n".format(card=deck.pop(), rem=len(deck) ))

