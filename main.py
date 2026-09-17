name = input("What is your name?: ")
age = input("How old are you?: ")
color = input("What is your favorite color?: ").strip()

print("Hello", name + "! You are", age, "and your favorite color is", color + ".")

color_roasts = {
	"blue": "Blue? Bold choice for someone who wants their personality in airplane mode.",
	"green": "Green? Very brave of you to choose the official color of unripe bananas.",
}

roast = color_roasts.get(color.lower())
if roast:
	print(roast)
else:
	print("Excellent choice! At least your color has escaped the roast list.")