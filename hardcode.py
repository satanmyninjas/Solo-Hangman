"""
  a = "  |--------|"
  b = "  |         "
  c = "  |          "
  d = "  |         "
  e = "  |          "
  f = "  |           "
  g = "  |"
  h = "-----"
  if count == 0:
    pass

  if count >= 1:
    b = list(b)
    b[-1] = "O"
    b = ''.join(b)

  if count >= 2:
    c = list(c)
    c[-2] = "|"
    c = ''.join(c)

  if count >= 3:
    c = list(c)
    c[-3] = "/"
    c = ''.join(c)

  if count >= 4:
    c = list(c)
    c[-1] = "\ "
    c = ''.join(c)

  if count >= 5:
    d = list(d)
    d[-1] = "^"
    d = ''.join(d)

  if count >= 6:
    e = list(e)
    e[-3] = "/"
    e = ''.join(e)

  if count >= 7:
    e = list(e)
    e[-1] = "\ "
    e = ''.join(e)

  if count >= 8:
    f = list(f)
    f[-5] = "°"
    f = ''.join(f)

  if count == 9:
    f = list(f)
    f[-1] = "°"
    f = ''.join(f)
    game_run = False

  print(a)
  print(b)
  print(c)
  print(d)
  print(e)
  print(f)
  print(g)
  print(h)
"""


def gallows():

  """
  "|--------|"
  "|        "  # head
  "|       "  # torso, add extra space for last arm
  "|        "  # add carrot
  "|       "  # add leg, space, leg, space
  "|      "  # degree, 3 spaces, degree
  "|"
  "-----"
  """

  # what i'm basing the list off
  pieces = ["", "0", "/", "|", "\ ", "^", "/", " \ ", "°", "   °"]

  structure = ["|--------|",
               "|        ",
               "|       ",
               "|        ",
               "|       ",
               "|      ",
               "|",
               "-----"
               ]

  mistakes = 0
  # look over fibonacci generator for specific usage on other variables

  game_over_trigger = 9
  # trigger game over at this number

  # '\n '.join(structure)
  # structure[1] + pieces[1]
  # while statement below

  while mistakes < game_over_trigger:
      yield mistakes
      mistakes =+ 1
      structure[mistakes] + pieces[mistakes]

      if mistakes == game_over_trigger:
          f'GAME OVER! You made {mistakes} mistakes.'

  for i in structure:
      print(i)
