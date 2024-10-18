#!/usr/bin/env python3
from random import randrange

quotes = [
("All models are wrong, but some are useful.", "George Box"),
("Tell me and I will forget, show me and I may remember; involve me and I will understand.", "Confucius"),
("You can observe a lot just by watching.", "Yogi Berra"),
("The greatest deception men suffer is from their own opinions.", "Leonardo da Vinci"),
("The great tragedy of Science - the slaying of a beautiful hypothesis by an ugly fact.", "Thomas Huxley"),
("Did you know that ... the sun's tides on Earth are about one-third the strength of the moons tides?", "Neil deGrasse Tyson"),
("There are only 10 types of people in the world: those who understand binary, and those who don't.", ""),
("Mean-averages can be highly misleading when the raw data do not form a symmetric pattern.","David Spiegelhalter"),
("Did you know that ... we can use binary to count on our fingers up to 1023?","Eugenia Cheng"),
("The big lesson of physics over the centuries is how much is hidden from our view.","Lisa Randall"),
("Did you know that ... entropy is responsible for all of our experience of the flow of time?","Sean Carroll"),
("What is the world really? It is a quantum wave function.","Sean Carroll"),
("The standards by which we judge ourselves as being worthy are often so high, we settle for nothing less than perfect.","Will Storr"),
("All science is either physics or stamp collecting","Ernest Rutherford"),
("As far as we currently know, our Universe contains about 10^11 galaxies, 10^23 stars, 10^80 protons and 10^89 photons.","Max Tegmark"),
("Resentment is like taking poison and hoping the other person dies.","St Augustine"),
("The problem with people is that they're only human.", "Bill Watterson"),
("Science is a way of thinking much more than it is a body of knowledge.", "Carl Sagan"),
("No tendency is quite so strong in human nature as the desire to lay down rules of conduct for other people.", "William Howard Taft"),
("The difference between stupidity and genius is that genius has its limits.", "Albert Einstein"),
("Study hard what interests you the most in the most undisciplined, irreverent and original manner possible.", "Richard Feynman"),
("Not only is the Universe stranger than we think, it is stranger than we can think.", "Werner Heisenberg"),
("Questions you cannot answer are usually far better for you than answers you cannot question.", "Yuval Noah Harari"),
("To this day, I remain impressed by the ability of Britons of all ages and social backgrounds to get genuinely excited by the prospect of a hot beverage.", "Bill Bryson"),
("The theory of quantum electrodynamics describes Nature as absurd from the point of view of common sense. And it agrees fully with experiment. So I hope you accept Nature as She is—absurd", "Richard Feynman"),
("Did you know that within string theory ... each [elementary particle] would be seen to be made of a single, tiny, oscillating loop of string.", ""),
("Did you know that ... the number of atoms within us, is about a million times the number of stars in the entire visible universe.", "Frank Wilczek"),
("Space-time tells matter how to move; matter tells space-time how to bend.", "John Wheeler"),
("Did you know that ... the primary properties of matter, from which all its other properties can be derived are these three: mass, charge, spin.", "Frank Wilczek"),
("I haven't failed. I have just found 10,000 ways that won't work.", "Thomas A. Edison"),
("Falsehood flies, and truth comes limping after it", "Jonathan Swift"),
("Checking your likes is the new smoking", "Bill Maher"),
("Indeed, few things feel more basic to my experience of adulthood than the vague sense that I’m falling behind, and need to do more, if I’m to stave off an ill-defined catastrophe that might otherwise come crashing down upon my head.", "Oliver Burkeman")
]

i = randrange(len(quotes))
try:
    print("%s --%s"%(quotes[i]))
except:
    print(i, quotes[i])
    raise
