import pyautogui as gui


# Parte inferior - Base
gui.mouseDown(button='left', x=1328, y=683)
gui.moveTo(1328, 683, duration=0.5)
gui.moveTo(970, 787, duration=0.5)
gui.moveTo(641, 663, duration=0.5)
gui.moveTo(643, 645, duration=0.5)
gui.moveTo(971, 767, duration=0.5)
gui.moveTo(1327, 670, duration=0.5)
gui.moveTo(1328, 683, duration=0.5)
gui.moveTo(1327, 670, duration=0.5)
gui.moveTo(1034, 576,  duration=0.5)

# Parte Superior - Protetor da Tela
gui.moveTo(643, 645, duration=0.5)
gui.moveTo(557, 374, duration=0.5)
gui.moveTo(980, 383, duration=0.5)
gui.moveTo(980, 387, duration=0.5)
gui.moveTo(1034, 576,  duration=0.5)

gui.moveTo(643, 645, duration=0.5)
gui.moveTo(555, 377, duration=0.5)
gui.moveTo(980, 383, duration=0.5)
gui.moveTo(980, 387, duration=0.5)
gui.moveTo(1034, 576,  duration=0.5)

# Parte Inferior - Touchpad e Teclado

gui.moveTo(1327, 670, duration=0.5)
gui.moveTo(1190, 702, duration=0.5)
gui.moveTo(1128, 678, duration=0.5)
gui.moveTo(1018, 710, duration=0.5)
gui.moveTo(1076, 735)
gui.mouseUp()

gui.mouseDown(button='left', x=902, y=714)
gui.moveTo(902, 714, duration=0.5)
gui.moveTo(717, 645, duration=0.5)
gui.moveTo(1019, 590, duration=0.5)
gui.moveTo(1185, 643, duration=0.5)
gui.moveTo(902, 714, duration=0.5)
gui.moveTo(879, 706, duration=0.5)
gui.moveTo(1152, 634, duration=0.5)
gui.moveTo(1119, 623, duration=0.5)
gui.moveTo(842, 692, duration=0.5)
gui.moveTo(802, 675, duration=0.5)
gui.moveTo(1090, 614, duration=0.5)
gui.moveTo(1052, 600, duration=0.5)
gui.moveTo(757, 662, duration=0.5)
gui.moveTo(717, 645, duration=0.5)
gui.moveTo(754, 636, duration=0.5)
gui.moveTo(928, 705, duration=0.5)
gui.moveTo(960, 697, duration=0.5)
gui.moveTo(790, 632, duration=0.5)
gui.moveTo(841, 623, duration=0.5)
gui.moveTo(994, 690, duration=0.5)
gui.moveTo(1031, 681, duration=0.5)
gui.moveTo(880, 616, duration=0.5)
gui.moveTo(918, 609, duration=0.5)
gui.moveTo(1062, 670, duration=0.5)
gui.moveTo(1097, 661, duration=0.5)
gui.moveTo(958, 604, duration=0.5)
gui.moveTo(993, 597, duration=0.5)
gui.moveTo(1135, 651, duration=0.5)

gui.mouseUp()


# Parte Superior - Tela

gui.mouseDown(button='left', x=662, y=611)
gui.moveTo(662, 611, duration=0.5)
gui.moveTo(598, 415, duration=0.5)
gui.moveTo(963, 415, duration=0.5)
gui.moveTo(999, 557, duration=0.5)
gui.moveTo(662, 611, duration=0.5)
gui.mouseUp()

# Parte Superior - Texto

gui.moveTo(22, 430, duration=0.5)
gui.click(22, 430, duration=0.1)
gui.moveTo(735, 500, duration=0.5)
gui.click(735, 500, duration=0.5)
gui.keyDown('ctrl')
gui.keyDown('v')
gui.keyUp('v')
gui.keyUp('ctrl')

print("Fim da operação")
