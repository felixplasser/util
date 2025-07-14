#!/usr/bin/env python3
from random import randrange
from textwrap import wrap

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
("The theory of quantum electrodynamics describes Nature as absurd from the point of view of common sense. And it agrees fully with experiment. So I hope you accept Nature as She is — absurd.", "Richard Feynman"),
("Did you know that within string theory ... each [elementary particle] would be seen to be made of a single, tiny, oscillating loop of string.", ""),
("Did you know that ... the number of atoms within us, is about a million times the number of stars in the entire visible universe.", "Frank Wilczek"),
("Space-time tells matter how to move; matter tells space-time how to bend.", "John Wheeler"),
("Did you know that ... the primary properties of matter, from which all its other properties can be derived are these three: mass, charge, spin.", "Frank Wilczek"),
("I haven't failed. I have just found 10,000 ways that won't work.", "Thomas A. Edison"),
("Falsehood flies, and truth comes limping after it.", "Jonathan Swift"),
("Checking your likes is the new smoking", "Bill Maher"),
("Indeed, few things feel more basic to my experience of adulthood than the vague sense that I’m falling behind, and need to do more, if I’m to stave off an ill-defined catastrophe that might otherwise come crashing down upon my head.", "Oliver Burkeman"),
("nullius in verba - take no one's word for it", "Royal Society"),
("You are the endpoint of an unbroken, billion-element chain of organisms each arising from the preceding generation: your parents, grandparents, great-grandparents, and so on, reaching all the way back to the last universal common ancestor of all life.", "Christof Koch"),
("There is no bad weather - there is only bad clothing and bad attitude.", "Christof Koch"),
("A crystal is like a class of children arranged for drill, but standing at ease, so that while the class as a whole has regularity both in time and space, each individual child is a little fidgety!", "Kathleen Lonsdale"),
("Do fewer things. Work at a natural pace. Obsess over quality.", "Cal Newport"),
("The quest for truth should always supersede one's ego defensive desire to be proven right.","Gad Saad"),
("Tact and diplomacy are fine in international relations, in politics, perhaps even in business; in science only one thing matters, that is the facts.","Hans J. Eysenck"),
("There are only two types of theories: those that divide the world into two types of theories, and those that do not.",""),
("But the peculiar evil of silencing the expression of an opinion is, that it is robbing the human race; posterity as well as the existing generation; those who dissent from the opinion, still more than those who hold it.","John Stuart Mill"),
("The easiest way to solve a problem is to deny that it exists.", "Isaac Asimov"),
("Nothing that is vast enters into the life of mortals without a curse", "Sophocles"),
("That you feel something to be right may have its cause in your never having thought much about yourself and in your blindly having accepted what has been labeled right since your childhood.", "Friedrich Nietzsche"),
("It is the incomplete revolutions which are remembered; the fate of those which triumph is to be taken for granted.", "Tom Holland"),
("The fact that we live at the bottom of a deep gravity well, on the surface of a gas covered planet going around a nuclear fireball 90 million miles away and think this to be normal is obviously some indication of how skewed our perspective tends to be.", "Douglas Adams"),
("The only way to know what’s happening in the world is to wade into cesspools on X, dodge 10 conspiracy theories, and emerge victorious with one nugget of actual true information.", "Nellie Bowles"),
("A new scientific truth does not triumph by convincing its opponents and making them see the light, but rather because its opponents eventually die and a new generation grows up that is familiar with it.", "Max Planck")
]

def cowsay(cowstr, wd=40):
    lines = wrap(cowstr, width=wd-2)
    if len(lines) == 1:
        left  = ['<']
        right = ['>']
    else:
        left  = ['\\'] + (len(lines)-2) * ['|'] + ['/']
        right = ['/']  + (len(lines)-2) * ['|'] + ['\\']

    outstr = ' ' + wd * '_' + '\n'
    for line in lines:
        outstr += left.pop() + line.center(wd) + right.pop() + "\n"
    outstr += ' ' + wd * '-'
    outstr += """
        \\   ^__^
         \\  (OO)\\_______
            (__)\\       )\\/\\
                ||----w |
                ||     ||
    """
    print(outstr)

if __name__=='__main__':
    i = randrange(len(quotes))
    try:
        cowstr = quotes[i][0]
        #print("%s --%s"%(quotes[i]))
    except:
        print(i, quotes[i])
        raise

    cowsay(cowstr)
