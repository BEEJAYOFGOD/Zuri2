class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, score, tracks=[]):
        self.tracks = tracks
        self.name = name
        self.age = int(age)
        self.score = float(score)

    def change_name(self, new_name):
        # To change the name of the student
        self.name = new_name

    def change_age(self, new_age):
        # to chnage the age of the student
        self.age = new_age

    def add_track(self, new_track):
        # to addd a track  to existing tracks
        self.tracks.append(new_track)

    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

print(f"{Bob.name} is {Bob.age} years old and is in the \
{Bob.tracks[0], Bob.tracks[1], Bob.tracks[2]} track with a score of {Bob.score}")
