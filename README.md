# Walkerbot
Code for simulating walking motion with the uArm Swift Pro.

GCC Senior Project. Codename: "Salsa Tequila"
- Adam Novak
- Michael Bender
- Sarah McKinnis
- Sarah Struble
- Brister Jones

Designed for use with GI PASS systems.

Making use of [uArm-Python-SDK](https://github.com/uArm-Developer/uArm-Python-SDK)

The folder titled "Examples" has scripts that were used in our testing and experimentation. Some are copied directly from the uArm Python SDK, but others are tests that we created to test our understanding of the documentation.

Important things that we discovered:
The set_polar() function seems to have issues when inputting more than two arguments at the time of writing, so set_position() is preferred. 

